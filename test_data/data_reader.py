import os
import csv
import random

class DataReader:
    @staticmethod
    def get_csv_data(relative_path):
        # Find the project root relative to the file data_reader.py
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        full_path = os.path.join(project_root, relative_path)

        rows = []
        with open(full_path, 'r', encoding='utf-8') as data_file:
            reader = csv.reader(data_file)
            next(reader, None)  # skip header
            for row in reader:
                rows.append(row)

        if not rows:
            raise ValueError("Plik CSV nie zawiera żadnych danych poza nagłówkiem.")

        return [random.choice(rows)]  # returns a list with one random row
