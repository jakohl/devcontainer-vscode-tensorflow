# Use a container as a full-featured development environment

The Visual Studio Code Dev Containers extension lets you use a container as a full-featured development environment. It allows you to open any folder inside (or mounted into) a container and take advantage of Visual Studio Code's full feature set. This is an example featuring a python/tensorflow environment together with some simple examples.

## Get Started

To use this template you should:

- install docker and make sure it is running with your default user permissions
- install Visual Studio Code
- install the Visual Studio Code extension Dev Containers
- in Visual Studio Code File > Open Folder > Folder_Of_This_Repository

Once everything is set up you can press F1 and type the command "Dev Containers: Rebuild and Reopen in Container". Press Enter. This will generate the Container and Open the Folder in the Container. You can now open a terminal in Visual Studio Code (Terminal > NewTerminal) and run the e.g. "python example_tensorflow.py".

## Customize Docker Image

You can customize the Docker image by altering the file `.devcontainer/Dockerfile`. See the Docker documentation for details.

## Customize pip packages

The Dockerfile in this example uses the file `.devcontainer/requirements.txt` to specify pip packages, which should be available in the Docker image. Use the syntax in the examples to specify specific versions of the pip packages. 

## Customize Extensions

You can customize the default VS Code Extensions, which are to be used in the container in the `.devcontainer/devcontainer.json` file using the extensions array.

## A note on gpu utilization

By installing Docker on Windows as Docker Desktop you should be able to use utilize gpus within a container per se. On e.g. Ubuntu some special packages need to be installed. [This guide](https://linuxhint.com/use-nvidia-gpu-docker-containers-ubuntu-22-04-lts/) may be helpful in this case.    

To utilize gpus within a container the `runArgs` needs to contain the `--gpus all` flag in the `.devcontainer/devcontainer.json` configuration file.

