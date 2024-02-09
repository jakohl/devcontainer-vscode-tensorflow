#! /bin/bash

ls -la /mnt/.ssh 

mkdir -p ~/.ssh

cp -fu /mnt/.ssh/id_ed25519 ~/.ssh/ 
cp -fu /mnt/.ssh/id_ed25519.pub ~/.ssh/ 

chmod 600 ~/.ssh/id_ed25519

chmod 644 ~/.ssh/id_ed25519.pub

ls -la ~/.ssh 