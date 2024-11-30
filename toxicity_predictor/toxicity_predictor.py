import csv
import re

def raw_data_retrieval(filepath):
    raw_data = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                raw_data.append(line)
    except FileNotFoundError:
        print("File not found.")
        exit(1)
    raw_data = raw_data[1:]
    if not raw_data:
        print("File is empty.")
        exit(1)
    return raw_data


def get_drug_chars(line):
    fields = line.split(',')
    return fields[0], fields[1], fields[2], fields[3]

def preprocessing(filepath):
    return

a=1
c = raw_data_retrieval("/Users/rajesh/Desktop/workspace/toxicity_predictor/Medicine_Details.csv")
b=1