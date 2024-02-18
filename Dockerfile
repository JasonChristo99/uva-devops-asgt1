FROM python:3.8-alpine

# print mongodb version
#CMD ["mongod", "--version"]

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

# RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]