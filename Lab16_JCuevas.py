import matplotlib.pyplot as plt
import csv
import os

def read_data(file_name):
    """Reads the CSV data and returns the data for plotting."""
    months = []
    unemployment_rates = []

    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for index, row in enumerate(reader):
            months.append(row[0])  
            unemployment_rates.append(float(row[1]))  

    return months, unemployment_rates 