import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(5, 5))

    def press(event):
        # Need to find method that returns window size
        print('Before resize, size is ', fig.get_size_inches())
        sz = 1.1 * fig.get_size_inches()
        print('Size will be set to ', sz)
        fig.set_size_inches(sz, forward=True)
        fig.canvas.draw()
        print('After resize, size is ', fig.get_size_inches())

    fig.canvas.mpl_connect('key_press_event', press)
    fig.show()
    input()
