
# FROM alpine:3.17.2
FROM tensorflow/tensorflow:2.11.0-gpu
# FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# ARG USERNAME=vscode
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get install -y --no-install-recommends \
#         bzip2 \
#         ca-certificates \
#         libglib2.0-0 \
#         libsm6 \
#         libxcomposite1 \
#         libxcursor1 \
#         libxdamage1 \
#         libxext6 \
#         libxfixes3 \
#         libxi6 \
#         libxinerama1 \
#         libxrandr2 \
#         libxrender1 \
#         mercurial \
#         openssh-client \
#         procps \
#         subversion \
#         wget \
#         zlib1g \
#     && apt-get upgrade -y 


# RUN wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh -O  anaconda.sh \
# && chmod +x anaconda.sh \
# && bash ./anaconda.sh -b -p /opt/conda 

# ENV LD_LIBRARY_PATH=/opt/conda/lib/:$LD_LIBRARY_PATH \
#     PATH=/opt/conda/bin:$PATH
    
# RUN conda init

# # Copy environment.yml to a temp location so we can update the environment.
# COPY environment.yml /tmp/conda-tmp/
# RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
#     && rm -rf /tmp/conda-tmp

# RUN mkdir -p /opt/conda/lib/nvvm/libdevice

# RUN cp /opt/conda/lib/libdevice.10.bc /opt/conda/lib/nvvm/libdevice/

# ENV LD_LIBRARY_PATH=/opt/conda/lib/:$LD_LIBRARY_PATH \
#     PATH=/opt/conda/bin:$PATH \
#     CUDA_DIR=/opt/conda/lib \
#     XLA_FLAGS=--xla_gpu_cuda_data_dir=/opt/conda/lib 

ENV PIP_ROOT_USER_ACTION=ignore
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip  \
&& pip install -r requirements.txt

# # WORKDIR /app