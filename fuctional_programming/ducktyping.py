class vscode:
    def complie(self):
        print("compiling using vscode")
    def execute(self):
        print("executing using vscode")
    def debug(self):
        print("debuging using vscode")
class pycharm:
    def complie(self):
        print("compiling using pycharm")
    def execute(self):
        print("executing using pycharm")
    def debug(self):\
        print("debuging using pycharm")
class programmer:
    def coding(self,ide):
        ide.complie()
        ide.execute()
        ide.debug()
dev=programmer()
pyc=pycharm()
dev.coding(pyc)