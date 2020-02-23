import socket
import os
import sys
from orca.messages import percentage

class Scanner:
    def __init__(self, PORTRANGE=100, IPFORMAT="192.168.0.XXX", STARTHOST=0):
        self.PORTRANGE = PORTRANGE
        self.sock = socket.socket()
        self.IPFORMAT = IPFORMAT
        self.STARTHOST = STARTHOST
        self.aboveLineLength = 0
        self.hostDict = dict()
    
    def scan(self):
        global ip
        print("Start scanning...")
        print("Scanning progress:")
        for i in range(self.STARTHOST, self.PORTRANGE):
            #status = "Scanning: "
            ip = self._parseIPFormat(i)
            self.progress("Scanning", i, self.STARTHOST+self.PORTRANGE, 50, 20)
            print(ip, sep='', end='\b'*(len(ip)+self.aboveLineLength), flush=True)
            #os.system('clear')
            res = True if os.system('ping -c 1 ' + ip + ' >/dev/null') is 0 else False
            if(res):
                self.hostDict[ip] = 'alive'
            else:
                self.hostDict[ip] = 'down'
        print("\n")
        print("Done...")
            
    def _parseIPFormat(self, IPPOST):
        if('XXX' in self.IPFORMAT):
            return self.IPFORMAT.replace('XXX', str(IPPOST))
        else:
            raise Exception("Ip Format Error!")
        
    def printRES(self):
        print("Stats:")
        for i in self.hostDict:
            print(">>> HOST " + i + " " + "STATUS: "+self.hostDict.get(i))
        print()
    
    def progress(self, name, start, end, tokens = 50, width = 20):
        percentage = float(start)/end
        arrow = "-"*int(round(percentage*tokens)-1)+">"
        spaces = ' '*(tokens-len(arrow))
        sys.stdout.write("\r{0: <{1}} : [{2}]{3}%\n".format(name, width, arrow + spaces, int(round(percentage*100))))
        self.aboveLineLength = len("\r{0: <{1}} : [{2}]{3}%\n".format(name, width, arrow + spaces, int(round(percentage*100))))
        sys.stdout.flush()
        if start == end:
            sys.stdout.write('\n\n')
        
            
            
if __name__ == '__main__':
    sc = Scanner(20, '192.168.0.XXX', 0)
    sc.scan()
    sc.printRES()