#!/usr/bin/env bash


apt-get install -y git python3.8 python3 python3-pip python3-dev

git init
git remote add origin https://github.com/Berkeley-CS170/proj-2022sp-input-autograder.git
git pull origin master

python3.8 -m pip install -r /autograder/source/requirements.txt
