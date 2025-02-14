from pandas import DataFrame
from comentario.models import Comentario


def get_proposal_df(proposal_number: int) -> DataFrame:
    comment_list = Comentario.objects.filter(proposta_id=proposal_number)
    print(comment_list)
    print(len(comment_list))
    nomes = ['Muito Negativa', 'Negativa', 'Neutra', 'Positiva', 'Muito Positiva']
    result_df = [0, 0, 0, 0, 0]

    # if len(comment_list) != 0:
    for comment in comment_list:
        if 0 <= comment.sentiment <= 4:
            result_df[comment.sentiment] += 1
    print(result_df)
    df = DataFrame(data={'Opinião': nomes,
                         'Comentários': result_df})
    print(df)
    return df
