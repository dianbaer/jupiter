#!/bin/sh
nohup python3 /home/firstaio-example/main.py &
echo $! > /home/firstaio-example/firstaioexample.pid
