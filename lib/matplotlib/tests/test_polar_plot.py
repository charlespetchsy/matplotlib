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


@image_comparison(baseline_images=['notpolar_plot_bar'], extensions=['png'], style='mpl20')
def test_notpolar_plot_with_bar():
    angle = np.linspace(0.0, 2 * np.pi, 8, endpoint=False)
    radius = np.array([450, 500, 550, 600, 650, 700, 750, 800])
    err = radius / 12
    width = 2 * np.pi / 8

    ax = plt.subplot(1, 1, 1, polar=False)
    bars = ax.bar(angle, radius, width=width, bottom=0.0, yerr=err, capsize=5)
    ax.set_ylim(0, 950)


@image_comparison(baseline_images=['notpolar_plot_nobar'], extensions=['png'], style='mpl20')
def test_notpolar_plot_with_nobar():
    angle = np.linspace(0.0, 2 * np.pi, 8, endpoint=False)
    radius = np.array([450, 500, 550, 600, 650, 700, 750, 800])
    err = radius / 12
    width = 2 * np.pi / 8

    ax = plt.subplot(1, 1, 1, polar=False)
    bars = ax.bar(angle, radius, width=width, bottom=0.0, yerr=err)
    ax.set_ylim(0, 950)
