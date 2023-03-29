# demo script to test the 
# dependency management with pip
# (here numpy, scipy and matplotlib)

import numpy as np
from scipy.interpolate import RBFInterpolator, InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
import os


# Set the umask value to 0
# to enable write permissions for 
# group and others
os.umask(0) 

# get path of current file
file_path = os.path.dirname(os.path.abspath(__file__))

# setup data
x = np.linspace(0, 10, 9).reshape(-1, 1)
y = np.sin(x)
xi = np.linspace(0, 10, 101).reshape(-1, 1)

# use fitpack2 method
ius = InterpolatedUnivariateSpline(x, y)
yi = ius(xi)

plt.subplot(2, 1, 1)
plt.plot(x, y, 'bo')
plt.plot(xi, yi, 'g')
plt.plot(xi, np.sin(xi), 'r')
plt.title('Interpolation using univariate spline')

# use RBF method
rbf = RBFInterpolator(x, y)
fi = rbf(xi)

plt.subplot(2, 1, 2)
plt.plot(x, y, 'bo')
plt.plot(xi, fi, 'g')
plt.plot(xi, np.sin(xi), 'r')
plt.title('Interpolation using RBF - multiquadrics')
plt.show()

plt.savefig(file_path+'/data/plot_of_example_interpolation.png')
