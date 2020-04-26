import csv
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from Authors_list.models import Authors
from .commands_utils import get_csv_file


class Command(BaseCommand):
    help = "Insert authors from a CSV file." \
           "CSV file name should be passed"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Authors

    def import_authors_to_db(self, author_name):
        try:
            self.model_name.objects.create(author_name=author_name)
        except Exception as e:
            raise CommandError("Error in inserting {}: {}".format(self.model_name, str(e)))
    
    def add_arguments(self, parser):
        parser.add_argument('filenames',
                            nargs='+',
                            type=str,
                            help="Inserts question from CSV file")
    
    def handle(self, *args, **options):
        for filename in options['filenames']:
            self.stdout.write(self.style.SUCCESS('Reading:{}'.format(filename)))
            file_path = get_csv_file(filename)
            try:
                with open(file_path) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for row in csv_reader:
                        if row != "":
                            author_name = [word.strip() for word in row][0]
                            self.import_authors_to_db(author_name)
                            self.stdout.write(self.style.SUCCESS('Added author: {}'.format(author_name)))
            except FileNotFoundError:
                raise CommandError("File {} does not exist".format(file_path))


    