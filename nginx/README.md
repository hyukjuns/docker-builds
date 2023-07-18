- Attach Shell
```
# Shell 접근
# 실행할때
docker run -it hyukjun/nginx:test /bin/sh

# 실행중
docker exec -it <CONTAINER_ID> /bin/sh
```
- document root
```
/usr/share/nginx/html/index.html
```
- config
```
/etc/nginx/nginx.conf
/etc/nginx/conf.d/default.conf
```