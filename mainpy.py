import re
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QApplication, QInputDialog, QLineEdit, QListWidgetItem, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonZapisz.clicked.connect(self.saveButton)
        self.ui.pushButtonPlik.clicked.connect(self.fileButton)
        self.show()


    def clearInput(self):
        self.ui.lineEditImie.clear()
        self.ui.lineEditNazwisko.clear()
        self.ui.lineEditTel.clear()
        self.ui.lineEditPESEL.clear()

    def people(self):
        person = {
            'name': self.ui.lineEditImie.text(),
            'lastName': self.ui.lineEditNazwisko.text(),
            'tel': self.ui.lineEditTel.text(),
            'PESEL': self.ui.lineEditPESEL.text(),
            'umowa': self.ui.checkBoxUmowa.isChecked()
        }
        return person
    def fileSave(self):
        with open("./employees.txt", "a") as file:
            file.write(f"imie i nazwisko: {self.people()['name']} {self.people()['lastname']} {self.people()['tel']} {self.people()['PESEL']} {self.people()['umowa']}")

    def addPerson(self):
        person = {
            'name': self.ui.lineEditImie.text(),
            'lastName': self.ui.lineEditNazwisko.text(),
            'tel': self.ui.lineEditTel.text(),
            'PESEL': self.ui.lineEditPESEL.text(),
            'umowa': self.ui.checkBoxUmowa.isChecked()
        }
        if re.match(r'^[0-9]{11}',person['PESEL']) is not None:
            employees = f"{person['name']} {person['lastName']} \ntel: {person['tel']} \nPesel: {person['PESEL']} \nUoP: {person['umowa']}"
            # with open("./employees.txt", "a") as file:
            #     file.write(f"imie i nazwisko: {employees}")

            self.ui.listWidgetPracownicy.addItem(employees)
            self.clearInput()
        else:
            mb = QMessageBox()
            mb.setText('pesel jest zly')
            mb.exec()

    def saveButton(self):
        self.addPerson()

    def fileButton(self):
        self.fileSave()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
    print(self.people()['name'])