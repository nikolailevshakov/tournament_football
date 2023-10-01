FROM python:3.7-alpine

RUN mkdir /bot
ADD . /bot
WORKDIR /bot
RUN apk update
RUN pip3 install -r requirements.txt
EXPOSE 80

CMD ["python", "main.py"]