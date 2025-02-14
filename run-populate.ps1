Write-Host "Populate Proposta"
docker exec lumina-web python src/manage.py import_proposta data/query_result_2024-12-09T14_15_28.94723Z.csv

# Populate Comentario
Write-Host "Populate Comentario"
docker exec lumina-web python src/manage.py import_comentario data/query_result_2024-12-09T16_29_01.331387Z.csv