import numpy
import ciao_contrib.runtool as rt
from ciao_contrib.runtool import dmlist
print("hello world")
#dmlist('ngc1333.fits', 'blocks')
dmlist('csc2.fits', 'blocks')

import matplotlib.pyplot as plt
import numpy as np


# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()