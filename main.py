# coding:utf-8

import rtspcheck
import portscan
import serialcheck
import external
import argparse
import reportbuilder
import device
import configparser

# 加载配置文件
config_raw = configparser.RawConfigParser()
config_raw.read("./config.cfg")


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
    4 - generateReport
    5 - Exit
    """)


def serial_info_check():
    global device
    se = serialcheck.SerialCheck(config_raw.get('DEFAULT', 'SERIAL_PATH'))
    se.PshCheck(device)
    se.keysearch()
    se.close()


def portscan():
    global device
    ip = input("input ip address: ")
    port = input("input port number(Default all): ")
    np = portscan.Portscan(ip, port)
    np.run()
    np.get_ports_and_hostname(device)

    r = np.isRtspOpen()
    if r:
        rt = rtspcheck.EmptyRtspPasswordCheck(ip)
        rt.run()


def WIFIcheck():
    wificheck = external.WifiCheck(config_raw.get('DEFAULT', 'WIFISecurityDetectionTool'))
    wificheck.run()


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def generateReport():
    global device
    report = reportbuilder.GenerateReport(device)
    report.run()


def main():
    print_title()
    print_menu()

    while 1:
        choice = {
            0: print_menu,
            1: serial_info_check,
            2: portscan,
            3: WIFIcheck,
            4: generateReport,
            5: exit
        }
        sel = int(input("input your choice: "))
        choice.get(sel, print_menu)()
        print_menu()


if __name__ == "__main__":
    device = device.DeviceInfo()
    main()


