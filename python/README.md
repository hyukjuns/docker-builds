# Python api server
### Usage
1. DB 정보 환경변수 설정
2. 앱실행
    - 개발환경: Debug 모드
    - 운영환경: gunicorn 사용


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