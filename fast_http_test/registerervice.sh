chmod +x /home/fast_http_test/startservice.sh
cp /home/fast_http_test/fasthttptest.service /usr/lib/systemd/system
systemctl enable fasthttptest
systemctl start fasthttptest
