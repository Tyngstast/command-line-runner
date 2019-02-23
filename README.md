# Python Command Line Runner Service

**Disclaimer: Use with caution and only use on closed access personal network. You could basically destroy you computer with two REST calls...**

RESTful Flask app for CRUD operations and execution of linux commands using subprocess lib.

The service exposes an API for commands and tags. Relevant POST and DELETE endpoints protected by API\_KEY decorator. API\_KEY will be set to env variable CLR\_API\_KEY or 'secret' if none is set.

Android app frontend: <https://github.com/Tyngstast/TO_BE_DETERMINED>

## Run
### Local Command Line
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
* marshmallow
* subprocess
* Docker

