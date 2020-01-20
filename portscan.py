import nmap

class Portscan(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        self.nm = nmap.PortScanner()
        if self.port != "":
            self.nm.scan(self.ip, self.port)
        else:
            self.nm.scan(self.ip)

    def isRtspOpen(self):
        if 554 in self.nm[self.ip]['tcp']:
            if self.nm[self.ip]['tcp'][554]['state'] == 'open':
                print("RTSP/554 port is open")
                return True
        else:
            print("RTSP/554 port is not open")
            return False

    def isHttpOpen(self):
        if 80 in self.nm[self.ip]['tcp']:
            if self.nm[self.ip]['tcp'][80]['state'] == 'open':
                print("HTTP/80 port is open")
                return True
        else:
            print("HTTP/80 port is not open")
            return False

    def getAllPort(self, device):
        for host in self.nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, self.nm[host].hostname()))
            device.hostname = self.nm[host].hostname()
            print('State : %s' % self.nm[host].state())

            for proto in self.nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                lport = self.nm[host][proto].keys()
                lport = sorted(lport)
                for port in lport:
                    device.PortList.append(port)
                    print('port : %s\tstate : %s' % (port, self.nm[host][proto][port]['state']))
                    print('\n')


