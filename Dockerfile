#FROM python:3
FROM python:3.10-slim
#FROM python:3.10.0-alpine3.14
WORKDIR /usr/src/app
EXPOSE 5000
COPY requirements.txt requirements.txt
COPY . /usr/src/app
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
