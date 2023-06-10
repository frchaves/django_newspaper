# Overloop Django Tech Test Backend

## Running with Docker

- A sample Dockerfile and a docker-compose is provided to run the application in an isolated environment
- Make sure you have `docker` and `docker-compose` installed and that the Docker daemon is running
- Build and run the container: `docker-compose up`
- Start making some requests: `curl http://localhost:8000/articles/`
- Test the app with `python manage.py test techtest.regions techtest.articles techtest.author`

## Running with a virtual environment

- To run the application in a virtual Python environment, follow these instructions. This example will create a virtual Python environment for 3.9.6
- Check you have the pyenv version you need: `pyenv versions`
- You should see 3.9.6
- If you do not have the correct version of Python, install it like this: `pyenv install 3.9.6`
- On command line do this: `~/.pyenv/versions/3.9.6/bin/python -m venv env`
- This creates a folder called env. Then do this to activate the virtual environment: `source env/bin/activate`
- Lastly do this to check that you are now on the correct Python version: `python --version`
- You can install the dependencies with `pip install -r requirements.txt`
- You should run `python setup_and_seed.py` to get a local database setup and seeded with lookup data
- You can then run the app with `python manage.py runserver 0.0.0.0:8000` in the root directory

## Project Structure Notes

- There are three django apps installed `articles`, `regions` and `author` 
- Django is used as a RESTful API, no html rendering is required
- Marshmallow is used to serialize and deserialize django object instances
