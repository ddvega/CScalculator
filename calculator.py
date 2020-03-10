from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from MainWindow import Ui_CScalculator
from math_class import Mathematics
from staticFunctions import *
from hamming import *


class MainWindow(QMainWindow, Ui_CScalculator):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.myMath = Mathematics()

        # variables
        self.itemSelected = ""
        self.equation = ""
        self.expression = ""
        self.hammingBits = 8
        self.hammingOe = "odd"
        self.bitWidth = '8'

        # button functions
        self.clearButt.pressed.connect(self.entry.clear)
        self.readMeButt.pressed.connect(show_read_me)
        self.gcdButt.pressed.connect(self.mathGcd)
        self.sRootButt.pressed.connect(self.mathSqRoot)
        self.factorialButt.pressed.connect(self.mathFactorial)
        self.log2Butt.pressed.connect(self.mathLog2)
        self.log10Butt.pressed.connect(self.mathLog10)
        self.logClearButt.pressed.connect(self.screenClear)
        self.entButt.pressed.connect(self.enterButtPressed)
        #self.binDecButt.pressed.connect(self.bin_bin2Dec)
        #self.decBinButt.pressed.connect(self.bin_Dec2Bin)
        #self.floatBinButt.pressed.connect(self.bin_float2Bin)

        # radio buttons


        # dropdown menus
        self.stackedWidget.setCurrentIndex(0)
        self.menu.activated[str].connect(self.menuChange)
        self.cboxbits.activated[str].connect(self.hamBitsDd)
        self.cBoxoddeven.activated[str].connect(self.hamOddEven)
        self.mainScreen.keyPressEvent = self.keyPressEvent
        self.mainScreen.itemSelectionChanged.connect(self.screenSelect)

        self.show()



    def bin_bin2Dec(self):
        self.expression = self.entry.displayText()
        try:
            self.equation = binaryToDec(self.expression)
            self.expression = self.expression + "->dec"
            self.screenAdd()

        except Exception:
            self.resetParams()


    def bin_Dec2Bin(self):
        self.expression = self.entry.displayText()
        self.bitWidth = self.entryBitWidth.displayText()
        print(self.expression)
        print(self.bitWidth)
        try:

            self.equation = decToBinary(self.expression, self.bitWidth)
            self.expression = self.expression + "->binary"
            self.screenAdd()

        except Exception:
            self.resetParams()

    def bin_float2Bin(self):
        self.expression = self.entry.displayText()
        floatWidth = self.entryFloatWidth.displayText()
        print(floatWidth)
        try:
            self.equation = floatToBinary(self.expression, floatWidth)
            self.expression = self.expression + "->binary"
            self.screenAdd()

        except Exception:
            self.resetParams()

    def enterAction(self):
        if self.menu.currentText() == 'Scientific Mode':
            self.screenAddScientific()
        elif self.menu.currentText() == 'Hamming Code Generator':
            self.hamGenerate()
        elif self.menu.currentText() == 'Hamming Code Reader':
            self.hamReader()
        elif self.menu.currentText()== 'Binary Converter':
            if self.radioBinInt.isChecked():
                self.bin_bin2Dec()
            elif self.radioIntBin.isChecked():
                self.bin_Dec2Bin()
            elif self.radioFloatBin.isChecked():
                self.bin_float2Bin()

        else:
            return

    def enterButtPressed(self):
        self.enterAction()

    def hamBitsDd(self):
        self.hammingBits = int(self.cboxbits.currentText())

    def hamGenerate(self):
        self.expression = self.entry.displayText()

        try:
            num = int(self.expression)
            self.equation = hamCodeGenerator(self.hammingBits, num,
                                             self.hammingOe)
            self.expression = "ham_" + str(self.hammingBits) + "_" + \
                              self.hammingOe + "(" + self.expression + ")"
            self.screenAdd()

        except Exception:
            self.resetParams()

    def hamOddEven(self):
        self.hammingOe = self.cBoxoddeven.currentText()


    def hamReader(self):
        self.expression = self.entry.displayText()
        try:
            self.equation = hamCodeRead(self.expression)
            self.screenAdd()

        except Exception:
            self.resetParams()

    def keyPressEvent(self, e):
        print("event", e)
        if e.key() == Qt.Key_Return:
            self.enterAction()

    def mathFactorial(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = self.myMath.factorial(self.expression)
            self.expression = self.expression + " factorial"
            self.screenAdd()

        except Exception:
            self.resetParams()

    def mathGcd(self):
        self.expression = self.entry.displayText()
        try:
            a = self.expression.split(',')[0]
            b = self.expression.split(',')[1]
            self.expression = "gcd between " + a + " & " + b
            self.equation = self.myMath.greatestCDenom(a, b)
            self.screenAdd()

        except Exception:
            self.resetParams()

    def mathLog10(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = self.myMath.log10(self.expression)
            self.expression = "log_10(" + self.expression + ")"
            self.screenAdd()

        except Exception:
            self.resetParams()

    def mathLog2(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = self.myMath.log2(self.expression)
            self.expression = "log_2(" + self.expression + ")"
            self.screenAdd()

        except Exception:
            self.resetParams()

    def mathSqRoot(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = self.myMath.squareRoot(self.expression)
            self.expression = "Square Root(" + self.expression + ")"
            self.screenAdd()

        except Exception:
            self.resetParams()

    def menuChange(self):
        value = self.menu.currentText()

        if value == 'Scientific Mode':
            self.stackedWidget.setCurrentIndex(0)

        if value == 'Hamming Code Generator':
            self.stackedWidget.setCurrentIndex(1)

        if value == 'Hamming Code Reader':
            self.stackedWidget.setCurrentIndex(2)

        if value == 'Binary Converter':
            self.stackedWidget.setCurrentIndex(3)

    def resetParams(self):
        self.expression = ""
        self.equation = ""
        self.entry.clear()

    def screenAdd(self):
        self.mainScreen.addItem(self.expression)
        self.mainScreen.addItem(self.equation)
        self.mainScreen.addItem("")
        self.mainScreen.scrollToBottom()
        self.resetParams()

    def screenAddHam(self):
        self.mainScreen.addItem(self.entry.displayText())

    def screenAddScientific(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = str(eval(self.expression))
            self.screenAdd()

        except Exception:
            self.resetParams()

    def screenClear(self):
        self.mainScreen.clear()

    def screenSelect(self):
        for item in self.mainScreen.selectedItems():
            self.itemSelected = item.text()
            self.entry.setText(self.itemSelected)



if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("TinyCalc")

    window = MainWindow()
    app.exec_()
