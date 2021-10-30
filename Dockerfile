FROM python:3.6
WORKDIR /usr/src/app
RUN apt-get -y update
EXPOSE 5000
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
