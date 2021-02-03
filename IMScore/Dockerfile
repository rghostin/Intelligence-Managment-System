FROM python:3

# python config
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


# create app user and group
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app

# setup application dir
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME/static_root
RUN mkdir -p $APP_HOME/media_root
WORKDIR $APP_HOME

# install dependencies
COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME
# RUN chown -R app:app $APP_HOME


# run entrypoint
RUN apt-get update && apt-get install -y netcat
# USER app:app
ENTRYPOINT ["/home/app/web/docker_entrypoint.sh"]