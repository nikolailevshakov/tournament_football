FROM python:3.7-alpine

RUN mkdir /bot
ADD . /bot
WORKDIR /bot
RUN pip install -r requirements.txt
EXPOSE 5000
ENV TOKEN="TOKEN"

CMD ["python", "main.py"]