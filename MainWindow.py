# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CScalculator(object):
    def setupUi(self, CScalculator):
        CScalculator.setObjectName("CScalculator")
        CScalculator.resize(385, 517)
        CScalculator.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(CScalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainScreen = QtWidgets.QListWidget(self.centralwidget)
        self.mainScreen.setMouseTracking(True)
        self.mainScreen.setFocusPolicy(QtCore.Qt.TabFocus)
        self.mainScreen.setStyleSheet("color: rgb(180, 152, 124);\n"
"background-color: rgb(51, 51, 29);\n"
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.scientific = QtWidgets.QWidget()
        self.scientific.setObjectName("scientific")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scientific)
        self.verticalLayout.setObjectName("verticalLayout")
        self.factorialButt = QtWidgets.QPushButton(self.scientific)
        self.factorialButt.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.factorialButt.setObjectName("factorialButt")
        self.verticalLayout.addWidget(self.factorialButt)
        self.pushButton = QtWidgets.QPushButton(self.scientific)
        self.pushButton.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.scientific)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.sqRtButt = QtWidgets.QPushButton(self.scientific)
        self.sqRtButt.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.sqRtButt.setObjectName("sqRtButt")
        self.verticalLayout.addWidget(self.sqRtButt)
        self.log10Butt = QtWidgets.QPushButton(self.scientific)
        self.log10Butt.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.log10Butt.setObjectName("log10Butt")
        self.verticalLayout.addWidget(self.log10Butt)
        self.log2Butt = QtWidgets.QPushButton(self.scientific)
        self.log2Butt.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.log2Butt.setObjectName("log2Butt")
        self.verticalLayout.addWidget(self.log2Butt)
        self.pushButton_6 = QtWidgets.QPushButton(self.scientific)
        self.pushButton_6.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.scientific)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.stackedWidget.addWidget(self.scientific)
        self.ham = QtWidgets.QWidget()
        self.ham.setObjectName("ham")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ham)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cboxbits = QtWidgets.QComboBox(self.ham)
        self.cboxbits.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.cboxbits.setObjectName("cboxbits")
        self.cboxbits.addItem("")
        self.cboxbits.addItem("")
        self.cboxbits.addItem("")
        self.verticalLayout_4.addWidget(self.cboxbits)
        self.cBoxoddeven = QtWidgets.QComboBox(self.ham)
        self.cBoxoddeven.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.cBoxoddeven.setObjectName("cBoxoddeven")
        self.cBoxoddeven.addItem("")
        self.cBoxoddeven.addItem("")
        self.verticalLayout_4.addWidget(self.cBoxoddeven)
        self.hamEncode = QtWidgets.QPushButton(self.ham)
        self.hamEncode.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.hamEncode.setObjectName("hamEncode")
        self.verticalLayout_4.addWidget(self.hamEncode)
        self.stackedWidget.addWidget(self.ham)
        self.binaryCon = QtWidgets.QWidget()
        self.binaryCon.setObjectName("binaryCon")
        self.stackedWidget.addWidget(self.binaryCon)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.menu = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menu.setFont(font)
        self.menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu.setStyleSheet("color: rgb(179, 147, 112);\n"
"font: 75 15pt \"Menlo\";\n"
"background-color: rgb(8, 8, 8);\n"
"")
        self.menu.setObjectName("menu")
        self.menu.addItem("")
        self.menu.addItem("")
        self.menu.addItem("")
        self.menu.addItem("")
        self.menu.addItem("")
        self.gridLayout_2.addWidget(self.menu, 1, 0, 1, 2)
        self.entry = QtWidgets.QLineEdit(self.centralwidget)
        self.entry.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(180, 152, 124);\n"
"font: 75 18pt \"Menlo\";\n"
"")
        self.entry.setObjectName("entry")
        self.gridLayout_2.addWidget(self.entry, 2, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.readMeButt = QtWidgets.QPushButton(self.widget)
        self.readMeButt.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 9pt \"Menlo\";")
        self.readMeButt.setObjectName("readMeButt")
        self.gridLayout.addWidget(self.readMeButt, 0, 0, 1, 1)
        self.clearButt = QtWidgets.QPushButton(self.widget)
        self.clearButt.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 9pt \"Menlo\";")
        self.clearButt.setObjectName("clearButt")
        self.gridLayout.addWidget(self.clearButt, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 12pt \"Menlo\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 42, 12);\n"
"color: rgb(179, 147, 112);\n"
"font: 75 9pt \"Menlo\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 3, 0, 1, 2)
        CScalculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(CScalculator)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CScalculator)

    def retranslateUi(self, CScalculator):
        _translate = QtCore.QCoreApplication.translate
        CScalculator.setWindowTitle(_translate("CScalculator", "CS-Calculator"))
        self.factorialButt.setText(_translate("CScalculator", "X!"))
        self.pushButton.setText(_translate("CScalculator", "test"))
        self.pushButton_3.setText(_translate("CScalculator", "test"))
        self.sqRtButt.setText(_translate("CScalculator", "sRoot"))
        self.log10Butt.setText(_translate("CScalculator", "LOG10"))
        self.log2Butt.setText(_translate("CScalculator", "LOG2"))
        self.pushButton_6.setText(_translate("CScalculator", "test"))
        self.pushButton_2.setText(_translate("CScalculator", "test"))
        self.cboxbits.setItemText(0, _translate("CScalculator", "8bit"))
        self.cboxbits.setItemText(1, _translate("CScalculator", "16bit"))
        self.cboxbits.setItemText(2, _translate("CScalculator", "32bit"))
        self.cBoxoddeven.setItemText(0, _translate("CScalculator", "odd"))
        self.cBoxoddeven.setItemText(1, _translate("CScalculator", "even"))
        self.hamEncode.setText(_translate("CScalculator", "ENCODE"))
        self.menu.setItemText(0, _translate("CScalculator", "Scientific Mode"))
        self.menu.setItemText(1, _translate("CScalculator", "Hamming Code Generator"))
        self.menu.setItemText(2, _translate("CScalculator", "Hamming Code Reader"))
        self.menu.setItemText(3, _translate("CScalculator", "Dec2Binary"))
        self.menu.setItemText(4, _translate("CScalculator", "Binary2Dec"))
        self.entry.setToolTip(_translate("CScalculator", "<html><head/><body><p>enter equation then hit RETURN</p></body></html>"))
        self.readMeButt.setText(_translate("CScalculator", "ProgInfo"))
        self.clearButt.setText(_translate("CScalculator", "clear"))
        self.pushButton_5.setText(_translate("CScalculator", "ENTER"))
        self.pushButton_4.setText(_translate("CScalculator", "LogClear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CScalculator = QtWidgets.QMainWindow()
    ui = Ui_CScalculator()
    ui.setupUi(CScalculator)
    CScalculator.show()
    sys.exit(app.exec_())
