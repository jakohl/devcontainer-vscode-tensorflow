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


# create the data directory if it
# does not exist already
if not os.path.exists(file_path+"/data"):
    os.makedirs(file_path+"/data")


# Say hello from the container
print("Hello from the container and from file 'one.py'!")


# Some simple math to test the debugging 
# functionality
a = 1
b = 2
c = a + b
print(c)

# open text file to write string to file
text_file = open(file_path+"/data/data_of_one.txt", "w")
n = text_file.write('Hello World from the container!')
text_file.close()


# open text file an read the content
text_file = open(file_path+"/data/data_of_one.txt", "r")
lines = text_file.readlines()
text_file.close()


# Some demo task to test the 
# dependency management with pip
# (here numpy, scipy and matplotlib)

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

plt.savefig(file_path+'/data/interpolations.png')


# Print content of data folder to inspect 
# permissions and ownership
os.system('ls -la '+file_path+"/data")
