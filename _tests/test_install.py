import unittest
import matplotlib.pyplot as plt
import sys


class TestInstallation(unittest.TestCase):

    # should show "This is a test to show installation worked" in the console
    # due to a change in line 1517 in _axes.py
    def test_plot(self):
        plt.plot([1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
