from alpine
workdir /var/www/
run apk update && apk upgrade && apk add php php-fpm git nginx openrc php81-curl php81-session php81-json php81-dom php81-apcu php81-brotli
run rm /etc/nginx/nginx.conf
run rm /etc/php81/php-fpm.d/www.conf
copy ./config/nginx.conf /etc/nginx/
copy ./config/www.conf /etc/php81/php-fpm.d/
run git clone https://git.bloatcat.tk/gospodin/translite.git
expose 80
cmd rc-update add nginx && rc-update add php-fpm81 && rc-service nginx start && rc-service php-fpm81 start
