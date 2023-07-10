# Simple Webpp
Client 와 Server의 HTTP Header를 출력 해주는 애플리케이션

## Local 실행 가이드
### 1. 가상환경 셋업
1. pyenv dependency 설치
```
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \\nlibbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \\nlibncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
2. pyenv 환경변수 설정
```
export PATH="/home/USERNAME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
3. 프로젝트용으로 사용할 python 버전 설치
```
pyenv install 3.8.9
```
4. 가상환경 셋업
```
# pyenv virtualenv <version> <가상환경이름>
pyenv virtualenv 3.8.9 myvirtualenv
```
5. 가상환경 설치 확인 (가상환경이름만 나오는것은 심볼릭 링크)
```
pyenv versions
```
6. 가상환경 적용
```
pyenv local myvirtualenv

# pyenv activate myvirtualenv
```
### 2. 실행

```
python app.py
```