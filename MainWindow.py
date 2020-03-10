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
        CScalculator.resize(404, 420)
        CScalculator.setMinimumSize(QtCore.QSize(0, 420))
        CScalculator.setStyleSheet("background-color: rgb(0 , 0,0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(CScalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(0,0,0);\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.readMeButt = QtWidgets.QPushButton(self.widget)
        self.readMeButt.setMinimumSize(QtCore.QSize(0, 25))
        self.readMeButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.readMeButt.setObjectName("readMeButt")
        self.gridLayout.addWidget(self.readMeButt, 0, 0, 1, 1)
        self.clearButt = QtWidgets.QPushButton(self.widget)
        self.clearButt.setMinimumSize(QtCore.QSize(0, 25))
        self.clearButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.clearButt.setObjectName("clearButt")
        self.gridLayout.addWidget(self.clearButt, 0, 2, 1, 1)
        self.entButt = QtWidgets.QPushButton(self.widget)
        self.entButt.setMinimumSize(QtCore.QSize(0, 25))
        self.entButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.entButt.setObjectName("entButt")
        self.gridLayout.addWidget(self.entButt, 0, 4, 1, 1)
        self.logClearButt = QtWidgets.QPushButton(self.widget)
        self.logClearButt.setMinimumSize(QtCore.QSize(0, 25))
        self.logClearButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.logClearButt.setObjectName("logClearButt")
        self.gridLayout.addWidget(self.logClearButt, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 5, 1, 1, 2)
        self.mainScreen = QtWidgets.QListWidget(self.centralwidget)
        self.mainScreen.setMinimumSize(QtCore.QSize(175, 205))
        self.mainScreen.setMouseTracking(True)
        self.mainScreen.setFocusPolicy(QtCore.Qt.TabFocus)
        self.mainScreen.setStyleSheet("color: rgb(181,137, 0);\n"
"background-color: rgb(49, 49, 49);\n"
"font: 75 13pt \"Menlo\";\n"
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
        self.gridLayout_2.addWidget(self.mainScreen, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 6, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 2, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.entry = QtWidgets.QLineEdit(self.centralwidget)
        self.entry.setMinimumSize(QtCore.QSize(0, 32))
        self.entry.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(180, 152, 124);\n"
"font: 75 18pt \"Menlo\";\n"
"")
        self.entry.setObjectName("entry")
        self.gridLayout_2.addWidget(self.entry, 4, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(15, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.menu = QtWidgets.QComboBox(self.centralwidget)
        self.menu.setMinimumSize(QtCore.QSize(0, 15))
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
        self.gridLayout_2.addWidget(self.menu, 3, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 230))
        self.stackedWidget.setStyleSheet("background-color: rgb(0,0,0);\n"
"")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.scientific = QtWidgets.QWidget()
        self.scientific.setObjectName("scientific")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scientific)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gcdButt = QtWidgets.QPushButton(self.scientific)
        self.gcdButt.setMinimumSize(QtCore.QSize(0, 25))
        self.gcdButt.setSizeIncrement(QtCore.QSize(0, 0))
        self.gcdButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.gcdButt.setObjectName("gcdButt")
        self.gridLayout_4.addWidget(self.gcdButt, 5, 0, 1, 1)
        self.sRootButt = QtWidgets.QPushButton(self.scientific)
        self.sRootButt.setMinimumSize(QtCore.QSize(0, 25))
        self.sRootButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.sRootButt.setObjectName("sRootButt")
        self.gridLayout_4.addWidget(self.sRootButt, 7, 0, 1, 1)
        self.log2Butt = QtWidgets.QPushButton(self.scientific)
        self.log2Butt.setMinimumSize(QtCore.QSize(0, 25))
        self.log2Butt.setSizeIncrement(QtCore.QSize(0, 0))
        self.log2Butt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.log2Butt.setObjectName("log2Butt")
        self.gridLayout_4.addWidget(self.log2Butt, 9, 0, 1, 1)
        self.factorialButt = QtWidgets.QPushButton(self.scientific)
        self.factorialButt.setMinimumSize(QtCore.QSize(0, 25))
        self.factorialButt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.factorialButt.setObjectName("factorialButt")
        self.gridLayout_4.addWidget(self.factorialButt, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scientific)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_2.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.log10Butt = QtWidgets.QPushButton(self.scientific)
        self.log10Butt.setMinimumSize(QtCore.QSize(0, 25))
        self.log10Butt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.log10Butt.setObjectName("log10Butt")
        self.gridLayout_4.addWidget(self.log10Butt, 8, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 10, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.scientific)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_3.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.scientific)
        self.ham = QtWidgets.QWidget()
        self.ham.setObjectName("ham")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ham)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        self.label = QtWidgets.QLabel(self.ham)
        self.label.setStyleSheet("background-color: rgb(0,0,0);\n"
"color: rgb(181,137, 0);\n"
"font: 75 13pt \"Menlo\";\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.cboxbits = QtWidgets.QComboBox(self.ham)
        self.cboxbits.setMinimumSize(QtCore.QSize(0, 40))
        self.cboxbits.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.cboxbits.setObjectName("cboxbits")
        self.cboxbits.addItem("")
        self.cboxbits.addItem("")
        self.cboxbits.addItem("")
        self.verticalLayout.addWidget(self.cboxbits)
        spacerItem8 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem8)
        self.label_2 = QtWidgets.QLabel(self.ham)
        self.label_2.setStyleSheet("background-color: rgb(0,0,0);\n"
"color: rgb(181,137, 0);\n"
"font: 75 13pt \"Menlo\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.cBoxoddeven = QtWidgets.QComboBox(self.ham)
        self.cBoxoddeven.setMinimumSize(QtCore.QSize(0, 40))
        self.cBoxoddeven.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 12pt \"Menlo\";\n"
"background-color: rgb(7 ,54 ,66);")
        self.cBoxoddeven.setObjectName("cBoxoddeven")
        self.cBoxoddeven.addItem("")
        self.cBoxoddeven.addItem("")
        self.verticalLayout.addWidget(self.cBoxoddeven)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem9)
        self.label.raise_()
        self.cboxbits.raise_()
        self.cBoxoddeven.raise_()
        self.label_2.raise_()
        self.stackedWidget.addWidget(self.ham)
        self.binaryCon = QtWidgets.QWidget()
        self.binaryCon.setObjectName("binaryCon")
        self.stackedWidget.addWidget(self.binaryCon)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioFloatBin = QtWidgets.QRadioButton(self.groupBox)
        self.radioFloatBin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.radioFloatBin.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(0,0,0);")
        self.radioFloatBin.setObjectName("radioFloatBin")
        self.gridLayout_3.addWidget(self.radioFloatBin, 2, 0, 1, 1)
        self.radioIntBin = QtWidgets.QRadioButton(self.groupBox)
        self.radioIntBin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.radioIntBin.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(0,0,0);")
        self.radioIntBin.setChecked(True)
        self.radioIntBin.setObjectName("radioIntBin")
        self.gridLayout_3.addWidget(self.radioIntBin, 1, 0, 1, 1)
        self.radioBinInt = QtWidgets.QRadioButton(self.groupBox)
        self.radioBinInt.setMaximumSize(QtCore.QSize(90, 16777215))
        self.radioBinInt.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(0,0,0);")
        self.radioBinInt.setObjectName("radioBinInt")
        self.gridLayout_3.addWidget(self.radioBinInt, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(0,0,0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.entryBitWidth = QtWidgets.QLineEdit(self.page)
        self.entryBitWidth.setMinimumSize(QtCore.QSize(0, 25))
        self.entryBitWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.entryBitWidth.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(180, 152, 124);\n"
"font: 75 10pt \"Menlo\";")
        self.entryBitWidth.setObjectName("entryBitWidth")
        self.verticalLayout_2.addWidget(self.entryBitWidth, 0, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setStyleSheet("color: rgb(181,137, 0);\n"
"font: 75 9pt \"Menlo\";\n"
"background-color: rgb(0,0,0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.entryFloatWidth = QtWidgets.QLineEdit(self.page)
        self.entryFloatWidth.setMinimumSize(QtCore.QSize(0, 25))
        self.entryFloatWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.entryFloatWidth.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(180, 152, 124);\n"
"font: 75 10pt \"Menlo\";")
        self.entryFloatWidth.setObjectName("entryFloatWidth")
        self.verticalLayout_2.addWidget(self.entryFloatWidth, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        CScalculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(CScalculator)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CScalculator)

    def retranslateUi(self, CScalculator):
        _translate = QtCore.QCoreApplication.translate
        CScalculator.setWindowTitle(_translate("CScalculator", "CS-Calculator"))
        self.readMeButt.setText(_translate("CScalculator", "INFO"))
        self.clearButt.setText(_translate("CScalculator", "CLEAR"))
        self.entButt.setText(_translate("CScalculator", "ENTER"))
        self.logClearButt.setText(_translate("CScalculator", "LOGCLR"))
        self.entry.setToolTip(_translate("CScalculator", "<html><head/><body><p>enter equation then hit RETURN</p></body></html>"))
        self.menu.setItemText(0, _translate("CScalculator", "Scientific Mode"))
        self.menu.setItemText(1, _translate("CScalculator", "Hamming Code Generator"))
        self.menu.setItemText(2, _translate("CScalculator", "Hamming Code Reader"))
        self.menu.setItemText(3, _translate("CScalculator", "Binary Converter"))
        self.gcdButt.setText(_translate("CScalculator", "GCD"))
        self.sRootButt.setText(_translate("CScalculator", "sRoot"))
        self.log2Butt.setText(_translate("CScalculator", "LOG2"))
        self.factorialButt.setText(_translate("CScalculator", "X!"))
        self.pushButton_2.setText(_translate("CScalculator", "test"))
        self.log10Butt.setText(_translate("CScalculator", "LOG10"))
        self.pushButton_3.setText(_translate("CScalculator", "test"))
        self.label.setText(_translate("CScalculator", "BITS"))
        self.cboxbits.setItemText(0, _translate("CScalculator", "8"))
        self.cboxbits.setItemText(1, _translate("CScalculator", "16"))
        self.cboxbits.setItemText(2, _translate("CScalculator", "32"))
        self.label_2.setText(_translate("CScalculator", "TYPE"))
        self.cBoxoddeven.setItemText(0, _translate("CScalculator", "odd"))
        self.cBoxoddeven.setItemText(1, _translate("CScalculator", "even"))
        self.groupBox.setTitle(_translate("CScalculator", "GroupBox"))
        self.radioFloatBin.setText(_translate("CScalculator", "float2bin"))
        self.radioIntBin.setText(_translate("CScalculator", "int2bin"))
        self.radioBinInt.setText(_translate("CScalculator", "bin2int"))
        self.label_3.setText(_translate("CScalculator", " bit width"))
        self.entryBitWidth.setText(_translate("CScalculator", "8"))
        self.label_4.setText(_translate("CScalculator", "float width"))
        self.entryFloatWidth.setText(_translate("CScalculator", "4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CScalculator = QtWidgets.QMainWindow()
    ui = Ui_CScalculator()
    ui.setupUi(CScalculator)
    CScalculator.show()
    sys.exit(app.exec_())
