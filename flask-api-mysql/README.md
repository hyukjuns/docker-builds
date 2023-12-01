# Python api server
### dockercompose
```
# up and build
docker compose up -d --build
```
- [networking in compose](https://docs.docker.com/compose/networking/)

### Dev: docker-compose.yml
- Dockerfile-dev
    - db.env: sql 접속 정보
    - service:
        - app: flask api
        - db: mysql

### Prod: Dockerfile
- Dockerfile
    - sql 접속정보: 환경변수로 입력 필요

### mysql
- db scheme 초기 세팅 -> scheme.sql

### Usage
1. DB 정보 환경변수 설정
```
export MYSQL_DATABASE_USER=userid
export MYSQL_DATABASE_PASSWORD=userpass
export MYSQL_DATABASE_DB=dbname
export MYSQL_DATABASE_HOST=dbhost
```
2. 앱실행
    - 개발환경: Debug 모드
    - 운영환경: gunicorn 사용

### ETC
- get env from os
```
import os
print(os.environ['HOME'])

# Returns `None` if the key doesn't exist
print(os.environ.get('KEY_THAT_MIGHT_EXIST'))

# Returns `default_value` if the key doesn't exist
print(os.environ.get('KEY_THAT_MIGHT_EXIST', default_value))

# Returns `default_value` if the key doesn't exist
print(os.getenv('KEY_THAT_MIGHT_EXIST', default_value))
```

- flask request
```
# query parameter
request.args.get('parameter')

# data from raw data

# data from form data
request.form.get('value')
```

- gunicron
```
# start server
gunicorn --config gunicorn_config.py app:app
```