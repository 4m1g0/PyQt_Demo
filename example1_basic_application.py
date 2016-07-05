import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Window(QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Test example 1")
        self.show()
        
app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
