#!/bin/bash

# Update
sudo apt-get update
# Install GPIO lib
sudo pip3 install --upgrade RPi.GPIO
# Install Git
sudo apt install git
# Install Python3 from source
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
# Install Flask
sudo apt-get install python3-flask
# Install Flask CORS
pip install -U flask-cors