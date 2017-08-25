import sys
from PyQt5 import QtWidgets, QtGui
##################################################
# CREATE WINDOW
#app = QtWidgets.QApplication(sys.argv)
#w = QtWidgets.QWidget()
#w.setWindowTitle("WindowTitle")
#w.setGeometry(100, 100, 300, 200)

#w.show()
#sys.exit(app.exec_())

##################################################
# LABEL:
#l1 = QtWidgets.QLabel(w)
#l1.setText("Hello World!")
##l1.setGeometry(100, 50, 100, 100) # Inofficiell
#l1.move(100, 20)

##################################################
# BUTTON:
#b1 = QtWidgets.QPushButton(w)
#b1.setText("Push Me")
#b1.move(100, 50)

##################################################
# PICTURE:
# p1 = QtWidgets.QLabel(w)
# p1.setPixmap(QtGui.QPixmap('QrCode.png'))
# p1.move(10, 10)

##################################################
# Horizontal and Vertical layout boxes
#b = QtWidgets.QPushButton("Push Me")
#l = QtWidgets.QLabel("Look at me")

#h_box = QtWidgets.QHBoxLayout()
#h_box.addStretch()
#h_box.addWidget(l)
#h_box.addStretch()

#v_box = QtWidgets.QVBoxLayout()
#v_box.addWidget(b)
#v_box.addLayout(h_box)
#w.setLayout(v_box)

##################################################
'''
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton("Push Me")
        self.l = QtWidgets.QLabel("I have not been clicked yet")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("PyQt5 Lesson 5")

        self.b.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        self.l.setText("I have been clicked!")


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
'''

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__() # constructor

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton("Clear")
        self.b2 = QtWidgets.QPushButton("Print")

        self.lbl = QtWidgets.QLabel()
        self.chx = QtWidgets.QCheckBox('Do you like dogs?')
        self.btn = QtWidgets.QPushButton('Push Me!')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.chx)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)

        self.setLayout(v_box)
        self.setWindowTitle("PyQt5 Lesson")

        self.b1.clicked.connect(self.btn_clk)
        self.b2.clicked.connect(self.btn_clk)

        self.show()

    def btn_clk(self):
        sender = self.sender()
        if sender.text() == "Print":
            output = self.le.text()
            if self.chx.isChecked():
                output += "\nI guess you like dogs"
            else:
                output += "\nDog hater then"
            print(output)
        else:
            self.le.clear()

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())