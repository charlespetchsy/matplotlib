import sys, matplotlib
import unittest
import matplotlib.pyplot as plt


# Run tests with tests.py
class TestInstallation(unittest.TestCase):

    # should show "This is a test to show installation worked" in the console
    # due to a change in line 1517 in _axes.py
    def test_plot(self):
        plt.plot([1, 2, 3, 4])

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    # Note: Backeend has already been set
    # If running on Ubuntu -> TKAgg


if __name__ == '__main__':
    unittest.main()
