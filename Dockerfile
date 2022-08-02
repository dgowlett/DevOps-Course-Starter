FROM python:buster as base

# For Production

FROM base as production

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | /usr/bin/python3 -
RUN mkdir -p /app/todo_app
COPY poetry* /app
COPY pyproject.toml /app
COPY todo_app /app/todo_app
WORKDIR /app
RUN ~/.local/bin/poetry install
ENV poetry=/root/.local/bin
ENV PATH=${poetry}:${PATH}
CMD poetry run gunicorn --bind 0.0.0.0:5000 "todo_app.app:create_app()"
EXPOSE 5000/tcp

# For Development

FROM base as development

RUN apt-get update && apt-get install -y curl 
RUN curl -sSL https://install.python-poetry.org | /usr/bin/python3 -
RUN mkdir /app
COPY poetry* /app
COPY pyproject.toml /app
WORKDIR /app
RUN ~/.local/bin/poetry install
ENV poetry=/root/.local/bin
ENV PATH=${poetry}:${PATH}
CMD poetry run flask run --host 0.0.0.0 --port 5100
EXPOSE 5100/tcp


# docker build --tag todo-app .
# docker run -d -p 5000:5000 --env-file .env --name todo-app-con todo-app
# docker ps
# docker exec -it todo-app-con bash
#
# Build for prod and dev
# docker build --target development --tag todo-app:dev .
# docker build --target production --tag todo-app:prod .
#
# To run the Development todo flask dev container Following on windows (the path) port 80 locally and mounts the host source code directory/folder in the container so that when
# changes are made to the source code the flask picks up those changes
# docker run --env-file ./.env -p 80:5100 -d --mount type=bind,source="${pwd}"\todo_app,target=/app/todo_app ---name todo-app_dev todo-app:dev
#
# To run the Production todo-app gunicorn container Following on windows (the path)
# docker run --env-file ./.env -p 5000:5000 -d --name todo-app_prod todo-app:prod
