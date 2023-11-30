FROM mysql:8.2.0

# DB Setup 1: Create Database, User/PW
ENV MYSQL_ROOT_PASSWORD=rootpass
ENV MYSQL_DATABASE=playerdb
ENV MYSQL_USER=dbuser
ENV MYSQL_PASSWORD=dbpass

# DB Setup 2: Add to entrypoint
ADD scheme.sql /docker-entrypoint-initdb.d

EXPOSE 3306