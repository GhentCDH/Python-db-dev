# Containerized database development with Python

This repository shows a dockerized Python script interacting with a Postgres database - using the SQLAlchemy library to ease db interaction. A docker compose script is used to spin up a database server and a development environment.

There are a few advantages of using containers like Docker, even during development: it makes setting a development reproducable, transferable and makes dependencies and assumptions on which system the script is running. It also makes you think about configuration and responsibilities of systems.

Another advantage is that it keeps a development machine clean: only docker needs to be installed. To interact with a postgres database, for example, there is no need to install - and configure - a postgres server on the development machine.

A disadvantage is that a bit of configuration is needed. This repository can help in this regard. 



`SQLAlchemy` is used as an ORM and the database is accessed via a connection string which looks similar to:

`postgresql://exampleuser:examplepass@database/test`

To allow VS Code to access debugging the python plugin needs to be available *in the container*. So first start the `Attach to running container` and then in VS Code install the plugin in the container. The video below shows a way to do it.

https://github.com/GhentCDH/Python-db-dev/assets/60453/a2b26004-ec0a-4b5e-92ec-740e5d07b910

In the video above Visual Studio Code is used to start two containers. A container with a postgres database server and a container with a python development environment. A IDE session is attached to the running python container and running code and debugging is done in the container itself.




## Format code

To format using ruff, execute

```sh
pdm run ruff format src
```


## Credits

The GhentCDH development team: Pieterjan Depotter, Frederic Lamsens, Joren Six

