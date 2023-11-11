from alpine
copy ./php-fpm /etc/init.d/
run chmod +x /etc/init.d/php-fpm
workdir /var/www/
run apk update && apk upgrade && apk add php php-fpm git nginx openrc php81-curl php81-session php81-json php81-dom php81-apcu php81-brotli
run rm /etc/nginx/nginx.conf
copy ./nginx.conf /etc/nginx/
run git clone https://git.bloatcat.tk/gospodin/translite.git
run rc-update add nginx && rc-update add php-fpm && rc-service nginx start && rc-service php-fpm start
