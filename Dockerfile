#FROM python:3.7.13-alpine3.16
#FROM python:buster
FROM python:3.10.2
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN curl -sSL https://install.python-poetry.org | /usr/bin/python3 -
RUN mkdir -p /opt/todoapp/todo_app
COPY todo_app /opt/todoapp/todo_app
COPY .docker_trello_env /opt/todoapp
COPY .env* /opt/todoapp
COPY poetry* /opt/todoapp
COPY pyproject.toml /opt/todoapp
COPY run_app.sh /opt/todoapp
WORKDIR /opt/todoapp
#RUN rm poetry.lock
RUN ~/.local/bin/poetry install
RUN chmod +x run_app.sh
ENV poetry=/root/.local/bin
ENV PATH=${poetry}:${PATH}
ENV trello_api_key=a66c8d5cc04af740d93eb1df0a8b8f8e
ENV trello_api_token=2c29ba4d64531f68d6a186d3a1d984fab851faf1d775d439257f1e0070095e62
ENV trello_board_id=iKG204fx
ENV TRELLO_API_KEY=${trello_api_key}
ENV TRELLO_API_TOKEN=${trello_api_token}
ENV TRELLO_BOARD_ID=${trello_board_id}
ENTRYPOINT ["./run_app.sh"]
EXPOSE 5000/tcp
EXPOSE 8000/tcp


# poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"