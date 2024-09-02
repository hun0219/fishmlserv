# fishmlserv

### Deploy
![deploy_image](https://github.com/user-attachments/assets/aa0556f8-1873-4adc-af03-69b0a1a69eb4)

###RUN
- dev
- http://localhost:8000/docs
```bash
uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```

- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949
```

### Docker
```bash
$ docker build -t fishmlserv:0.4.0 .
$ docker run -d -p 8877:8765 --name fishmlserv2 fishmlserv:0.4.0
$ docker ps 
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
f88123ed81dc   fishmlserv:0.7.1   "uvicorn main:app --…"   16 minutes ago   Up 16 minutes   0.0.0.0:7799->8080/tcp, :::7799->8080/tcp   fishml071

# docker 컨테이너 안으로...
$ docker exec -it fishml071 bash

# docker 컨테이너 안에서
root@f88123ed81dc:/code# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

# 다시 호스트OS(WSL)로 exit
root@f88123ed81dc: exit

# 로그 확인
$ sudo docker logs -f <CONTAINER ID|NAMES>
```

### fly.io
$ fly launch --no-deploy
$ flyctl launch --name hun0219
$ flyctl scale memory 256
$ flyctl deploy

### Ref
- https://curlconverter.com/python

### images
- https://hub.docker.com
