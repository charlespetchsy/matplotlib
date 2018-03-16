import numpy as np
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['polar_1'],
                 extensions=['png'], style='default')
def test_polar_plot():
    angle = np.linspace(0.0, 2 * np.pi, 8, endpoint=False)
    radius = np.array([450, 500, 550, 600, 650, 700, 750, 800])
    err = radius/12
    width = 2 * np.pi / 8

    ax = plt.subplot(1, 1, 1, polar=True)
    bars = ax.bar(angle, radius, width=width, bottom=0.0, yerr=err, capsize=10)
    ax.set_ylim(0,950)
