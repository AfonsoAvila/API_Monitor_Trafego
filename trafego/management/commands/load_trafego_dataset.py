#--------------------# CREATE TO POPULATE THE DATABASE FROM GITHUB #--------------------#

from django.core.management.base import BaseCommand
import csv
import urllib.request
from trafego.models import SegEstrada

class Command(BaseCommand):
    help = 'A receber o CSV do GitHub'

    def handle(self, *args, **kwargs):
        github_url = 'https://raw.githubusercontent.com/Ubiwhere/Traffic-Speed/master/traffic_speed.csv'

        #Open csv
        response = urllib.request.urlopen(github_url)
        lines = [line.decode('utf-8') for line in response.readlines()]

        #maps the data as a dictionary
        reader = csv.DictReader(lines)
        for row in reader:
            #pass the strings in dict to float values so we can calculate and manipulate
            segment_id = int(row['ID'])
            long_start = float(row['Long_start'])
            lat_start = float(row['Lat_start'])
            long_end = float(row['Long_end'])
            lat_end = float(row['Lat_end'])
            length = float(row['Length'])
            speed = float(row['Speed'])

            #Verify if it exists in the database (update) if not, create new
            segment, created = SegEstrada.objects.update_or_create(
                id=segment_id,
                defaults={
                    'long_start': long_start,
                    'lat_start': lat_start,
                    'long_end': long_end,
                    'lat_end': lat_end,
                    'length': length,
                    'speed': speed,
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Novo segmento de estrada nº {segment_id}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Segmento nº {segment_id} updated'))

        self.stdout.write(self.style.SUCCESS('Ficheiro carregado com sucesso para a database!'))

