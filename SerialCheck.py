import serial
import time


class SerialCheck(object):
    def __init__(self, path):
        try:
            self.ser = serial.Serial(path, 115200, timeout=3)
        except OSError:
            print("Failed to read serial port, please re-insert\r\n")
            time.sleep(10)
            self.ser = serial.Serial(path, 115200, timeout=3)

    def PshCheck(self):
        self.ser.write(b'ifconfig\r')
        result = self.ser.read(500)
        print("------------")
        print(result)
        if result.__contains__(b'netmask') or result.__contains__(b'127.0.0.1') or result.__contains__(b'BROADCAST'):
            print("\033[1;31mcan execute linux commands\n\033[0m")
        else:
            print("\033[1;32mcan not execute linux commands\n\033[0m")

    def keysearch(self):
        userinput = input("Enter search keywords: ")
        interval = int(input("Enter search duration: "))
        dict = [n for n in userinput.split()]
        time_start = time.time()
        while True:
            time_end = time.time()
            if time_end - time_start > interval:
                print("Search Finished\r\n")
                return
            line = self.ser.readline()
            for word in dict:
                if line.__contains__(str.encode(word)):
                    print(line)

    def close(self):
        self.ser.close()

# UBOOT CHECK
# Hit Ctrl+u to stop autoboot: