import RtspCheck
import PortScan
import SerialCheck
from optparse import OptionParser

def main():
    usage = "usage: %prog [options] -d ip -p port"
    parser = OptionParser(usage)
    parser.add_option("-d", "--ip", dest="ip")
    parser.add_option("-p", "--port", dest="port")
    (options, args) = parser.parse_args()
    ip = options.ip
    if ip == None:
        parser.print_usage()
        exit()
    port = options.port

    se = SerialCheck.SerialCheck('/dev/ttyUSB0')
    se.PshCheck()
    se.keysearch()
    se.close()

    np = PortScan.Portscan(ip, port)
    np.run()
    np.getAllPort()

    r = np.isRtspOpen()
    if r:
        rt = RtspCheck.EmptyRtspPasswordCheck(ip)
        rt.run()

if __name__ == "__main__":
    main()