# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. This project uses the official distribution of Python version 3.7+ the installation instrution below however will install these for you
(as found in the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

The project uses docker container technology to stand up a development and production environments, therefore you will need to install docker desktop first for your host OS [docker installion](https://docs.docker.com/engine/install) ; note docker desktop for windows may require a paid subscription to use, please check the latest documentation - as of today 2nd August 2022 it is okay to use subscription free for educational purposes.

## Dependencies

This App uses the Trello site to store the Card and list information that the App uses, therefore the following variables will need to be provided after creating a trello account from https://trello.com and creation of a new Board followed by generation of a required api key and token from https://trello.com/1/appKey/generate, these will be requested when installing the App in the next section

TRELLO_API_KEY
TRELLO_API_TOKEN
TRELLO_BOARD_ID

First make a copy of the .env.template file to the .env file and then fill in the TRELLO environment variables obtained when you created you trello account 

## Development

If any changes are made to the code base, then the following can be used to run tests which can be found and defined in the files under the tests directory.

After any changes, care must be taken to ensure that poetry / flask works as expected run from a terminal.

> poetry run flask run

## To run all Unit and Intergration Tests run the following

poetry run pytest tests

## Unit tests only

The individual tests can be performed in the following way

poetry run pytest --setup-only todo_app/tests

Followed by the individual tests picked out from running pytest --setup-only above

poetry run pytest todo_app/tests/test_view_model.py::test_done_items_property_only_returns_the_done_items

poetry run pytest todo_app/tests/test_view_model.py::test_todo_items_property_only_returns_the_todo_items

Run all the Unit tests

poetry run pytest todo_app/tests/test_view_model.py

## Intergration tests only

To run the Intergration tests run the following:

poetry run pytest todo_app/tests/test_client.py

## To run End 2 End tests

To run the end to end test run the following

poetry run pytest todo_app/tests_e2e/test_client_e2e.py


## To run the all Unit and Intergration Tests under Docker

docker build --target test --tag my-test-image .

docker run my-test-image todo_app/tests

## To run the End 2 End tests under Docker

This will require the live TRELLO API KEY and TOKEN but note that this test will create a new temporary board to perform the End to End Tests.

Using the TRELLO Variable set in the .env file set and pass the env valiable to docker, example for the bash shell:

export TRELLO_KEY=lkjh66dfgohe66rgoheorgh
export TRELLO_TOKEN=ijhu999gtfreyeyikd8888jdjsdpsfjpwffwevjffejd1

docker run -e TRELLO_API_KEY="$TRELLO_KEY" -e TRELLO_API_TOKEN="$TRELLO_TOKEN" my-test-image todo_app/tests_e2e

## Installing and running the App

## Building and running the DEVELOPMENT docker container

First build the docker image for development

docker build --target development --tag todo-app:dev .

To run the Development todo flask dev container Following on windows (the path) port 80 locally and mounts the host source code directory/folder in the container so that when
changes are made to the source code the flask picks up those changes

docker run --env-file ./.env -p 5100:5100 -d --mount type=bind,source="${pwd}"\todo_app,target=/app/todo_app --name todo-app_dev todo-app:dev

Now you can not only navigate using a browser to http://127.0.0.1 , you can also make changes to the source code and they will be refelected by flasks reloading of the application files with in the running development docker container

## Controlling the development container

To Stop the development container.

docker stop todo-app_dev

To Start the development container again.

docker start todo-app_dev

To remove the development container i.e. If you wish to perform a docker run again using the same ports/name etc

docker rm todo-app_dev

## Building and running the PRODUCTION docker container 

First build the production docker image

docker build --target production --tag todo-app:prod .

To run the Production todo-app gunicorn container Following on windows (the path)

docker run --env-file ./.env -p 80:5000 -d --name todo-app_prod todo-app:prod

Now you should be able to navigate using a browser to http://127.0.0.1 or the public IP address

## Controlling the production container

To Stop the production container.

docker stop todo-app_prod

To Start the production container again.

docker start todo-app_prod

To remove the production container i.e. If you wish to perform a docker run again using the same ports/name etc

docker rm todo-app_prod

