#!/bin/bash


sudo apt install git

sudo su
cd /usr/src
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar -xf Python-3.7.0.tgz
apt-get update
apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
cd Python-3.7.0
./configure --enable-optimizations
make altinstall
ln -s /usr/local/bin/python3.7 /usr/local/bin/python3
python3 --version
rm -Rf Python-3.7.0
rm Python-3.7.0.tgz
exit

sudo apt-get install python3-flask
pip install -U flask-cors
sudo pip3 install --upgrade RPi.GPIO

