#!/bin/bash

echo "Setting up necessary files..."
docker-compose up -d

DOMAIN=lulumagic.com

if ! grep -q "$DOMAIN" /etc/hosts; then
    echo "Please enter computer password to add lulu's magic site to /etc/hosts..."
    echo "127.0.0.1 ::1 $DOMAIN" | sudo tee -a /etc/hosts
    echo "You're good to go! Visit lulumagic.com for some tricks!"
fi

