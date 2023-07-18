FROM nginx:latest
ENV WEBPORT 8080
EXPOSE ${WEBPORT}
COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf