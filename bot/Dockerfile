FROM python:3.7-alpine

RUN mkdir /bot
ADD . /bot
WORKDIR /bot
RUN pip3 install -r requirements.txt
RUN pip wheel numpy pandas
EXPOSE 80

CMD ["python", "main.py"]