chmod +x /home/jupiter_http_test/startservice.sh
cp /home/jupiter_http_test/jupiterhttptest.service /usr/lib/systemd/system
systemctl enable jupiterhttptest
systemctl start jupiterhttptest
