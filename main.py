import RtspCheck
import PortScan
import SerialCheck
import External
from optparse import OptionParser


def main():
    usage = "usage: %prog [options] -d ip -p port"
    parser = OptionParser(usage)
    parser.add_option("-d", "--ip", dest="ip")
    parser.add_option("-p", "--port", dest="port")
    parser.add_option("-c", "--wifi", dest="cwifi")
    (options, args) = parser.parse_args()
    ip = options.ip
    if ip is None:
        parser.print_usage()
        exit()
    port = options.port
    cwifi = options.cwifi

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

    if cwifi is not None:
        wificheck = External.WifiCheck("/root/Downloads/SecurityVulnerabilityDetectionTool_v1.3/vdt-v1.3/vdt_wts/")
        wificheck.run()


if __name__ == "__main__":
    main()

