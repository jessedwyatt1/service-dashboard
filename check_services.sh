#!/bin/bash

HOST=192.168.0.220
USER=jwyatt
SSH_KEY=/root/.ssh/id_rsa

# Check CasaOS Main Service
if ssh -o StrictHostKeyChecking=no -i $SSH_KEY $USER@$HOST systemctl is-active --quiet casaos.service; then
    echo "CasaOS:active"
else
    echo "CasaOS:inactive"
fi

# Check Webmin
if ssh -o StrictHostKeyChecking=no -i $SSH_KEY $USER@$HOST systemctl is-active --quiet webmin.service; then
    echo "Webmin:active"
else
    echo "Webmin:inactive"
fi

# Check Transmission
if ssh -o StrictHostKeyChecking=no -i $SSH_KEY $USER@$HOST systemctl is-active --quiet transmission-daemon.service; then
    echo "Transmission:active"
else
    echo "Transmission:inactive"
fi

# Check ExpressVPN
if ssh -o StrictHostKeyChecking=no -i $SSH_KEY $USER@$HOST systemctl is-active --quiet openvpn@expressvpn.service; then
    echo "ExpressVPN:active"
else
    echo "ExpressVPN:inactive"
fi
