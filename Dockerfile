#FROM python:buster as base
FROM python:3.10-slim-buster as base
RUN apt-get update && apt-get install -y curl
RUN which python3
RUN curl -sSL https://install.python-poetry.org | /usr/local/bin/python3 -
WORKDIR /app 
COPY poetry* /app/
COPY pyproject.toml /app
COPY todo_app ./todo_app
RUN ~/.local/bin/poetry install
ENV poetry=/root/.local/bin
ENV PATH=${poetry}:${PATH}


# For Production

FROM base as production
CMD poetry run gunicorn --bind 0.0.0.0:5000 "todo_app.app:create_app()"
EXPOSE 5000/tcp

# For Development

FROM base as development
CMD poetry run flask run --host 0.0.0.0 --port 5100
EXPOSE 5100/tcp

# Testing stage

FROM base as test
COPY .env.test .
RUN apt-get install -y --no-install-recommends firefox-esr
ENV MOZ_HEADLESS=1
#ENTRYPOINT ["poetry", "run", "pytest"]
EXPOSE 5100/tcp
