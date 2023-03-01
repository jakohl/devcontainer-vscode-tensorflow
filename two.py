import os

# get path of current file
file_path = os.path.dirname(os.path.abspath(__file__))

# Say hello from the container
print("Hello from the container and from file 'two.py'!")


# open text file to write string to file
text_file = open(file_path+"/data/data_of_two.txt", "w")
n = text_file.write('Hello World from the container!')
text_file.close()


# open text file an read the content
text_file = open(file_path+"/data/data_of_two.txt", "r")
lines = text_file.readlines()
text_file.close()

