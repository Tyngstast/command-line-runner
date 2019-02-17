# Python Command Line Runner Service

RESTful Flask app for linux commands.

The service will expose a CRUD API for commands. Sqlite database for storage.

Live reloading during development works fine with both command line and docker execution.

Android app frontend: <https://github.com/TO_BE_DETERMINED>

## Run
### Command Line
1. Download and install pyenv: https://github.com/pyenv/pyenv#basic-github-checkout
2. Download and install pyenv-virtualenv: https://github.com/pyenv/pyenv-virtualenv#installation
3. pyenv install 3.5.3 (reason for 3.5.3 is raspberry pi compatability)
4. go to cloned directory
5. pyenv virtualenv 3.5.3 commandlinerunner
6. pyenv activate commandlinerunner
7. pip install -r requirements.txt
8. ./run.sh

### Docker
docker-compose up -d

## Techniques
* Flask
* Flask-RESTful
* SQLAlchemy
* subprocess

