# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\ema\diplProjekt\GUIpricing.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(538, 408)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 30, 81, 31))
        self.pushButton_2.setStyleSheet("bacground-color : red;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 30, 81, 31))
        self.pushButton_3.setStyleSheet("bacground-color : red;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 30, 81, 31))
        self.pushButton_4.setStyleSheet("bacground-color : red;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 250, 361, 16))
        self.horizontalSlider.setMaximum(20000)
        self.horizontalSlider.setSingleStep(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(230, 110, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(60, 110, 71, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 150, 71, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 180, 111, 51))
        self.checkBox_3.setObjectName("checkBox_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 150, 101, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(230, 190, 101, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Pause"))
        self.pushButton_3.setText(_translate("Dialog", "Stop"))
        self.pushButton_4.setText(_translate("Dialog", "Start"))
        self.comboBox.setItemText(0, _translate("Dialog", "Classic"))
        self.comboBox.setItemText(1, _translate("Dialog", "Halogen"))
        self.comboBox.setItemText(2, _translate("Dialog", "Led"))
        self.comboBox.setItemText(3, _translate("Dialog", "New Item"))
        self.comboBox.setItemText(4, _translate("Dialog", "Energy saving"))
        self.checkBox.setText(_translate("Dialog", "Bulb"))
        self.checkBox_2.setText(_translate("Dialog", "AC"))
        self.checkBox_3.setText(_translate("Dialog", "Washing machine"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Small"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Medium"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Big"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Type 1"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Type 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

