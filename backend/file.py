import csv
import os

def append_file(path, new_data):
    fieldnames = ['id', 'problema', 'sintoma', 'causa', 'solucao']

    file_exists = os.path.isfile(path)
    with open(path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(new_data)

def remove_file(path, id):
    fieldnames = ['id', 'problema', 'sintoma', 'causa', 'solucao']

    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    new_data = [row for row in data if row['id'] != id]

    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_data)

def write_file(path, data):
    fieldnames = ['id', 'problema', 'sintoma', 'causa', 'solucao']

    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def read_file(path_csv):
    with open(path_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dados = list(reader)
    return dados