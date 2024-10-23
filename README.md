# Assignment - Browser Interactive App: Slider Input & Histogram Output

## Objective
To implement a working interactive web app written in Python running in the browser, using Shiny Playground.

## Overview
This project is a Shiny application built with Python to visualize data from the **Palmer Penguins** dataset. The application features two main components:
1. A histogram generator for visualizing random data.
2. A scatter plot for exploring the relationship between flipper length and body mass for different penguin species.

## Features
- **Random Histogram**: Users can adjust the number of bins for the histogram using a slider. The histogram visualizes random normally distributed data.
- **Scatter Plot**: Users can select their favorite penguin species from a dropdown menu to view a scatter plot of flipper length versus body mass. A regression line is included to highlight trends in the data.

## Technologies Used
- Python
- Shiny for Python
- Matplotlib for plotting
- Seaborn for enhanced data visualization
- Palmer Penguins dataset from the `palmerpenguins` library
- NumPy and Pandas for data manipulation

## Getting Started
To run the application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
