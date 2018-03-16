import pytest
import matplotlib.pyplot as plt
import numpy as np

# ========== Test for height changes ====================

def test_canvas_size_square1():
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

def test_canvas_size2_sqaure2():
    fig1 = plt.figure(figsize=(5, 5))
    fig2 = plt.figure(figsize=(1, 5.525))

    # First figure
    new_size = 1.105 * fig1.get_size_inches()
    fig1.set_size_inches(new_size)
    size1 = list(fig1.get_size_inches())

    # Second figure
    new_size1 = fig2.get_size_inches()
    fig2.set_size_inches(new_size1)
    size2 = list(fig2.get_size_inches())

    assert(size1[1] == size2[1])

def test_canvas_size2_rect1():
    fig1 = plt.figure(figsize=(5, 3))
    fig2 = plt.figure(figsize=(1, 3.315))

    # First figure
    new_size = 1.105 * fig1.get_size_inches()
    fig1.set_size_inches(new_size)
    size1 = list(fig1.get_size_inches())

    # Second figure
    new_size1 = fig2.get_size_inches()
    fig2.set_size_inches(new_size1)
    size2 = list(fig2.get_size_inches())

    assert(size1[1] == size2[1])

def test_canvas_size2_rect2():
    fig1 = plt.figure(figsize=(8, 6))
    fig2 = plt.figure(figsize=(1, 6.63))

    # First figure
    new_size = 1.105 * fig1.get_size_inches()
    fig1.set_size_inches(new_size)
    size1 = list(fig1.get_size_inches())

    # Second figure
    new_size1 = fig2.get_size_inches()
    fig2.set_size_inches(new_size1)
    size2 = list(fig2.get_size_inches())

    assert(size1[1] == size2[1])

# ========== Test for proportion ====================

def test_canvas_size_prop1():
    fig1 = plt.figure(figsize=(8, 6))
    fig2 = plt.figure(figsize=(8.8, 6.6))

    # First figure
    new_size = 1.1 * fig1.get_size_inches()
    fig1.set_size_inches(new_size)
    size1 = list(fig1.get_size_inches())

    # Second figure
    new_size1 = fig2.get_size_inches()
    fig2.set_size_inches(new_size1)
    size2 = list(fig2.get_size_inches())

    assert(np.round(sum(size1), 5) == sum(size2))

def test_canvas_size_prop2():
    fig1 = plt.figure(figsize=(5, 5))
    fig2 = plt.figure(figsize=(6.16, 6.16))

    # First figure
    new_size = 1.232 * fig1.get_size_inches()
    fig1.set_size_inches(new_size)
    size1 = list(fig1.get_size_inches())

    # Second figure
    new_size1 = fig2.get_size_inches()
    fig2.set_size_inches(new_size1)
    size2 = list(fig2.get_size_inches())

    assert(sum(size1) == sum(size2))

def test_canvas_size_prop3():
    fig1 = plt.figure(figsize=(2, 8))
    fig2 = plt.figure(figsize=(2.2, 8.8))

    # First figure
    new_size = 1.1 * fig1.get_size_inches()
    fig1.set_size_inches(new_size)
    size1 = list(fig1.get_size_inches())

    # Second figure
    new_size1 = fig2.get_size_inches()
    fig2.set_size_inches(new_size1)
    size2 = list(fig2.get_size_inches())

    assert(sum(size1) == sum(size2))

