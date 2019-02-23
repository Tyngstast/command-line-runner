#!/bin/bash

DIR=$(dirname "$0")
PYTHON_VERSION=3.5.3

if [ -z "$CLR_API_KEY" ]; then
    export CLR_API_KEY=secret
fi

if [[ -z "$VIRTUAL_ENV" && ! "$RUNNING_IN_DOCKER" ]]; then
    VENV=$DIR/venv
    if [ ! -d "$VENV" ]; then
        VENV=$HOME/.pyenv/versions/$PYTHON_VERSION/envs/commandlinerunner
    fi
    if [ ! -d "$VENV" ]; then
        echo "virtual environment not found, exiting..." 
        exit 0
    fi
    echo "VIRTUAL_ENV not activated, activating..."
    source $VENV/bin/activate 
fi

export PYTHONPATH=$PYTHONPATH:$DIR/

export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000

echo "Starting flask app..."

flask run
