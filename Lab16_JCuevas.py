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

def plot_data(months, unemployment_rates):
    """Generates and shows a line plot for unemployment rates."""
    plt.figure(figsize=(10, 6))
    plt.plot(months, unemployment_rates, linestyle='-', color='b', label="Unemployment Rate")
    plt.title("Unemployment Rate Over Time")
    plt.xlabel("Month")
    plt.ylabel("Unemployment Rate (%)")
    plt.xticks(rotation=45, ha='right')
    plt.xticks(range(0, len(months), max(1, len(months)//10)))
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

def main():
    """Main function to execute the reading and plotting of data."""
    
    current_dir = os.path.dirname(__file__)
    file_name = os.path.join(current_dir, "OHRU.csv")

    months, unemployment_rates = read_data(file_name)
    plot_data(months, unemployment_rates)

if __name__ == "__main__":
    main()

