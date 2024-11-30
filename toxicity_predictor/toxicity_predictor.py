import csv

def raw_data_retrieval(filepath):
    raw_data = []
    with open(filepath, 'r') as file:
        for line in file:
            raw_data.append(line)
    return raw_data

def preprocessing_data(filepath):
    return