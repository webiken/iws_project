# IWS Interview Solution by Sam Mohamed

## TechStack ##
- Python Web Framework Django (version 1.8).
- Bootstrap 3.0
- JQuery 2.0.3
- JQuery UI 1.11.2
- Bootstrap Editable Plugin
- SQLite
- Docker

##Running the App Locally##
This application uses a Dockerfile to setup a docker container for local development.
If you have Docker installed on your machine, please start the docker daemon, then do the following:
```
$ cd <clone-dir>
$ docker build -t iws_soultion .
$ docker run -t iws_solution -p 8000:8000 venv/bin/python manage.py runserver 0.0.0.0:8000
```
Then simply point your browser on your machine to http://localhost:8000 and you will be able to see the application.

### Dockerfile explanation###
The Dockerfile does several things.  Since RHEL and CentOS come with python 2.6, the Dockerfile starts by downlaoding and building the Python 2.7.9 binary into `/usr/local/bin`.  It then creates a `virtual-environment` for the application, followed by running `migrations` and launching the `development server`.



