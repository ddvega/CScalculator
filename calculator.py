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
        self.itemSelected = ""  # holds value of item selected from log
        self.equation = "" # holds value of solved equation
        self.expression = ""  # holds value of user entry
        self.hammingBits = 8  # number of bits for hamming code
        self.hammingOe = "odd"  # even or odd hamming code
        self.bitWidth = '8'  # bit size for binary conversion
        self.binFunctionType = 'dec2bin'  # binary convert function
        self.binSorU = 'unsigned'  # signed or unsiged number

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


        # set options widget to first position
        self.stackedWidget.setCurrentIndex(0)

        # dropdown menus # dd = dropdown
        self.menu.activated[str].connect(self.ddmenuChange)
        self.ddbits.activated[str].connect(self.ddhamBits)
        self.ddoddeven.activated[str].connect(self.ddhamOddEven)
        self.ddBinConvert.activated[str].connect(self.ddBinChange)
        self.ddSignedUnsigned.activated[str].connect(self.ddTypeChange)

        self.logScreen.keyPressEvent = self.keyPressEvent
        self.logScreen.itemSelectionChanged.connect(self.screenSelect)


        self.show()


    def ddBinChange(self):
        self.binFunctionType = self.ddBinConvert.currentText()

    def ddTypeChange(self):
        self.binSorU = self.ddSignedUnsigned.currentText()



    def bin_bin2Dec(self):
        self.expression = self.entry.displayText()
        try:
            self.equation = binaryToDec(self.expression, self.binSorU)
            self.expression = self.expression + "->dec"
            self.logScreenAdd()

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
            self.logScreenAdd()

        except Exception:
            self.resetParams()

    def bin_float2Bin(self):
        self.expression = self.entry.displayText()
        floatWidth = self.entryFloatWidth.displayText()
        print(floatWidth)
        try:
            self.equation = floatToBinary(self.expression, floatWidth)
            self.expression = self.expression + "->binary"
            self.logScreenAdd()

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
            if self.binFunctionType == 'bin2dec':
                self.bin_bin2Dec()
            elif self.binFunctionType == 'dec2bin':
                self.bin_Dec2Bin()
            elif self.binFunctionType == 'float2bin':
                self.bin_float2Bin()

        else:
            return

    def enterButtPressed(self):
        self.enterAction()

    def ddhamBits(self):
        self.hammingBits = int(self.ddbits.currentText())

    def hamGenerate(self):
        self.expression = self.entry.displayText()

        try:
            num = int(self.expression)
            self.equation = hamCodeGenerator(self.hammingBits, num,
                                             self.hammingOe)
            self.expression = "ham_" + str(self.hammingBits) + "_" + \
                              self.hammingOe + "(" + self.expression + ")"
            self.logScreenAdd()

        except Exception:
            self.resetParams()

    def ddhamOddEven(self):
        self.hammingOe = self.ddoddeven.currentText()


    def hamReader(self):
        self.expression = self.entry.displayText()
        try:
            self.equation = hamCodeRead(self.expression)
            self.logScreenAdd()

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
            self.logScreenAdd()

        except Exception:
            self.resetParams()

    def mathGcd(self):
        self.expression = self.entry.displayText()
        try:
            a = self.expression.split(',')[0]
            b = self.expression.split(',')[1]
            self.expression = "gcd between " + a + " & " + b
            self.equation = self.myMath.greatestCDenom(a, b)
            self.logScreenAdd()

        except Exception:
            self.resetParams()

    def mathLog10(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = self.myMath.log10(self.expression)
            self.expression = "log_10(" + self.expression + ")"
            self.logScreenAdd()

        except Exception:
            self.resetParams()

    def mathLog2(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = self.myMath.log2(self.expression)
            self.expression = "log_2(" + self.expression + ")"
            self.logScreenAdd()

        except Exception:
            self.resetParams()

    def mathSqRoot(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = self.myMath.squareRoot(self.expression)
            self.expression = "Square Root(" + self.expression + ")"
            self.logScreenAdd()

        except Exception:
            self.resetParams()

    def ddmenuChange(self):
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

    def logScreenAdd(self):
        self.logScreen.addItem(self.expression)
        self.logScreen.addItem(self.equation)
        self.logScreen.addItem("")
        self.logScreen.scrollToBottom()
        self.resetParams()

    def screenAddHam(self):
        self.logScreen.addItem(self.entry.displayText())

    def screenAddScientific(self):
        try:
            self.expression = fixZeros(self.entry.displayText())
            self.equation = str(eval(self.expression))
            self.logScreenAdd()

        except Exception:
            self.resetParams()

    def screenClear(self):
        self.logScreen.clear()

    def screenSelect(self):
        for item in self.logScreen.selectedItems():
            self.itemSelected = item.text()
            self.entry.setText(self.itemSelected)



if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("TinyCalc")

    window = MainWindow()
    app.exec_()
