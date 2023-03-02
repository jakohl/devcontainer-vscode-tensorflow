
#FROM mcr.microsoft.com/devcontainers/base:ubuntu
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
# FROM mcr.microsoft.com/devcontainers/python:0-3.11
# FROM mcr.microsoft.com/vscode/devcontainers/anaconda:0.202.8-3

ARG USERNAME=vscode
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
        bzip2 \
        ca-certificates \
        # curl \
        libglib2.0-0 \
        libsm6 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxi6 \
        libxinerama1 \
        libxrandr2 \
        libxrender1 \
        mercurial \
        openssh-client \
        procps \
        subversion \
        wget \
        zlib1g \
    && apt-get upgrade -y 

RUN mkdir /opt/conda

# RUN curl --output anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
RUN wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh -O  anaconda.sh

RUN chmod +x anaconda.sh
# RUN sha256sum anaconda.sh
# e7ecbccbc197ebd7e1f211c59df2e37bc6959d081f2235d387e08c9026666acd

RUN rm -rf /opt/conda


RUN bash ./anaconda.sh -b -p /opt/conda

ENV LD_LIBRARY_PATH=/opt/conda/lib/:$LD_LIBRARY_PATH \
    PATH=/opt/conda/bin:$PATH
    
RUN conda init

# sha256sum anaconda.sh


# RUN wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda_11.7.0_515.43.04_linux.run 
# RUN wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
# RUN sudo sh cuda_11.7.0_515.43.04_linux.run --silent --override --toolkit --toolkitpath=/usr/local/cuda-versions/11.7
# RUN sudo sh cuda_11.7.0_515.43.04_linux.run --silent --override --toolkit
# RUN sudo sh cuda_11.8.0_520.61.05_linux.run --silent --override --toolkit




# RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin 

# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get install -y --no-install-recommends \
#         software-properties-common \
#     && apt-get upgrade -y 

# RUN sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
# RUN sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
# RUN sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"
# RUN sudo apt-get update

# RUN sudo apt-get install libcudnn8=8.8.0.121-1+cuda11.8
# RUN sudo apt-get install libcudnn8-dev=8.8.0.121-1+cuda11.8



# RUN wget https://developer.nvidia.com/downloads/c118-cudnn-local-repo-ubuntu2204-88012110-1amd64deb cudnn-local-repo-ubuntu2204-8.8.0.121_1.0-1_amd64.deb

# # RUN sudo dpkg -i cudnn-local-repo-${OS}-8.x.x.x_1.0-1_amd64.deb
# RUN sudo dpkg -i cudnn-local-repo-ubuntu2204-8.8.0.121_1.0-1_amd64.deb
# RUN sudo cp /var/cudnn-local-repo-*/cudnn-local-*-keyring.gpg /usr/share/keyrings/

# RUN sudo apt-get update

# RUN sudo apt-get install libcudnn8=8.8.0.121-1+cuda11.7
# RUN sudo apt-get install libcudnn8-dev=8.8.0.121-1+cuda11.7

# RUN conda config --set channel_priority strict
# RUN conda config --remove channels conda-forge
# RUN conda config --add channels conda-forge

# Copy environment.yml (if found) to a temp location so we can update the environment.
COPY environment.yml /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# Install the xz-utils package
# RUN apt-get update && apt-get install -y xz-utils

# RUN conda --version
# RUN python --version

# RUN conda --help

# RUN conda create -n python3.11 python=3.11
# RUN conda activate python3.11
# RUN conda install -y python=3.11
# RUN conda install -y -c conda-forge python=3.11

# RUN conda install -y -c conda-forge cudatoolkit=11.2.2 cudnn=8.1.0

# RUN conda uninstall python
# RUN conda install python=3.11
# RUN conda install -y -c conda-forge python=3.11

# RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
# ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
RUN mkdir -p /opt/conda/lib/nvvm/libdevice

RUN cp /opt/conda/lib/libdevice.10.bc /opt/conda/lib/nvvm/libdevice/

ENV LD_LIBRARY_PATH=/opt/conda/lib/:$LD_LIBRARY_PATH \
    PATH=/opt/conda/bin:$PATH \
    CUDA_DIR=/opt/conda/lib \
    XLA_FLAGS=--xla_gpu_cuda_data_dir=/opt/conda/lib 

# ENV LANG=C.UTF-8 \
#     LC_ALL=C.UTF-8 \
#     PATH=/opt/conda/bin:$PATH
    
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip 

# RUN python3 -m pip install tensorflow

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt



# WORKDIR /app


# COPY . .
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Requires the latest pip


# Current stable release for CPU and GPU
# pip install tensorflow


# RUN pip3 install --user -r requirements.txt



