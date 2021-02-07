FROM python:3

# env config
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=Europe/Brussels

# setup application dir
ENV APP_HOME=/app/web
RUN mkdir -p $APP_HOME/static_root
RUN mkdir -p $APP_HOME/media_root
RUN mkdir -p /var/log/web
RUN mkdir -p /root/.config/rclone
WORKDIR $APP_HOME

# install python dependencies
COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

# install other dependencies
RUN apt-get update && apt-get install -y \
    lsb-release \
    netcat \
    rclone \
    nano \
    wkhtmltopdf

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && apt-get install -y postgresql-client

# run entrypoint
ENTRYPOINT ["/app/web/docker_entrypoint.sh"]
