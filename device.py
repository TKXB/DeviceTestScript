class DeviceInfo(object):

    def __init__(self):
        self.PortList = []
        self.hostname = ""
        self.isrtspvul = False # 是否启动rtsp登录认证
        self.islinuxcommandexe = False # 是否可以执行linux系统命令


