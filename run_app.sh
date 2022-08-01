#!/bin/sh -x
#. /opt/todoapp/.docker_trello_env
env
poetry run gunicorn --bind 0.0.0.0:5000 "todo_app.app:create_app()"
#poetry run flask run --host 0.0.0.0