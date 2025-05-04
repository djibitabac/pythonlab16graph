# Lab16_pcarswel1.py
# Name: Djibril Ba
# This program reads unemployment data from a CSV file, prints the header using enumerate,
# and plots the unemployment rate over time using matplotlib.
# Date: 5/3/2025

"""
This script reads U.S. national unemployment data from 'OHRU.csv',
prints the header row using enumerate(), and plots the unemployment
rate over time using matplotlib. Dates are parsed using the datetime
module to properly format the x-axis.
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize empty lists to store dates and unemployment rates
dates = []
rates = []

# Open the CSV file containing unemployment data
with open('OHRU.csv', 'r') as file:
    reader = csv.reader(file)

    # Loop through each row using enumerate to track line numbers
    for i, row in enumerate(reader):
        if i == 0:
            # Print the header row (column names) from the CSV file
            print("Header:", row)
            continue  # Skip processing the header row

        # Parse the date from string format (YYYY-MM-DD) to a datetime object
        date = datetime.strptime(row[0], "%Y-%m-%d")

        # Convert the unemployment rate from string to float
        rate = float(row[1])

        # Append the parsed date and rate to their respective lists
        dates.append(date)
        rates.append(rate)

# Create a plot of unemployment rate over time
plt.figure(figsize=(12, 6))  # Set the figure size

# Plot the unemployment rate data
plt.plot(dates, rates, label='Unemployment Rate', color='blue')

# Label the axes
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')

# Add a title to the graph
plt.title('U.S. National Unemployment Rate Over Time')

# Display a grid for easier reading
plt.grid(True)

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the legend
plt.legend()

# Display the plot window
plt.show()
