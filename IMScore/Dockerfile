FROM python:3

# env config
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=Europe/Brussels

# create app user and group
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app

# setup application dir
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME/static_root
RUN mkdir -p $APP_HOME/media_root
RUN mkdir -p /var/log/web && chown app:app /var/log/web
WORKDIR $APP_HOME

# install python dependencies
COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME
RUN chown -R app:app $APP_HOME

# install other dependencies
RUN apt-get update && apt-get install -y \
    lsb-release \
    netcat \
    rclone

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && apt-get install -y postgresql-client

# run entrypoint
USER app:app
ENTRYPOINT ["/home/app/web/docker_entrypoint.sh"]