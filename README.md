# Download Script #
wget https://raw.githubusercontent.com/THGLouis/PatroniHAProxyStatus/main/patronistatus.py

mv patronistatus.py /usr/local/bin/patroni-check

chmod +x /usr/local/bin/patroni-check

# Create service file #

wget https://raw.githubusercontent.com/THGLouis/PatroniHAProxyStatus/main/etc/systemd/system/patronistatus.service

mv patronistatus.service /etc/systemd/system/patroni-check.service

systemctl daemon-reload

systemctl enable --now patroni-check
