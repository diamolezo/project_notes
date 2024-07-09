
import csv, os.path


def create_user_data():
    if not os.path.isfile(path):
        with open(path, 'w+', encoding='utf-8') as c_file:
            file_create = csv.writer(c_file, delimiter=",", lineterminator="\r")