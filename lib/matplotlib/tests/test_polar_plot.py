import numpy as np
import matplotlib
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


@image_comparison(baseline_images=['polar_plot_1_bar'], extensions=['png'], style='mpl20')
def test_polar_plot_1_with_bar_fixed():
    angle = np.linspace(0.0, 2 * np.pi, 8, endpoint=False)
    radius = np.array([450, 500, 550, 600, 650, 700, 750, 800])
    err = radius / 12
    width = 2 * np.pi / 8

    ax = plt.subplot(1, 1, 1, polar=True)
    bars = ax.bar(angle, radius, width=width, bottom=0.0, yerr=err, capsize=10)
    ax.set_ylim(0, 950)


@image_comparison(baseline_images=['polar_plot_1_nobar'], extensions=['png'], style='mpl20')
def test_polar_plot_1_with_nobar():
    angle = np.linspace(0.0, 2 * np.pi, 8, endpoint=False)
    radius = np.array([450, 500, 550, 600, 650, 700, 750, 800])
    err = radius / 12
    width = 2 * np.pi / 8

    ax = plt.subplot(1, 1, 1, polar=True)
    bars = ax.bar(angle, radius, width=width, bottom=0.0, yerr=err)
    ax.set_ylim(0, 950)


@image_comparison(baseline_images=['polar_plot_2_bar'], extensions=['png'], style='mpl20')
def test_polar_plot_2_with_bar():
    fig = plt.figure()
    ax = plt.axes(polar=True)

    r = np.array([5.31, 5.29, 5.25, 5.19, 5.09, 4.92, 4.67, 4.27, 3.75, 3.56])
    theta = 2 * np.pi / 360 * np.array(list(range(0, 100, 10)))

    ax.plot(theta, r, "ro")
    ax.errorbar(theta, r, yerr=1, xerr=.1, capsize=5)


@image_comparison(baseline_images=['polar_plot_2_nobar'], extensions=['png'], style='mpl20')
def test_polar_plot_2_with_nobar():
    fig = plt.figure()
    ax = plt.axes(polar=True)

    r = np.array([5.31, 5.29, 5.25, 5.19, 5.09, 4.92, 4.67, 4.27, 3.75, 3.56])
    theta = 2 * np.pi / 360 * np.array(list(range(0, 100, 10)))

    ax.plot(theta, r, "ro")
    ax.errorbar(theta, r, yerr=1, xerr=.1)


@image_comparison(baseline_images=['polar_plot_2_nobar'], extensions=['png'], style='mpl20')
def test_polar_plot_3_with_bar():
    # From https://matplotlib.org/gallery/statistics/boxplot_demo.html

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # fake up some data
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low), 0)

    fig, axs = plt.subplots(2, 3)

    # basic plot
    axs[0, 0].boxplot(data)
    axs[0, 0].set_title('basic plot')

    # notched plot
    axs[0, 1].boxplot(data, 1)
    axs[0, 1].set_title('notched plot')

    # change outlier point symbols
    axs[0, 2].boxplot(data, 0, 'gD')
    axs[0, 2].set_title('change outlier\npoint symbols')

    # don't show outlier points
    axs[1, 0].boxplot(data, 0, '')
    axs[1, 0].set_title("don't show\noutlier points")

    # horizontal boxes
    axs[1, 1].boxplot(data, 0, 'rs', 0)
    axs[1, 1].set_title('horizontal boxes')

    # change whisker length
    axs[1, 2].boxplot(data, 0, 'rs', 0, 0.75)
    axs[1, 2].set_title('change whisker length')

    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                        hspace=0.4, wspace=0.3)
