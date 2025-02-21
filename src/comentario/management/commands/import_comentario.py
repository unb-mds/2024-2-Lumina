import re
import csv
import pandas as pd
from django.core.management.base import BaseCommand
from comentario.models import Comentario
from proposta.models import Proposta

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Read CSV using pandas
        data = pd.read_csv(csv_file)

        # Loop over rows in CSV
        for index, row in data.iterrows():
            proposta_id = row['Decidim Root Commentable ID']
            proposta, created = Proposta.objects.get_or_create(component_id = proposta_id)

            Comentario.objects.create (
                commentable_type = row['Decidim Commentable Type'],
                commentable_id = row['ID'],
                author_id = row['Decidim Author ID'],
                body = re.sub(r'\{"pt-BR":\s*"(.*)"\}', r'\1', row['Body']),
                created_at = row['Created At'],
                updated_at = row['Updated At'],
                proposta = proposta
            )
        
        self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(data)} records"))