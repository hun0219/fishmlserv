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
$ docker build -t fishmlserv:0.4.0
$ docker run -d -p 8877:8765 --name fishmlserv2 fishmlserv:0.4.0
```

### fly.io
$ flyctl launch --name hun0219

### Ref
- https://curlconverter.com/python

### images
- https://hub.docker.com
