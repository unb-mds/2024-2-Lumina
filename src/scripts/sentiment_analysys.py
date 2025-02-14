import json
from datetime import datetime, date
from django.db.models import QuerySet
from openai import OpenAI
from pydantic import BaseModel
from comentario.models import Comentario
from time import sleep
import os


class Prompts:
    sentiment_analysis_v1 = """Perform sentiment analysis on a given Brazilian Portuguese comment. Determine the sentiment score and output it as a number ranging from 0 to 5, where 0 indicates very negative sentiment and 5 indicates very positive sentiment.

# Steps

1. *Read and Understand the Comment*: Thoroughly read and understand the context and content of the comment.
2. *Identify Sentiment Indicators*: Look for words, phrases, and overall tone that indicate sentiment—positive (e.g., "bom," "excelente"), negative (e.g., "ruim," "horrível"), or neutral (e.g., "ok," "normal").
3. *Assess the Sentiment*: Consider the implications of sentiment indicators and the context provided in the comment to identify the overall sentiment.
4. *Assign a Score*: Based on the analysis, assign a score from 0 (very negative) to 4 (very positive).

# Output Format

The output should be in JSON format specifying the identified sentiment category:
```json
{
  "comment": "[original comment]",
  "sentiment": "[0-4]"
}

# Examples

*Example 1:*

- *Input:* "Que ideia horrível, volte pra escola!"
- *Reasoning:* The words "horrível" (horrible) and "volte pra escola" (go back to school) indicate a strong negative sentiment.
- *Output:*
{
  "comment": "Que ideia horrível, volte pra escola!",
  "sentiment": "0"
}

*Example 2:*

- *Input:* "Adorei a ideia, realmente faz muito sentido esse curso de ação."
- *Reasoning:* The words "adorei" (loved) and "realmente faz sentido" (really makes sense) indicate a strong positive sentiment.
- *Output:*
{
  "comment": "Adorei a ideia, realmente faz muito sentido esse curso de ação.",
  "sentiment": "4"
}

*Example 3:*

- *Input:* "Amei! Só precisar mudar tudo!"
- *Reasoning:* The word "amei" (loved it) could indicate positive sentiment, but the term "só precisa mudar tudo" (you only need to change everything) indicates irony and that the writer had a really negative sentiment.
- *Output:*
{
  "comment": "Amei! Só precisar mudar tudo!",
  "sentiment": "0"
}

*Example 4:*

- *Input:* "Não entendi. O que foi levantado?"
- *Reasoning:* The comment doesn't have any strong wording or context.
- *Output:*
{
  "comment": "Não entendi. O que foi levantado?",
  "sentiment": "2"
}

# Notes

- Neutral comments that neither praise nor criticize explicitly should fall in the 1-3 range.
- Consider linguistic nuances and colloquialisms specific to Brazilian Portuguese.
- Pay attention to context clues that might indicate sarcasm or irony, which can affect the perceived sentiment."""

    sentiment_analysis_v2 = """Perform sentiment analysis on comments from a government proposal website. The comments should be categorized with a number from 0 to 4, where 0 represents a very negative comment, 2 represents a neutral comment, and 4 represents a very positive comment.

# Steps

1. **Read the Comment**: Carefully read and understand the comment to capture its essence.
2. **Identify Sentiment Indicators**: Look for words and phrases that indicate positive, negative, or neutral sentiment.
3. **Determine Sentiment Level**: Assess the overall sentiment of the comment based on identified indicators and context, paying attention to sarcasm or irony, and classify it on a scale from 0 to 4.
4. **JSON Output**: Construct a JSON formatted response with the resulting sentiment score.

# Output Format

The output should be formatted as a JSON object with a single field:
```json
{
  "sentiment": [0-4]
}
```"""


class Sentiment(BaseModel):
    sentiment: int


def get_response(message, sys_prompt):
    client = OpenAI(
        api_key=os.getenv("LUMINA_OPENAI_API_KEY"))

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": message},
        ],
        response_format=Sentiment,
        temperature=0.1,
        max_completion_tokens=35,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].message.parsed


def str_response(sentiment: int):
    data = ["Muito negativo", "Negativo", "Neutro", "Positivo", "Muito positivo"]
    return data[sentiment]


def analyze_sentiment(text: str) -> int:
    result = get_response(text, Prompts.sentiment_analysis_v2)
    try:
        sentiment_value = int(result.sentiment)
        if 0 <= sentiment_value <= 4:
            return sentiment_value
        else:
            raise ValueError
    except ValueError:
        return -1


def get_comments(since: datetime | None = None, max_comments: int = 500) -> QuerySet[Comentario]:
    if since is None:
        comment_list = Comentario.objects.filter(sentiment=-1)
    else:
        comment_list = Comentario.objects.filter(sentiment=-1, updated_at__gt=since)

    comment_list: QuerySet[Comentario] = comment_list.order_by('updated_at')[:max_comments]
    return comment_list


def get_tasks_file(comment_list: QuerySet[Comentario]) -> str:
    tasks = []
    now = datetime.now()

    # Create task list
    for comment in comment_list:
        task = {
            "custom_id": comment.id,
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                # This is what you would have in your Chat Completions API call
                "model": "gpt-4o-mini",
                "temperature": 0.1,
                "response_format": {
                    "type": "json_object"
                },
                "messages": [
                    {
                        "role": "system",
                        "content": Prompts.sentiment_analysis_v2
                    },
                    {
                        "role": "user",
                        "content": comment.body
                    }
                ],
            }
        }
        tasks.append(task)

    file_name = f"batch/source/batch_{now.date().isoformat()}_{datetime.time(now)}.jsonl"

    # Create file and write lines
    with open(file_name, 'w') as file:
        for obj in tasks:
            file.write(json.dumps(obj) + '\n')

    return file_name


def save_to_db(results: list[dict], start_time: datetime):
    for result in results:
        comment = Comentario.objects.get(id=result["custom_id"])
        comment.sentiment = result["sentiment"]
        comment.analyzed_at = start_time
        comment.save()


def serial_analysis(since: datetime | None = None, max_comments: int = 500, delay: int | float = 0):
    now = datetime.now()
    comment_list = get_comments(since, max_comments)
    for comment in comment_list:
        sentiment = analyze_sentiment(comment.body)
        comment.sentiment = sentiment
        comment.analyzed_at = now
        comment.save()
        sleep(delay)


def batch_analysis(since: datetime | None = None, max_comments: int = 500):
    # Initialize OpenAI client and variables
    client = OpenAI(api_key=os.getenv("LUMINA_OPENAI_API_KEY"))
    comment_list = get_comments(since, max_comments)
    file_name = get_tasks_file(comment_list)
    start_time = datetime.now()

    # Upload file to OpenAI
    batch_file = client.files.create(
        file=open(file_name, "rb"),
        purpose="batch"
    )

    # Create batch job
    batch_job = client.batches.create(
        input_file_id=batch_file.id,
        endpoint="/v1/chat/completions",
        completion_window="24h"
    )

    # Retrieve batch object
    batch_job = client.batches.retrieve(batch_job.id)

    # Wait for batch job to complete
    while True:
        status = batch_job.status

        match status:
            case "validating" | "finalizing" | "cancelling":
                sleep(15)
            case "in_progress":
                sleep(40)
            case "completed":
                break
            case "failed":
                pass
            case "expired" | "cancelled":
                pass

    # Retrieve result file
    result_file_id = batch_job.output_file_id
    result = client.files.content(result_file_id).content

    result_file_name = "batch/result/" + file_name.split("/")[2].replace(".jsonl", "_result.jsonl")

    # Save result file
    with open(result_file_name, 'wb') as file:
        file.write(result)

    # Parse result file as list of dicts
    results = []
    with open(result_file_name, 'r') as file:
        for line in file:
            # Parsing the JSON string into a dict and appending to the list of results
            json_object = json.loads(line.strip())
            results.append(json_object)

    # Save results to database
    save_to_db(results, start_time)
