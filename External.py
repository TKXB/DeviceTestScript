import subprocess
import os


class WifiCheck:
    def __init__(self, path):
        self.path = path

    def run(self):
        nowpath = os.getcwd()
        os.chdir(self.path)
        self.check("./vdt_agent --5.2.1", timeout=100, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.check("./vdt_agent --5.2.2", timeout=100, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.check("./vdt_agent --5.2.3", timeout=100, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.check("./vdt_agent --5.2.4", timeout=100, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.check("./vdt_agent --5.3.1", timeout=100, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.check("./vdt_agent --5.4.1", timeout=100, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.chdir(nowpath)

    def check(*popenargs, timeout=None, **kwargs):
        with subprocess.Popen(*popenargs, **kwargs) as p:
            try:
                p.wait(timeout=timeout)
                out, err = p.communicate()
                isvul = True
                if err is not None:
                    # print("stderr output")
                    # print(err.decode())
                    if err.__contains__(b"Client DOESN'T seem vulnerable"):
                        print("Client DOESN'T seem vulnerable")
                        isvul = False
                if out is not None:
                    # print("stdout output")
                    # print(out.decode())
                    if out.__contains__(b"Client DOESN'T seem vulnerable"):
                        print("Client DOESN'T seem vulnerable")
                        isvul = False
                if isvul:
                    print("Client seem vulnerable")
            except subprocess.TimeoutExpired:
                print("Timeout, Client DOESN'T seem vulnerable")
                p.kill()
                p.wait()

            except:
                print("terminating...")
                p.kill()
                p.wait()
                raise

os.chdir("")

