FROM python:3.7-alpine

RUN mkdir /bot
ADD . /bot
WORKDIR /bot
RUN pip3 install -r requirements.txt
RUN chmod +x ./scripts/start.sh
EXPOSE 80

CMD ["sh", "-c","./scripts/start.sh"]