import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot():
    # Specify the path to the CSV file
    file_path = r"C:\Python34\epa-sea-level.csv"
    data = pd.read_csv(file_path)

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Sea Level Data')

    # Calculate the first line of best fit (for the entire dataset)
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    sea_levels_predicted = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels_predicted, color='red', label='Line of Best Fit (1880-2050)')

    # Calculate the second line of best fit (from 2000 onwards)
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    recent_years_extended = pd.Series([i for i in range(2000, 2051)])
    recent_sea_levels_predicted = intercept_recent + slope_recent * recent_years_extended
    plt.plot(recent_years_extended, recent_sea_levels_predicted, color='green', label='Line of Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and show the plot
    plt.savefig('sea_level_plot.png')
    plt.show()

    return plt.gca()

# Execute the function to create and save the plot
if __name__ == "__main__":
    draw_plot()
