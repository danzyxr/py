import csv


def read_text(file):
    with open(file, "r") as f:
        data = f.readlines()
        return [line.strip() for line in data]

def convert_to_csv()