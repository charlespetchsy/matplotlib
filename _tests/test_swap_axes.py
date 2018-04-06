import pytest
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison
import numpy as np

# ========== Symmetry Test====================
@image_comparison(baseline_images=['spines_axes_positions'], extensions=['png'])
def test_spines_axes_positions():
    fig1 = plt.figure(figsize=(5, 5))
    fig2 = plt.figure(figsize=(1, 5.5))

    # First figure 
    new_size = 1.1 * fig1.get_size_inches()
    fig1.set_size_inches(new_size)
    size1 = list(fig1.get_size_inches())

    # Second figure
    new_size1 = fig2.get_size_inches()
    fig2.set_size_inches(new_size1)
    size2 = list(fig2.get_size_inches())

    assert(size1[1] == size2[1])

