from src.comentario.models import Comentario
from src.proposta.models import Proposta
import datetime


def populate_db_fake():
    now = datetime.datetime.now().isoformat(timespec='seconds')
    Proposta.objects.create(
        component_id=3001,
        created_at=now,
        updated_at=now,
        votes_count=3204,
        title="Devemos acabar com a heterosexualidade",
        title_lang="pt-BR",
        body="Chega de ter que conviver com héteros, essa PEC visa ilegalizar comportamentos heterosexuais.",
        body_lang="pt-BR",
        comments_count=3
    ).save()
    Proposta.objects.create(
        component_id=3002,
        created_at=now,
        updated_at=now,
        votes_count=5120,
        title="Lanche de graça nas universidades",
        title_lang="pt-BR",
        body="Tornar todo e qualquer produto alimentício vendido dentro de universidades federais completamente gratuito.",
        body_lang="pt-BR",
        comments_count=2
    ).save()
    Proposta.objects.create(
        component_id=3003,
        created_at=now,
        updated_at=now,
        votes_count=2560,
        title="Bibliotecas 24 horas",
        title_lang="pt-BR",
        body="Permitir que bibliotecas de universidades públicas funcionem 24 horas por dia para auxiliar estudantes que preferem estudar em horários alternativos.",
        body_lang="pt-BR",
        comments_count=3
    ).save()
    Proposta.objects.create(
        component_id=3004,
        created_at=now,
        updated_at=now,
        votes_count=7321,
        title="Transporte público gratuito para estudantes",
        title_lang="pt-BR",
        body="Implementar passe livre no transporte público para alunos de universidades públicas como forma de incentivo à educação superior.",
        body_lang="pt-BR",
        comments_count=10
    ).save()
    Proposta.objects.create(
        component_id=3005,
        created_at=now,
        updated_at=now,
        votes_count=1920,
        title="Aumento do investimento em pesquisa",
        title_lang="pt-BR",
        body="Incrementar significativamente o financiamento destinado a projetos de pesquisa em universidades públicas para fomentar a inovação.",
        body_lang="pt-BR",
        comments_count=1
    ).save()
    Proposta.objects.create(
        component_id=3006,
        created_at=now,
        updated_at=now,
        votes_count=8450,
        title="Hortas comunitárias nas universidades",
        title_lang="pt-BR",
        body="Criação de hortas comunitárias em universidades públicas para promover a alimentação saudável e a sustentabilidade entre estudantes.",
        body_lang="pt-BR",
        comments_count=5
    ).save()
    Comentario.objects.create(
        commentable_id=1001,
        author_id=20,
        body="Que ideia horrivel",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3001,
        root_comment_id=1001,
        analyzed_at=now,
        sentiment=0,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1001,
        author_id=20,
        body="Eu apoio",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3001,
        root_comment_id=1001,
        analyzed_at=now,
        sentiment=3,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1002,
        author_id=21,
        body="Não concordo com essa proposta.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3002,
        root_comment_id=1002,
        analyzed_at=now,
        sentiment=1,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1003,
        author_id=22,
        body="Pode melhorar, mas é um bom começo.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3002,
        root_comment_id=1003,
        analyzed_at=now,
        sentiment=2,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1004,
        author_id=23,
        body="Excelente proposta, estou ansioso para ver isso acontecer.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3003,
        root_comment_id=1004,
        analyzed_at=now,
        sentiment=4,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1005,
        author_id=24,
        body="Isso é completamente inviável, precisamos de algo mais concreto.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3003,
        root_comment_id=1005,
        analyzed_at=now,
        sentiment=0,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1006,
        author_id=25,
        body="Estou neutro em relação a esta proposta.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3004,
        root_comment_id=1006,
        analyzed_at=now,
        sentiment=2,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1007,
        author_id=21,
        body="Concordo plenamente com a proposta!",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3004,
        root_comment_id=1007,
        analyzed_at=now,
        sentiment=4,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1008,
        author_id=22,
        body="Não acho que essa seja a melhor solução.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3005,
        root_comment_id=1008,
        analyzed_at=now,
        sentiment=1,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1009,
        author_id=23,
        body="Essa proposta é excelente, vai trazer muitos benefícios.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3005,
        root_comment_id=1009,
        analyzed_at=now,
        sentiment=4,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1010,
        author_id=24,
        body="Precisa de algumas melhorias, mas é um bom ponto de partida.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3006,
        root_comment_id=1010,
        analyzed_at=now,
        sentiment=2,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1011,
        author_id=25,
        body="Não estou convencido de que essa proposta funcionará.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3006,
        root_comment_id=1011,
        analyzed_at=now,
        sentiment=1,
        prompt_version="1.0"
    ).save()

    Comentario.objects.create(
        commentable_id=1012,
        author_id=21,
        body="Concordo plenamente com essa proposta.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3001,
        root_comment_id=1012,
        analyzed_at=now,
        sentiment=4,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1013,
        author_id=22,
        body="Não acho que seja uma boa ideia.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3002,
        root_comment_id=1013,
        analyzed_at=now,
        sentiment=1,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1014,
        author_id=23,
        body="Precisamos discutir mais sobre isso.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3003,
        root_comment_id=1014,
        analyzed_at=now,
        sentiment=2,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1015,
        author_id=24,
        body="Essa proposta é excelente! Vamos em frente!",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3004,
        root_comment_id=1015,
        analyzed_at=now,
        sentiment=4,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1016,
        author_id=25,
        body="Acho que precisamos de mais informações antes de decidir.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3005,
        root_comment_id=1016,
        analyzed_at=now,
        sentiment=2,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1017,
        author_id=26,
        body="A proposta é interessante, mas pode ter consequências negativas.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3006,
        root_comment_id=1017,
        analyzed_at=now,
        sentiment=1,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1018,
        author_id=27,
        body="Estou totalmente a favor! Precisamos de mudanças.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3003,
        root_comment_id=1018,
        analyzed_at=now,
        sentiment=4,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1019,
        author_id=28,
        body="Não entendo como isso pode ajudar.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3001,
        root_comment_id=1019,
        analyzed_at=now,
        sentiment=1,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1020,
        author_id=29,
        body="É uma proposta que merece nossa atenção.",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3005,
        root_comment_id=1020,
        analyzed_at=now,
        sentiment=3,
        prompt_version="1.0"
    ).save()
    Comentario.objects.create(
        commentable_id=1021,
        author_id=30,
        body="Pior proposta já feita",
        body_lang="pt-BR",
        created_at=now,
        updated_at=now,
        proposta=3004,
        root_comment_id=1021,
        analyzed_at=now,
        sentiment=0,
        prompt_version="1.0"
    ).save()
