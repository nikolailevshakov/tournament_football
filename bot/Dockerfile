FROM python:3.7-alpine

RUN mkdir /bot
ADD . /bot
WORKDIR /bot
RUN pip3 install -r requirements.txt
EXPOSE 80
ENV TOKEN="TOKEN"

CMD ["python", "main.py"]