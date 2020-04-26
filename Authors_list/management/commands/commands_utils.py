import os
from django.apps import apps


def get_current_app_path():
    return apps.get_app_config('Authors_list').path

def get_csv_file(filename):
    app_path = get_current_app_path()
    file_path = os.path.join(app_path, "management", "commands", filename)
    return file_path