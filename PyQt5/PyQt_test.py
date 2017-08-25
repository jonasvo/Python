import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt

SLIDER1_STDVALUE = 50

class Window(QWidget):

    def __init__(self):
        super().__init__() # constructor

        self.init_ui()

    def init_ui(self):
        self.radio_lbl = QLabel("Which do you like best?")
        self.radio_dog = QRadioButton("Dogs")
        self.radio_cat = QRadioButton("Cats")

        self.le = QLineEdit("50")
        self.b_clear = QPushButton("Clear")
        self.b_print = QPushButton("Print")
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(0)
        self.s1.setMaximum(100)
        self.s1.setValue(SLIDER1_STDVALUE)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QSlider.TicksBelow)

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_lbl)
        v_box.addWidget(self.radio_dog)
        v_box.addWidget(self.radio_cat)
        v_box.addWidget(self.le)
        v_box.addWidget(self.b_clear)
        v_box.addWidget(self.b_print)
        v_box.addWidget(self.s1)

        self.setLayout(v_box)
        self.setWindowTitle("PyQt5 Test")

        self.b_clear.clicked.connect(lambda: self.btn_clk(self.b_clear, "Clearing..."))
        self.b_print.clicked.connect(lambda: self.btn_clk(self.b_print, "Printing: "))
        self.s1.valueChanged.connect(self.v_change)

        self.show()

    def btn_clk(self, b_action, string):
        output = ""
        if self.radio_cat.isChecked():
            output = "Cat Lover is "
        if self.radio_dog.isChecked():
            output = "Dog Lover is "

        output += string
        if b_action.text() == "Print":
            output += self.le.text()
        else:
            self.le.clear()
            self.s1.setValue(SLIDER1_STDVALUE)

        print(output)

    def v_change(self):
        my_value = str(self.s1.value())
        self.le.setText(my_value)

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())