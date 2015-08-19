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
This application uses a `Dockerfile` to setup a docker container for local development.
If you have Docker installed on your machine, please start the docker daemon, then do the following:
```
$ cd <clone-dir>
$ docker build -t iws_soultion .
$ docker run -t iws_solution -p 8000:8000 venv/bin/python manage.py runserver 0.0.0.0:8000
```
Then simply point your browser on your machine to `http://localhost:8000` and you will be able to see the application.

### Dockerfile explanation###
The Dockerfile does several things.  Since RHEL and CentOS come with python 2.6, the Dockerfile starts by downlaoding and building the Python 2.7.9 binary into `/usr/local/bin`.  It then creates a `virtual-environment` for the application, followed by installing `fixtues`.  Fixtures contain Client and Product Area model data.

###Unit Tests###
In `iws_project/iws_solution/tests.py` is a TestCase with a single unit test for ensuring that when saving a feature request the priorities are re-ordered correctly.

###Validation###
- Target Date in the future
- Client Priority always an Integer and greater than 0
- Tickker URL is a valid URL
- Required Fields

###Routes###
- home
- list
- list/client-id
- edit

The `home` route is the the `/` url and is where a user can save a feature request.  Once a feature request is successfuly saved, the response is redirected to `/list` with no additional args.  There the user is presented with a drop down list of `Clients`.  Once a client is chosen, the page is redirected to `/list/client-id`.

The boostrap table with feature requests has an edit in place feature.  Any cell can be clicked,  edited, and ajax saved which will update the DB column for that feature based on its primary key.

Target Dates and Ticekt URLs are validated.

###Static Assets###
Static Assets are hosted on Amaozon S3.  For clarity, then are also included in `project-root/static-assets`.
