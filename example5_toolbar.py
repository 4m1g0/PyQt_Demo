import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QMessageBox
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
        
        extractAction = QAction('something', self)
        extractAction.triggered.connect(self.messageBox)
        
        self.toolBar = self.addToolBar("something cool")
        self.toolBar.addAction(extractAction)
        
        self.show()
    
    # this does NOT close the application
    def close_application(self):
        print("whoooa so custom")
        self.setWindowTitle(self.windowTitle() + "!")
    
    def messageBox(self):
        choice = QMessageBox.question(self, 'Test message', 'delete all HDD?', QMessageBox.Yes | QMessageBox.No)
        
        if choice == QMessageBox.Yes:
            print('Ok, deleted...')
        else:
            print('...')
        
        
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
    
run()
