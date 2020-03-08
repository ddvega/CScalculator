from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyperclip
import texteditor

from MainWindow import Ui_CScalculator

# Calculator state.
READY = 0
INPUT = 1


class MainWindow(QMainWindow, Ui_CScalculator):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #self.basEnterButt.pressed.connect(self.list_add_basic)
        self.clearButt.pressed.connect(self.clearEntry)
        # self.hamEncode.pressed.connect(self.)
        # self.loadButt.pressed.connect(self.useLog)
        self.readMeButt.pressed.connect(self.read_me_open)
        self.stackedWidget.setCurrentIndex(0)
        self.menu.activated[str].connect(self.menu_changed)
        self.mainScreen.keyPressEvent = self.keyPressEvent
        self.mainScreen.itemSelectionChanged.connect(self.on_change)
        # self.expScreen.itemSelectionChanged.connect(self.expScrChanged)

        # holds value selected in mainScreen
        self.itemSelected = ""
        self.equation = ""

        self.show()

    def clearEntry(self):
        self.entry.clear()

    def on_change(self):
        for item in self.mainScreen.selectedItems():
            self.itemSelected = item.text()
            self.entry.setText(self.itemSelected)
            print(self.itemSelected)

    # def expScrChanged(self):
    #     for item in self.expScreen.selectedItems():
    #         self.itemSelected = item.text()
    #         self.entry.setText(self.itemSelected)
    #         print(self.itemSelected)

    # what happens when you push enter key
    def keyPressEvent(self, e):
        print("event", e)
        if e.key() == Qt.Key_Return:
            if self.menu.currentText() == 'Scientific Mode':
                self.list_add_basic()
            elif self.menu.currentText() == 'Hamming Code Generator':
                self.list_add_ham()
            else:
                return

    def useLog(self):
        print("hello there")

    # def display(self):
    #     self.outputScreen.insertPlainText(self.equation)

    def onClick(self):
        self.evalulate()

    def list_add_basic(self):
        tval = self.evalulate()
        self.entry.setText("")
        self.mainScreen.addItem(tval)
        # self.expScreen.addItem(self.expression)
        self.expression = ""

    def list_add_ham(self):
        self.mainScreen.addItem(self.entry.displayText())

    def evalulate(self):
        self.expression = self.entry.displayText()
        # self.outputScreen.clear()
        self.equation = str(eval(self.entry.displayText()))
        # self.display()
        return str(eval(self.entry.displayText()))

    def read_me_open(self):
        texteditor.open(filename="readme.txt")

    def menu_changed(self):
        value = self.menu.currentText()

        if value == 'Scientific Mode':
            self.stackedWidget.setCurrentIndex(0)

        if value == 'Hamming Code Generator':
            self.stackedWidget.setCurrentIndex(1)

        if value == 'Dec2Binary':
            self.stackedWidget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("TinyCalc")

    window = MainWindow()
    app.exec_()
