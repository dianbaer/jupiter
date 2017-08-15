chmod +x /home/firstaio-example/startservice.sh
cp /home/firstaio-example/firstaioexample.service /usr/lib/systemd/system
systemctl enable firstaioexample
systemctl start firstaioexample
