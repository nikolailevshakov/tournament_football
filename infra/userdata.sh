#!/bin/bash


apt update -y
echo "${token}" > /home/ubuntu/token
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

git clone  https://oauth2:$(cat /home/ubuntu/token)@gitlab.com/sample9832632/bot.git
rm token
mkdir /home/ubuntu/db-data
#cd /home/ubuntu/tournament_football/bot
#docker compose up -d