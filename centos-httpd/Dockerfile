FROM centos:7
RUN yum -y install httpd
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
WORKDIR /var/www/html
VOLUME /var/www/html
ENV WEBPORT 80
EXPOSE ${WEBPORT}
COPY index.html /var/www/html/