# demo script to test reading and writing files

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
print("Hello from the container and from file 'example_files.py'!")

# open text file to write string to file
text_file = open(file_path+"/data/data_of_example_files.txt", "w")
n = text_file.write('Hello World from the container!')
text_file.close()

# open text file an read the content
text_file = open(file_path+"/data/data_of_example_files.txt", "r")
lines = text_file.readlines()
text_file.close()

# Print content of data folder to inspect 
# permissions and ownership
os.system('ls -la '+file_path+"/data")