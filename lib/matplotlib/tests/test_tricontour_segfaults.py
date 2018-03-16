import numpy as np
import matplotlib.pyplot as plt
import pytest


def errFunc1():
    x, y = np.meshgrid(np.arange(10), np.arange(10))
    z = x ** 2. + y ** 2.
    z[x < y] = np.nan
    fig, ax = plt.subplots()
    ax.tricontourf(x.ravel(), y.ravel(), z.ravel())

def errFunc2():
    x, y = np.meshgrid(np.arange(10), np.arange(10))
    z = x ** 2. + y ** 2.
    z[x < y] = np.inf
    fig, ax = plt.subplots()
    ax.tricontourf(x.ravel(), y.ravel(), z.ravel())
    
def func3():
    x, y = np.meshgrid(np.arange(10), np.arange(10))
    z = x ** 2. + y ** 2.
    fig, ax = plt.subplots()
    ax.tricontourf(x.ravel(), y.ravel(), z.ravel())

def test_contour_nan():
    with pytest.raises(ValueError):
        errFunc1()

def test_contour_inf():
    with pytest.raises(ValueError):
        errFunc2()
        
def test_contour_no_inf_or_nan():
    func3()
