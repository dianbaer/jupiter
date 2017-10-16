#!/bin/sh
nohup python3 /home/fast_http_test/AioInit.py &
echo $! > /home/fast_http_test/fasthttptest.pid
