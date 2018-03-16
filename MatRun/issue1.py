import matplotlib
matplotlib.use('TKAgg')
#matplotlib.use('QT5Agg')

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5., 5.))
def press(event):
    print('Before resize, size is ', fig.get_size_inches())
    sz = 1.1 * fig.get_size_inches()
    print('Size will be set to ', sz)
    fig.set_size_inches(sz)
    fig.canvas.draw()
    print('After resize, size is ', fig.get_size_inches(), "\n")
fig.canvas.mpl_connect('key_press_event', press)
fig.show()

input()
