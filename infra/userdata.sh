#!/bin/bash


apt update -y

#INSTALL DOCKER

apt-get install ca-certificates curl gnupg

install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update -y

apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# RUN APPLICATION

git clone https://github.com/nikolailevshakov/tournament_football.git /home/ubuntu/tournament_football
mkdir /home/ubuntu/db-data
apt install postgresql -y
docker build -t bot /home/ubuntu/tournament_football/bot
#docker run --name bot -p 80:5000 -e TOKEN=TOKEN -d bot
docker pull postgres
docker run --name postgres -e POSTGRES_PASSWORD=password \
  -v /home/ubuntu/db-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  -d postgres