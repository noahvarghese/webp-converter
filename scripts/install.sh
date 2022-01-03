#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

sudo cp ./src/main.py /usr/local/bin/image-converter.py