import pytest
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison
import numpy as np

# =================TESTING DIFFERENCE FUNCTIONS ======================
@image_comparison(baseline_images=['swap_x_squared'], extensions=['png'])
def test_polynomial_plot():
    t = np.arange(0, 10, 0.1)
    a = t**2
    plt.plot(t, a, 'sw')

@image_comparison(baseline_images=['swap_linear'], extensions=['png'])
def test_linear_plot():
    t = np.arange(0, 10, 0.1)
    a = t
    plt.plot(t, a, 'sw')

@image_comparison(baseline_images=['swap_sine'], extensions=['png'])
def test_sine_plot():
    t = np.arange(0, 10, 0.1)
    a = np.sin(t)
    plt.plot(t, a, 'sw')

@image_comparison(baseline_images=['swap_cosine'], extensions=['png'])
def test_cosine_plot():
    t = np.arange(0, 10, 0.1)
    a = np.cos(t)
    plt.plot(t, a, 'sw')



