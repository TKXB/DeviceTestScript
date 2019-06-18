import RtspCheck
import PortScan
import SerialCheck
import External
import argparse

def main():
    parser = argparse.ArgumentParser(description='EZVIZ device security test toolkit')
    parser.add_argument('ip', metavar='target_host',
                        type=str,
                        help='Device\'s ip address')
    parser.add_argument('--port', metavar='target_port',
                        type=str,
                        help='Port number of device under test')
    parser.add_argument('--testwifi', metavar='yes|no',
                        type=str2bool,
                        help='WIFI security test')
    args = parser.parse_args()

    if args.testwifi is True:
        wificheck = External.WifiCheck("/root/Downloads/SecurityVulnerabilityDetectionTool_v1.3/vdt-v1.3/vdt_wts/")
        wificheck.run()
        exit()

    se = SerialCheck.SerialCheck('/dev/ttyUSB0')
    se.PshCheck()
    se.keysearch()
    se.close()

    np = PortScan.Portscan(args.ip, args.port)
    np.run()
    np.getAllPort()

    r = np.isRtspOpen()
    if r:
        rt = RtspCheck.EmptyRtspPasswordCheck(args.ip)
        rt.run()


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__":
    main()


