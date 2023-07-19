- Attach Shell
```
# Shell 접근
# 실행할때
docker run -it <IMAGE_NAME> /bin/sh

# 실행중
docker exec -it <CONTAINER_ID> /bin/sh
```
- document root
```
/usr/share/nginx/html/index.html
```
- Config
```
/etc/nginx/nginx.conf
/etc/nginx/conf.d/default.conf
```
- Log
```
/var/log/nginx/access.log
/var/log/nginx/error.log
```