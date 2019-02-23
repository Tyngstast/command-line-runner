#!/bin/bash

DIR=$(dirname "$0")

if [ -z "$VIRTUAL_ENV" ]; then
    VENV=$DIR/venv/bin/activate
    if [ ! -f "$VENV" ]; then
        VENV=$HOME/.pyenv/versions/3.5.3/envs/commandlinerunner/bin/activate
    fi
    echo "VIRTUAL_ENV not activated, activating..."
    source $VENV 
fi

export PYTHONPATH=$PYTHONPATH:$DIR/

export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000

flask run
