import struct, socket
import sys, subprocess

start_ip =  (10 << 24) + (10 << 16)

total = 1000
if (len(sys.argv) > 1):
    total = int(sys.argv[1])

for i in range(start_ip + 3, start_ip + total+3):
    ip_addr = socket.inet_ntoa(struct.pack('!L', i))
    mac_addr = ':'.join(s.encode('hex') for s in ("%012x" % i).decode('hex'))

    print ip_addr, mac_addr

    command = "/usr/local/sbin/arping -q -S " + str(ip_addr) + " -s " + str(mac_addr) + " " + str(ip_addr) + " -i eth0 -p -c 3 -w 100"
    subprocess.call(command, shell=True)
