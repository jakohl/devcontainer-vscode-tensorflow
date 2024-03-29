# demo script to test notebook functionalities
# hover over "# %%" and click "Run cell" to run a cell
# (view the plot, print a variable, ...)

# %%
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

# fig.savefig("test.png")
plt.show()

# %%
a=1
b=a-3
b


# %%
