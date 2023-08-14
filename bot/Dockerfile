FROM python:3.7-alpine

WORKDIR /home/ubuntu/tournament_football/bot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD ["python", "main.py"]