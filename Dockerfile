FROM python:3.12-slim-bookworm as python-base

# gcc is required to install some dependencies,
# postgres is required for pg interaction
RUN apt-get update
RUN apt-get install -y gcc

#install postgres library
RUN apt-get install -y libpq-dev

# Default user id's and name
ARG USER_GID=1001
ARG USER_UID=1001
ARG USER_NAME=ghentcdh

# Create the user
RUN groupadd --gid $USER_GID $USER_NAME 
RUN useradd --uid $USER_UID --gid $USER_GID -m $USER_NAME 

# Enables passwordless sudo
RUN apt-get install -y sudo
RUN echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME
RUN chmod 0440 /etc/sudoers.d/$USER_NAME

# Set the default user
USER $USER_NAME

# Install PDM as user $USER_NAME
RUN pip install --user pip setuptools wheel
RUN pip install pdm

#makes sure pdm and other pip installed binaries are added to the path
ENV PATH="${PATH}:/home/${USER_NAME}/.local/bin"

#set the work dir
WORKDIR /app


