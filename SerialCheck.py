import serial
class SerialCheck(object):
    def __init__(self, path):
        self.ser = serial.Serial(path, 115200, timeout=3)

    def PshCheck(self):
        self.ser.write(b'ifconfig\r')
        result = self.ser.read(200)
        print("------------")
        print(result)
        if result.__contains__(b'netmask'):
            print("\033[1;31mcan execute linux commands\n\033[0m")
        else:
            print("\033[1;32mcan not execute linux commands\n\033[0m")
        self.ser.close()