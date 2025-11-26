# Containerized database development with Python

This repository shows a dockerized Python script interacting with a Postgres database - using the SQLAlchemy library to ease db interaction. A docker compose script is used to spin up a database server and a development environment.

There are a few advantages of using containers like Docker, even during development: it makes setting a development reproducable, transferable and makes dependencies and assumptions on which system the script is running. It also makes you think about configuration and responsibilities of systems.

Another advantage is that it keeps a development machine clean: only docker needs to be installed. To interact with a postgres database, for example, there is no need to install - and configure - a postgres server on the development machine.

A disadvantage is that a bit of configuration is needed. This repository can help in this regard. 


## Getting started

To get started, clone and 'compose' the images. The `docker compse` command needs an `.env` file so this is linked to the configuration example. If this runs succesfuly, the IDE can be connected to the container for development.

`````sh
git clone git@github.com:GhentCDH/Python-db-dev.git
cd Python-db-dev
ln -s env.example .env
docker compose -f compose.dev.yaml up
`````

In the video below Visual Studio Code is used to (re)start two containers. A container with a PostgreSQL database server and a container with a Python development environment. A IDE session is attached to the running Python container, executing code and debugging is done in the container itself. To allow VS Code to access debugging the Visual Studio Code Python plugin needs to be available *in the container*. So first start the `Attach to running container` and then in VS Code install the Python plugin in the container. 


https://github.com/GhentCDH/Python-db-dev/assets/60453/a2b26004-ec0a-4b5e-92ec-740e5d07b910



## Background info on the Python environment

The Python environment is managed by PDM, a python dependency manager. The script connects via `SQLAlchemy` - an ORM  - to the database which is accessed via a connection string which is configured via the `.env` and looks like `postgresql://exampleuser:examplepass@database/test`.

To format Python code via the ruff formatter, execute `pdm run ruff format src`. Ruff is also added as a pdm dependency. 

The python image is based of the standard Python docker image but adds a couple of extra packages to interact with the database and installs the pdm manager.

## Credits

The GhentCDH development team: Pieterjan Depotter, Frederic Lamsens, Joren Six

Development by [Ghent Centre for Digital Humanities - Ghent University](https://www.ghentcdh.ugent.be/). Funded by the [GhentCDH research projects](https://www.ghentcdh.ugent.be/projects).

<img src="https://www.ghentcdh.ugent.be/ghentcdh_logo_blue_text_transparent_bg_landscape.svg" alt="Landscape" width="500">
