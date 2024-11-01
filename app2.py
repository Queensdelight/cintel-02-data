from pathlib import Path

import pandas as pd


import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

file_path = Path(__file__).parent / "test_scores.csv"
df = pd.read_csv(file_path)


with ui.sidebar():
    ui.input_slider("n", "N", 0, 100, 20)


@render.plot(alt="A histogram")
def histogram():
    test_scores = df['Score'].values
    plt.hist(test_scores, input.n(), density=True)
