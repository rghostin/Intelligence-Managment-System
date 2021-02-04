FROM nginx:mainline-alpine

ENV TZ=Europe/Brussels

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

RUN apk add certbot certbot-nginx
RUN mkdir /etc/letsencrypt
