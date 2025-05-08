# Lab16_1.py
# Name: Djibril Ba
# Date: 5/8/2025
# This program reads unemployment data from a CSV file,
# shows the header row and plots unemployment rates over time

"""
Reads unemployment data from 'OHRU.csv', prints the column headers,
and displays a line graph of U.S. unemployment rates over time.
"""

import csv
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt


def read_unemployment_data(file_path):
    """Reads dates and unemployment rates from a CSV file."""
    dates = []
    rates = []

    try:
        with file_path.open('r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header:
                print("Header:", header)

    

            for row in reader:
                try:
                    date = datetime.strptime(row[0], "%Y-%m-%d")
                    rate = float(row[1])
                    dates.append(date)
                    rates.append(rate)
                except (ValueError, IndexError) as e:
                    print(f"Skipping invalid row: {row} - Error: {e}")




    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return [], []

    return dates, rates


def plot_unemployment(dates, rates):
    """Plots unemployment rates over time."""
    plt.figure(figsize=(12, 6))
    plt.plot(dates, rates, label='Unemployment Rate', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.title('U.S. National Unemployment Rate Over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    # Set up the path to the CSV file using pathlib for cross platform support
    file_path = Path("OHRU.csv")




    # Read and plot the data
    dates, rates = read_unemployment_data(file_path)

    if dates and rates:
        plot_unemployment(dates, rates)
    else:
        print("No valid data to plot.")


if __name__ == "__main__":
    main()
