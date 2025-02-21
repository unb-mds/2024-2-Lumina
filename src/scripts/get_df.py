from pandas import DataFrame
from comentario.models import Comentario


def get_proposal_dic(proposal_number: int) -> dict:
    comment_list = Comentario.objects.filter(proposta_id=proposal_number)

    labels = ['Muito Negativa', 'Negativa', 'Neutra', 'Positiva', 'Muito Positiva']
    values = [0, 0, 0, 0, 0]

    if len(comment_list) != 0:
        for comment in comment_list:
            if 0 <= comment.sentiment <= 4:
                values[comment.sentiment] += 1

    dic = {'Opinião': labels,
           'Comentários': values}
    print(dic)
    return dic


def get_proposal_df(proposal_number: int) -> DataFrame:
    data = get_proposal_dic(proposal_number)
    df = DataFrame(data={'Opinião': data['Opinião'], 'Comentários': data['Comentários']})
    print(df)
    return df
