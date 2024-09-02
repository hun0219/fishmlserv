#  컨테이너 만들때 3.11버전으로 만듦
#FROM python:3.11
#FROM python:3.11.9-slim-bullseye
#FROM python:3.11.9-slim
FROM python:3.11-alpine3.20

# 컨테이너 루트밑에 code 만듦
WORKDIR /code

# 지금 로컬의 모든 걸 컨테이너 code 디렉토리 밑에 복사
#COPY . /code/
COPY src/fishmlserv/main.py /code/
# pip /code/requirment.txt 설치 하기 위해 /code/에 복사
COPY requirements.txt /code/

# 
#COPY ./requirements.txt /code/requirements.txt

# 컨테이너가 실행될때 requirements.txt안에꺼 설치 / .toml디펜던시 설정넣은거(.toml에 있음)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#RUN pip install git+https://

# 서버실행시 커맨드 실행 ","가 띄워쓰기임
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
# 포트를 내부적으로 열어준다 8765
