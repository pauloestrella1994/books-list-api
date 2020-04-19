from django.core.management.base import BaseCommand
from Authors_list.models import Authors

class Command(BaseCommand):
    help = "With this command, you can import your csv file with authors data into your database"
    
    def  __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__data = []
        self.__info = []
    
    def add_arguments(self, parser):
        parser.add_arguments()