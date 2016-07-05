import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtCore

class Window(QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Test example 1")
        self.home()
   
    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()
        
        
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
    
run()
