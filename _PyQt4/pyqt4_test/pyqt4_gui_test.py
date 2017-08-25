import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500, 250, 500, 250)
        self.setWindowTitle("Nuts!")
        # self.setWindowIcon(QtGui.QIcon('pic.png'))

        extract_action = QtGui.QAction("Git Aout!", self)
        extract_action.setShortcut("Ctrl+Q")
        extract_action.setStatusTip("Leave the app")
        extract_action.triggered.connect(self.close_application)

        self.statusBar()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(extract_action)

        self.home()

    def home(self):
        # Button:
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(400, 75)

        # Toolbar:
        extract_action = QtGui.QAction(QtGui.QIcon('toxic_smiley_icon.png'), "Flee the Scene", self)
        extract_action.triggered.connect(self.close_application)
        self.tool_bar = self.addToolBar("Extraction")
        self.tool_bar.addAction(extract_action)

        # Checkbox:
        check_box = QtGui.QCheckBox("Enlarge Window", self)
        check_box.resize(150, 30)
        check_box.move(400, 100)
        check_box.stateChanged.connect(self.enlarge_window)

        # Progress bar with button:
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(150, 80, 250, 20)
        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200, 100)
        self.btn.clicked.connect(self.download)

        # Drop down list with different style choices:
        self.styleChoice = QtGui.QLabel("Windows Vista", self)

        combo_box = QtGui.QComboBox()
        combo_box.addItems(QtGui.QStyleFactory.keys())

        combo_box.move(50, 100)
        self.styleChoice.move(25, 75)
        combo_box.activated[str].connect(self.style_choice)

        self.show()

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(500, 250, 1000, 600)
        else:
            self.setGeometry(500, 250, 500, 300)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Exit",
                                            "Le Sure?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def main():
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
