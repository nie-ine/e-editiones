FROM nginx:1.15.8-alpine

RUN rm /etc/nginx/nginx.conf
RUN rm /etc/nginx/mime.types
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx_conf/nginx.conf /etc/nginx/
COPY nginx_conf/mime.types /etc/nginx/
COPY nginx_conf/default.conf /etc/nginx/conf.d/
COPY _site/ /usr/share/nginx/html/
