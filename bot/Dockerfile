FROM python:3.7-alpine

RUN mkdir /bot
ADD . /bot
WORKDIR /bot
RUN pip3 install -r requirements.txt
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip3 wheel numpy pandas
EXPOSE 80

CMD ["python", "main.py"]