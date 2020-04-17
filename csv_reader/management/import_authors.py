import csv
from django.core.management.base import BaseCommand
from csv_reader.models import Authors

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_arguments ("C:/Users/ASUS/projetos_django/test_olist/csv_reader/fixtures/authors.csv", nargs=1, type=str)
    def handle(self, *args, **options):
        verbosity = options.get ("verbosity", NORMAL)
        file_path = options["C:/Users/ASUS/projetos_django/test_olist/csv_reader/fixtures/authors.csv"] [0]

        if verbosity >= NORMAL:
            self.stdout.write("=== importing data ===")

            with open(file_path) as f:
                reader = csv.reader(f)
                for row in enumerate(reader):
                    index, (name) = row
                    if index == 0:
                        continue
                authors, created = Authors.objects.get_or_created(
                    name=name,                    
                )
            if verbosity >= NORMAL:
                self.stdout.write(
                    f"{Authors.name}"
                )
                
