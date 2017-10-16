chmod +x /home/faster-http-test/startservice.sh
cp /home/faster-http-test/fasterhttptest.service /usr/lib/systemd/system
systemctl enable fasterhttptest
systemctl start fasterhttptest
