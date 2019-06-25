import RtspCheck
import PortScan
import SerialCheck
import External
import argparse

def print_title():
    print("""
    
 /$$$$$$$$                      /$$                 /$$$$$$$$                    /$$           /$$$$$$$$                  /$$
| $$_____/                     |__/                |__  $$__/                   | $$          |__  $$__/                 | $$
| $$       /$$$$$$$$ /$$    /$$ /$$ /$$$$$$$$         | $$  /$$$$$$   /$$$$$$$ /$$$$$$           | $$  /$$$$$$   /$$$$$$ | $$
| $$$$$   |____ /$$/|  $$  /$$/| $$|____ /$$/         | $$ /$$__  $$ /$$_____/|_  $$_/           | $$ /$$__  $$ /$$__  $$| $$
| $$__/      /$$$$/  \  $$/$$/ | $$   /$$$$/          | $$| $$$$$$$$|  $$$$$$   | $$             | $$| $$  \ $$| $$  \ $$| $$
| $$        /$$__/    \  $$$/  | $$  /$$__/           | $$| $$_____/ \____  $$  | $$ /$$         | $$| $$  | $$| $$  | $$| $$
| $$$$$$$$ /$$$$$$$$   \  $/   | $$ /$$$$$$$$         | $$|  $$$$$$$ /$$$$$$$/  |  $$$$/         | $$|  $$$$$$/|  $$$$$$/| $$
|________/|________/    \_/    |__/|________/         |__/ \_______/|_______/    \___/           |__/ \______/  \______/ |__/
                                                                                                                             
                                                                                                                             
    """)


def print_menu():
    print("""
    -------------- EZVIZ TEST TOOL OPTIONS -------------
    0 - Print this menu
    1 - SerialCheck
    2 - PortScan 
    3 - WIFICheck
    4 - Exit
    """)


def serialcheck():
    se = SerialCheck.SerialCheck('/dev/ttyUSB0')
    se.PshCheck()
    se.keysearch()
    se.close()


def portscan():
    ip = input("input ip address: ")
    port = input("input port number: ")
    np = PortScan.Portscan(ip, port)
    np.run()
    np.getAllPort()

    r = np.isRtspOpen()
    if r:
        rt = RtspCheck.EmptyRtspPasswordCheck(ip)
        rt.run()

def WIFIcheck():
    wificheck = External.WifiCheck("/root/Downloads/SecurityVulnerabilityDetectionTool_v1.3/vdt-v1.3/vdt_wts/")
    wificheck.run()


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main():
    print_title()
    print_menu()
    # parser = argparse.ArgumentParser(description='EZVIZ device security test toolkit')
    # parser.add_argument('ip', metavar='target_host',
    #                     type=str,
    #                     help='Device\'s ip address')
    # parser.add_argument('--port', metavar='target_port',
    #                     type=str,
    #                     help='Port number of device under test')
    # parser.add_argument('--testwifi', metavar='yes|no',
    #                     type=str2bool,
    #                     help='WIFI security test')
    # args = parser.parse_args()

    # if args.testwifi is True:

    while 1:
        choice = {
            0: print_menu,
            1: serialcheck,
            2: portscan,
            3: WIFIcheck,
            4: exit
        }
        sel = int(input("input your choice: "))
        choice.get(sel, print_menu)()
        print_menu()


if __name__ == "__main__":
    main()


