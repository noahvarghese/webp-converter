#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Just in case, never know when I'll forget in a future project to run this at setup
sudo chmod a+x ./src/main.py