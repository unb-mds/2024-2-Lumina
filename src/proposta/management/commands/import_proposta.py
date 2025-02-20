import re
import csv
import pandas as pd
from django.core.management.base import BaseCommand
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
            body = row['Body']
            body = re.sub(r'\{"pt-BR":\s*"(.*)"\}', r'\1', body)
            body = re.sub(r'(\n|\t)', '', body)
            body = re.sub(r'(\")', '"', body)

            Proposta.objects.create (
                component_id =  row['ID'],
                created_at =  row['Created At'],
                updated_at =  row['Updated At'],
                votes_count = row['Proposal Votes Count'],
                title =  re.sub(r'\{"pt-BR":\s*"(.*)"\}', r'\1', row['Title']),
                body = body,
                comments_count =  row['Comments Count'],
                topic = row['Topic']
            )
        
        self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(data)} records"))