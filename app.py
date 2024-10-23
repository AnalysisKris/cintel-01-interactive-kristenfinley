from shiny import App, render, ui, Inputs
import matplotlib.pyplot as plt
import numpy as np

# Layout the UI with a title
app_ui = ui.page_fluid(
    ui.h2("Random Histogram Generator"),  # Title of the page
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20),  # Updated slider ID
    ui.output_plot("dist"),  # Output ID
)

def server(input, output, session):

    @render.plot(alt="A histogram")
    def dist():
        # Use the slider value for the number of bins
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(437)  # Sample data
        plt.hist(x, bins=input.selected_number_of_bins(), density=True)  # Pass user input bins

# Call App() to combine app_ui and server() into an interactive app
app = App(app_ui, server)
