# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(712, 467)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 50, 651, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxUmowa = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.checkBoxUmowa.setObjectName("checkBoxUmowa")
        self.gridLayout.addWidget(self.checkBoxUmowa, 4, 0, 1, 1)
        self.lineEditNazwisko = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditNazwisko.setObjectName("lineEditNazwisko")
        self.gridLayout.addWidget(self.lineEditNazwisko, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditTel = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditTel.setObjectName("lineEditTel")
        self.gridLayout.addWidget(self.lineEditTel, 2, 1, 1, 1)
        self.lineEditPESEL = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditPESEL.setMaxLength(11)
        self.lineEditPESEL.setObjectName("lineEditPESEL")
        self.gridLayout.addWidget(self.lineEditPESEL, 3, 1, 1, 1)
        self.listWidgetPracownicy = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.listWidgetPracownicy.setObjectName("listWidgetPracownicy")
        self.gridLayout.addWidget(self.listWidgetPracownicy, 0, 2, 4, 1)
        self.pushButtonZapisz = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonZapisz.setObjectName("pushButtonZapisz")
        self.gridLayout.addWidget(self.pushButtonZapisz, 4, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditImie = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditImie.setObjectName("lineEditImie")
        self.gridLayout.addWidget(self.lineEditImie, 0, 1, 1, 1)
        self.pushButtonPlik = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonPlik.setObjectName("pushButtonPlik")
        self.gridLayout.addWidget(self.pushButtonPlik, 5, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBoxUmowa.setText(_translate("Dialog", "Umowa o prace"))
        self.label_2.setText(_translate("Dialog", "Nazwisko"))
        self.label_3.setText(_translate("Dialog", "nrTel"))
        self.label.setText(_translate("Dialog", "Imie"))
        self.pushButtonZapisz.setText(_translate("Dialog", "Zapisz"))
        self.label_4.setText(_translate("Dialog", "PESEL"))
        self.pushButtonPlik.setText(_translate("Dialog", "Zapisz do pliku"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
