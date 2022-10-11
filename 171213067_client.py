import socket
import time


Port = 12345
file = open("targethosts.txt")



for satir in file:
    ip=file.readline()
    try:
        RTTs=time.ctime()
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(msg, (ping, 12345)) 
        send_time_ms = time.time()
        s.settimeout(1)
        data addr = s.recvfrom(1024)
        RTTf=time.ctime()

        print("UDP : %s", ip)
        print("RTT : %s", RTTf-RTTs)
        print("HEDEF : %s", ip)

        file.close()

 except s.gettimeout():
        print "paket kaybı"
        continue