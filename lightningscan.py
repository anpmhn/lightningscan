#!/usr/bin/env python

import sys
import socket
import threading
import time
usage= "Usage: python lightningscan.py [ip address]"


if len(sys.argv) <= 1:
    print usage
    exit()

ip = sys.argv[1]
print "\n"
print "Checking open ports in %s" % ip
print "---------------------------------"
def test_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((str(ip), int(port)))
        s.close
        screenLock.acquire()
        print port
	screenLock.release()
        return True
    except:
        return False


def start_thread(ip, port):
    t = threading.Thread(target=test_port, args=(ip, port))
    t.start()
screenLock = threading.Semaphore(value=1)

for port in range(0,65535):
    start_thread(ip, port)
# Uncomment the below line to add 5 Second delay after each port check
#    time.sleep(5)

