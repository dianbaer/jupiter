#!/bin/sh
nohup python3 /home/faster-http-test/AioInit.py &
echo $! > /home/faster-http-test/fasterhttptest.pid
