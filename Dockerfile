FROM python:buster as base
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | /usr/bin/python3 -

# For Production

FROM base as production

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

RUN mkdir /app
COPY poetry* /app
COPY pyproject.toml /app
WORKDIR /app
RUN ~/.local/bin/poetry install
ENV poetry=/root/.local/bin
ENV PATH=${poetry}:${PATH}
CMD poetry run flask run --host 0.0.0.0 --port 5100
EXPOSE 5100/tcp
