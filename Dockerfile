FROM alpine
WORKDIR /var/www/
RUN apk update && apk upgrade && apk add php php-fpm git nginx openrc php81-curl php81-session php81-json php81-dom php81-apcu php81-brotli
RUN rm /etc/nginx/nginx.conf
RUN rm /etc/php81/php-fpm.d/www.conf
COPY ./config/nginx.conf /etc/nginx/
COPY ./config/www.conf /etc/php81/php-fpm.d/
RUN git clone https://git.bloatcat.tk/gospodin/translite.git
EXPOSE 80
ENTRYPOINT ["/bin/sh", "-c", "/usr/sbin/php-fpm81 -D && /usr/sbin/nginx -c /etc/nginx/nginx.conf -g 'daemon off;'"]

