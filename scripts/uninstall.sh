#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

sudo rm /usr/local/bin/image-converter.py
echo "image-converter.py successfully removed"