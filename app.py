from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from palmerpenguins import load_penguins

# Load the Palmer Penguins dataset
penguins = load_penguins()

# Extract unique species for the dropdown
unique_species = penguins['species'].dropna().unique().tolist()

# Set Seaborn style for the plots
sns.set(style="whitegrid")

# Layout the UI with a title
app_ui = ui.page_fluid(
    ui.h2("Random Histogram and Palmer Penguins Scatterplot"),  # Title of the page
    ui.input_slider("selected_number_of_bins", "Number of Bins for Histogram", 1, 100, 20),  # Slider for histogram bins
    ui.output_plot("dist"),  # Output ID for histogram
    ui.input_select("species", "Select Species for Scatterplot", unique_species),  # Dropdown for species with all options
    ui.output_plot("scatterplot")  # Output for scatterplot
)

def server(input, output, session):
    @output
    @render.plot(alt="A histogram")
    def dist():
        # Use the slider value for the number of bins
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(437)  # Sample data
        plt.hist(x, bins=input.selected_number_of_bins(), density=True)  # Pass user input bins
        plt.title("Random Histogram")
        plt.xlabel("Value")
        plt.ylabel("Density")
        plt.grid(True)  # Optional: Add grid lines for better visibility

    @output
    @render.plot(alt="Palmer Penguins Scatterplot with Throughline")
    def scatterplot():
        # Load the Palmer Penguins dataset
        penguins = load_penguins()
        
        # Filter the dataset based on the selected species
        selected_species = input.species()
        if selected_species is not None:
            filtered_penguins = penguins[penguins["species"] == selected_species]
        else:
            filtered_penguins = penguins
        
        # Create a scatterplot of flipper length vs. body mass with a throughline
        plt.figure(figsize=(10, 6))
        
        # Create a color palette for the selected species
        palette = sns.color_palette("Set2", n_colors=1)  # Only need one color for the selected species
        
        # Create scatter plot with transparency
        sns.scatterplot(data=filtered_penguins, x="flipper_length_mm", y="body_mass_g",
                        color=palette[0], s=100, alpha=0.7, edgecolor='w')  # Edge color for better visibility

        # Add the regression line
        sns.regplot(data=filtered_penguins, x="flipper_length_mm", y="body_mass_g", 
                    scatter=False, color='red', label="Regression Line", ci=None)

        plt.title(f"Flipper Length vs. Body Mass of {selected_species} Penguins", fontsize=16)
        plt.xlabel("Flipper Length (mm)", fontsize=14)
        plt.ylabel("Body Mass (g)", fontsize=14)
        plt.legend(title="Species", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)  # Improved grid
        plt.tight_layout()  # Adjust layout

# Call App() to combine app_ui and server() into an interactive app
app = App(app_ui, server)
