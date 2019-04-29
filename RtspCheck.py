import rtsp

class EmptyRtspPasswordCheck(object):

    def __init__(self, ip):
        self.url = "rtsp://admin:@"+ip

    def run(self):
        isVul = True
        client = rtsp.Client(rtsp_server_uri=self.url)
        try:
            client.read()
            print("\033[1;31mThis Device RTSP is vulnerable, Can log in with a blank password\033[0m")
        except:
            isVul = False
            print("\033[1;32mThis Device RTSP is not vulnerable\033[0m")