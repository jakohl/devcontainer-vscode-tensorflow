FROM tensorflow/tensorflow:2.15.0-gpu

RUN apt update \
    && apt-get -yq install git \
    && apt-get autoremove -y \
    && apt-get clean all

ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN addgroup --gid $USER_GID $USERNAME \
    && adduser --uid $USER_UID --gid $USER_GID --disabled-password --gecos "" $USERNAME
    
ENV PIP_ROOT_USER_ACTION=ignore
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip  \
    && pip install -r requirements.txt