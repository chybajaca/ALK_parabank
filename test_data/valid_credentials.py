import csv

class DataReader:
    @staticmethod
    def get_csv_data(filename):
        rows = []
        with open(filename, 'r') as data_file:
            reader = csv.reader(data_file)
            next(reader, None)  # Pomija nagłówki
            for row in reader:
                rows.append(row)
        return rows