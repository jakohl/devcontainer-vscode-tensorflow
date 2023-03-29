# Use a container as a full-featured development environment

The Visual Studio Code Dev Containers extension lets you use a container as a full-featured development environment. It allows you to open any folder inside (or mounted into) a container and take advantage of Visual Studio Code's full feature set. This is an example featuring a python/tensorflow environment together with some simple examples.

## Get Started

To use this template you should:

- install docker and make sure it is running with your default user permissions
- install Visual Studio Code
- install the Visual Studio Code extension "Dev Containers"
- in Visual Studio Code File > Open Folder > Folder_Of_This_Repository

Once everything is set up you can press F1 and type the command "Dev Containers: Rebuild and Reopen in Container". Press Enter. This will generate the Container and Open the Folder in the Container. You can now open a terminal in Visual Studio Code (Terminal > NewTerminal) and run the e.g. "python example_tensorflow.py".