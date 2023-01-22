#!/bin/bash

echo "Downloading .zip"
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1hhHzQUQvp7WG7UcVIjfLeIEPcMZjflx7" -O exp.zip && rm -rf /tmp/cookies.txt
echo "Unpacking zip"
unzip exp.zip
echo "Removing .zip"
rm exp.zip


