# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CScalculator(object):
    def setupUi(self, CScalculator):
        CScalculator.setObjectName("CScalculator")
        CScalculator.resize(409, 420)
        CScalculator.setMinimumSize(QtCore.QSize(0, 420))
        CScalculator.setStyleSheet("background-color: rgb(0 , 0,0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(CScalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.menu = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menu.setFont(font)
        self.menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 15pt \"Menlo\";\n"
"background-color: rgb(0,0,0);\n"
"")
        self.menu.setObjectName("menu")
        self.menu.addItem("")
        self.menu.addItem("")
        self.menu.addItem("")
        self.menu.addItem("")
        self.menu.addItem("")
        self.gridLayout_2.addWidget(self.menu, 1, 0, 1, 2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 75))
        self.stackedWidget.setStyleSheet("background-color: rgb(0,0,0);\n"
"")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.scientific = QtWidgets.QWidget()
        self.scientific.setObjectName("scientific")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scientific)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.scientific)
        self.pushButton_2.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.log2Butt = QtWidgets.QPushButton(self.scientific)
        self.log2Butt.setSizeIncrement(QtCore.QSize(0, 0))
        self.log2Butt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.log2Butt.setObjectName("log2Butt")
        self.gridLayout_4.addWidget(self.log2Butt, 11, 0, 1, 1)
        self.log10Butt = QtWidgets.QPushButton(self.scientific)
        self.log10Butt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.log10Butt.setObjectName("log10Butt")
        self.gridLayout_4.addWidget(self.log10Butt, 10, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scientific)
        self.pushButton.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.scientific)
        self.pushButton_3.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.gcdButt = QtWidgets.QPushButton(self.scientific)
        self.gcdButt.setSizeIncrement(QtCore.QSize(0, 0))
        self.gcdButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.gcdButt.setObjectName("gcdButt")
        self.gridLayout_4.addWidget(self.gcdButt, 7, 0, 1, 1)
        self.factorialButt = QtWidgets.QPushButton(self.scientific)
        self.factorialButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.factorialButt.setObjectName("factorialButt")
        self.gridLayout_4.addWidget(self.factorialButt, 8, 0, 1, 1)
        self.sRootButt = QtWidgets.QPushButton(self.scientific)
        self.sRootButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.sRootButt.setObjectName("sRootButt")
        self.gridLayout_4.addWidget(self.sRootButt, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.scientific)
        self.ham = QtWidgets.QWidget()
        self.ham.setObjectName("ham")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ham)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.ham)
        self.label.setStyleSheet("background-color: rgb(0,0,0);\n"
"color: rgb(181,137, 0);\n"
"font: 75 13pt \"Menlo\";\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.cboxbits = QtWidgets.QComboBox(self.ham)
        self.cboxbits.setMinimumSize(QtCore.QSize(0, 50))
        self.cboxbits.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.cboxbits.setObjectName("cboxbits")
        self.cboxbits.addItem("")
        self.cboxbits.addItem("")
        self.cboxbits.addItem("")
        self.verticalLayout.addWidget(self.cboxbits)
        self.label_2 = QtWidgets.QLabel(self.ham)
        self.label_2.setStyleSheet("background-color: rgb(0,0,0);\n"
"color: rgb(181,137, 0);\n"
"font: 75 13pt \"Menlo\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.cBoxoddeven = QtWidgets.QComboBox(self.ham)
        self.cBoxoddeven.setMinimumSize(QtCore.QSize(0, 50))
        self.cBoxoddeven.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.cBoxoddeven.setObjectName("cBoxoddeven")
        self.cBoxoddeven.addItem("")
        self.cBoxoddeven.addItem("")
        self.verticalLayout.addWidget(self.cBoxoddeven)
        self.label.raise_()
        self.cboxbits.raise_()
        self.cBoxoddeven.raise_()
        self.label_2.raise_()
        self.stackedWidget.addWidget(self.ham)
        self.binaryCon = QtWidgets.QWidget()
        self.binaryCon.setObjectName("binaryCon")
        self.stackedWidget.addWidget(self.binaryCon)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.entry = QtWidgets.QLineEdit(self.centralwidget)
        self.entry.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(180, 152, 124);\n"
"font: 75 18pt \"Menlo\";\n"
"")
        self.entry.setObjectName("entry")
        self.gridLayout_2.addWidget(self.entry, 2, 0, 1, 2)
        self.mainScreen = QtWidgets.QListWidget(self.centralwidget)
        self.mainScreen.setMouseTracking(True)
        self.mainScreen.setFocusPolicy(QtCore.Qt.TabFocus)
        self.mainScreen.setStyleSheet("color: rgb(181,137, 0);\n"
"background-color: rgb(49, 49, 49);\n"
"font: 75 11pt \"Menlo\";\n"
"selection-color: rgb(22, 22, 22);\n"
"selection-background-color: rgb(139, 56, 24);\n"
"\n"
"\n"
"")
        self.mainScreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainScreen.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mainScreen.setLineWidth(1)
        self.mainScreen.setMidLineWidth(0)
        self.mainScreen.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mainScreen.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainScreen.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.mainScreen.setAutoScroll(False)
        self.mainScreen.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.mainScreen.setResizeMode(QtWidgets.QListView.Adjust)
        self.mainScreen.setViewMode(QtWidgets.QListView.ListMode)
        self.mainScreen.setSelectionRectVisible(False)
        self.mainScreen.setObjectName("mainScreen")
        self.gridLayout_2.addWidget(self.mainScreen, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(0,0,0);\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.readMeButt = QtWidgets.QPushButton(self.widget)
        self.readMeButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.readMeButt.setObjectName("readMeButt")
        self.gridLayout.addWidget(self.readMeButt, 0, 0, 1, 1)
        self.clearButt = QtWidgets.QPushButton(self.widget)
        self.clearButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.clearButt.setObjectName("clearButt")
        self.gridLayout.addWidget(self.clearButt, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 3, 0, 1, 2)
        CScalculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(CScalculator)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(CScalculator)

    def retranslateUi(self, CScalculator):
        _translate = QtCore.QCoreApplication.translate
        CScalculator.setWindowTitle(_translate("CScalculator", "CS-Calculator"))
        self.menu.setItemText(0, _translate("CScalculator", "Scientific Mode"))
        self.menu.setItemText(1, _translate("CScalculator", "Hamming Code Generator"))
        self.menu.setItemText(2, _translate("CScalculator", "Hamming Code Reader"))
        self.menu.setItemText(3, _translate("CScalculator", "Dec2Binary"))
        self.menu.setItemText(4, _translate("CScalculator", "Binary2Dec"))
        self.pushButton_2.setText(_translate("CScalculator", "test"))
        self.log2Butt.setText(_translate("CScalculator", "LOG2"))
        self.log10Butt.setText(_translate("CScalculator", "LOG10"))
        self.pushButton.setText(_translate("CScalculator", "test"))
        self.pushButton_3.setText(_translate("CScalculator", "test"))
        self.gcdButt.setText(_translate("CScalculator", "GCD"))
        self.factorialButt.setText(_translate("CScalculator", "X!"))
        self.sRootButt.setText(_translate("CScalculator", "sRoot"))
        self.label.setText(_translate("CScalculator", "BITS"))
        self.cboxbits.setItemText(0, _translate("CScalculator", "8"))
        self.cboxbits.setItemText(1, _translate("CScalculator", "16"))
        self.cboxbits.setItemText(2, _translate("CScalculator", "32"))
        self.label_2.setText(_translate("CScalculator", "TYPE"))
        self.cBoxoddeven.setItemText(0, _translate("CScalculator", "odd"))
        self.cBoxoddeven.setItemText(1, _translate("CScalculator", "even"))
        self.entry.setToolTip(_translate("CScalculator", "<html><head/><body><p>enter equation then hit RETURN</p></body></html>"))
        self.readMeButt.setText(_translate("CScalculator", "INFO"))
        self.clearButt.setText(_translate("CScalculator", "CLEAR"))
        self.pushButton_5.setText(_translate("CScalculator", "ENTER"))
        self.pushButton_4.setText(_translate("CScalculator", "LOGCLR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CScalculator = QtWidgets.QMainWindow()
    ui = Ui_CScalculator()
    ui.setupUi(CScalculator)
    CScalculator.show()
    sys.exit(app.exec_())
