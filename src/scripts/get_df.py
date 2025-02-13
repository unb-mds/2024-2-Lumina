from django.contrib.gis.gdal.prototypes.geom import is_empty
from pandas import DataFrame
from comentario.models import Comentario


def get_proposal_df(proposal_number: int) -> DataFrame:
    comment_list = Comentario.objects.filter(proposta__exact=proposal_number)
    result_df = {'Opinião': ['Muito Negativa', 'Negativa', 'Neutra', 'Positiva', 'Muito Positiva'],
                 'Comentários': [0, 0, 0, 0, 0]}

    if len(comment_list) != 0:
        for comment in comment_list:
            if 0 >= comment.sentiment <= 4:
                result_df['Comentários'][comment.sentiment] += 1
    return DataFrame(result_df)
