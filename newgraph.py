# Lab16_1.py
# Name: Djibril Ba
# This program reads unemployment data from a CSV file,
# shows the header row, and plots unemployment rates over time.
# Date: 5/3/2025

"""
Reads unemployment data from 'OHRU.csv', prints the column headers,
and displays a line graph of U.S. unemployment rates over time.
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Lists to store the data from the CSV file
dates = []
rates = []

# Open and read the CSV file
with open('OHRU.csv', 'r') as file:
    reader = csv.reader(file)

    for i, row in enumerate(reader):
        if i == 0:
            # Print the header row
            print("Header:", row)
            continue

        # Convert date string to datetime object
        date = datetime.strptime(row[0], "%Y-%m-%d")

        # Convert rate string to float
        rate = float(row[1])

        # Add the values to our lists
        dates.append(date)
        rates.append(rate)

# Set the size of the graph
plt.figure(figsize=(12, 6))

# Plot the data
plt.plot(dates, rates, label='Unemployment Rate', color='blue')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.title('U.S. National Unemployment Rate Over Time')

# Add grid and legend
plt.grid(True)
plt.legend()

# Make sure layout fits and show the graph
plt.tight_layout()
plt.show()
