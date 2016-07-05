import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction
from PyQt5 import QtCore

class Window(QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Test example 1")
        
        extractAction = QAction("&Do something", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("leave the app")
        extractAction.triggered.connect(self.close_application)
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        
        self.home()
   
    def home(self):
        btn = QPushButton("Quit", self)
        btn.move(100,100)
        btn.clicked.connect(self.close_application)
        self.show()
    
    def close_application(self):
        print("whoooa so custom")
        self.setWindowTitle(self.windowTitle() + "!")
        
        
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
    
run()
