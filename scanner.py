import socket
import os

class Scanner:
    def __init__(self, PORTRANGE=100, IPFORMAT="192.168.0.XXX", STARTHOST=0):
        self.PORTRANGE = PORTRANGE
        self.sock = socket.socket()
        self.IPFORMAT = IPFORMAT
        self.STARTHOST = STARTHOST
        self.hostDict = dict()
    
    def scan(self):
        global ip
        for i in range(self.STARTHOST, self.PORTRANGE):
            ip = self._parseIPFormat(i)
            print(ip)
            #os.system('clear')
            res = True if os.system('ping -c 1 ' + ip + ' >/dev/null') is 0 else False
            if(res):
                self.hostDict[ip] = 'alive'
            else:
                self.hostDict[ip] = 'down'
            
    def _parseIPFormat(self, IPPOST):
        if('XXX' in self.IPFORMAT):
            return self.IPFORMAT.replace('XXX', str(IPPOST))
        else:
            raise Exception("Ip Format Error!")
        
    def printRES(self):
        for i in self.hostDict:
            print(">>> HOST " + i + " " + "STATUS: "+self.hostDict.get(i))
        print()
        
            
            
if __name__ == '__main__':
    sc = Scanner(19, '192.168.0.XXX', 0)
    sc.scan()
    sc.printRES()