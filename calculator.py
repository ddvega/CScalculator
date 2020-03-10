from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyperclip
import texteditor

from MainWindow import Ui_CScalculator
from staticFunctions import *
from math_class import Mathematics
from staticFunctions import *
from hamming import *

# Calculator state.
READY = 0
INPUT = 1


class MainWindow(QMainWindow, Ui_CScalculator):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.myMath = Mathematics()
        self.clearButt.pressed.connect(self.entry.clear)
        # self.hamEncode.pressed.connect(self.)
        # self.loadButt.pressed.connect(self.useLog)


        # button functions
        self.readMeButt.pressed.connect(self.read_me_open)
        self.gcdButt.pressed.connect(self.mathGcd)
        self.sRootButt.pressed.connect(self.mathSqRoot)
        self.factorialButt.pressed.connect(self.mathFactorial)
        self.log2Butt.pressed.connect(self.mathLog2)
        self.log10Butt.pressed.connect(self.mathLog10)
        self.logClearButt.pressed.connect(self.logClear)

        self.stackedWidget.setCurrentIndex(0)
        self.menu.activated[str].connect(self.menu_changed)
        self.cboxbits.activated[str].connect(self.hamBitsDd)
        self.cBoxoddeven.activated[str].connect(self.hamOddEven)
        self.mainScreen.keyPressEvent = self.keyPressEvent
        self.mainScreen.itemSelectionChanged.connect(self.on_change)
        # self.expScreen.itemSelectionChanged.connect(self.expScrChanged)
        # holds value selected in mainScreen
        self.itemSelected = ""
        self.equation = ""
        self.expression = ""
        self.hammingBits = 8
        self.hammingOe = "odd"

        self.show()

    def on_change(self):
        for item in self.mainScreen.selectedItems():
            self.itemSelected = item.text()
            self.entry.setText(self.itemSelected)
            print(self.itemSelected)

    def keyPressEvent(self, e):
        print("event", e)
        if e.key() == Qt.Key_Return:
            if self.menu.currentText() == 'Scientific Mode':
                self.lstAddSci()
            elif self.menu.currentText() == 'Hamming Code Generator':
                self.hamGenerate()
            else:
                return

    def reset(self):
        self.expression = ""
        self.equation = ""
        self.entry.clear()

    def addToScreen(self):
        self.mainScreen.addItem(self.expression)
        self.mainScreen.addItem(self.equation)
        self.mainScreen.addItem("")
        self.mainScreen.scrollToBottom()
        self.reset()

    def mathGcd(self):
        self.expression = self.entry.displayText()
        try:
            a = self.expression.split(',')[0]
            b = self.expression.split(',')[1]
            self.expression = "gcd between " + a + " & " + b
            self.equation = self.myMath.greatestCDenom(a, b)
            self.addToScreen()

        except:
            print("error")
            self.reset()

    def mathFactorial(self):
        self.expression = fixZeros(self.entry.displayText())
        print(type(self.expression))
        try:
            self.equation = self.myMath.factorial(self.expression)
            self.expression = self.expression + " factorial"
            self.addToScreen()
        except:
            self.reset()
            print("error")

    def mathSqRoot(self):
        self.expression = fixZeros(self.entry.displayText())
        try:
            self.equation = self.myMath.squareRoot(self.expression)
            self.expression = "Square Root(" + self.expression + ")"
            self.addToScreen()
        except:
            self.reset()
            print("error")

    def mathLog2(self):
        self.expression = fixZeros(self.entry.displayText())
        try:
            self.equation = self.myMath.log2(self.expression)
            self.expression = "log_2(" + self.expression + ")"
            self.addToScreen()
        except:
            self.reset()
            print("error")

    def mathLog10(self):
        self.expression = fixZeros(self.entry.displayText())
        try:
            self.equation = self.myMath.log10(self.expression)
            self.expression = "log_10(" + self.expression + ")"
            self.addToScreen()
        except:
            self.reset()
            print("error")

    def hamGenerate(self):
        self.expression = self.entry.displayText()
        print(self.expression)
        try:
            num = int(self.expression)
            self.equation = hamCodeGenerator(self.hammingBits, num,
                                             self.hammingOe)
            print(self.equation)
            self.expression = "ham_" + str(self.hammingBits) + "_" + \
                              self.hammingOe + "(" + self.expression + ")"
            self.addToScreen()
        except:
            self.reset()
            print("error")

    def lstAddSci(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            # self.outputScreen.clear()
            self.equation = str(eval(self.expression))
            self.addToScreen()

        except:
            print("error")
            self.reset()

    def logClear(self):
        self.mainScreen.clear()

    def list_add_ham(self):
        self.mainScreen.addItem(self.entry.displayText())

    def read_me_open(self):
        texteditor.open(filename="readme.txt")

    def hamBitsDd(self):
        self.hammingBits = int(self.cboxbits.currentText())
        print(self.hammingBits)

    def hamOddEven(self):
        self.hammingOe = self.cBoxoddeven.currentText()
        print(self.hammingOe)

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
