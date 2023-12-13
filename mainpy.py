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
        self.show()


    # def validatePESEL(self):
    #     PESEL = self.ui.lineEditPESEL.text(),
    #     return re.match(r'^[0-9]{11}',PESEL) is not None



    def clearInput(self):
        self.ui.lineEditImie.clear()
        self.ui.lineEditNazwisko.clear()
        self.ui.lineEditTel.clear()
        self.ui.lineEditPESEL.clear()

    def addPerson(self):
        # Pesel=''
        # if self.validatePESEL():
        #      pesel = self.ui.lineEditPESEL.text()
        # else:
        #     mb = QMessageBox()
        #     mb.setText('pesel jest zly')
        #     mb.exec()
        person = {
            'name': self.ui.lineEditImie.text(),
            'lastName': self.ui.lineEditNazwisko.text(),
            'tel': self.ui.lineEditTel.text(),
            'PESEL': self.ui.lineEditPESEL.text(),
            'umowa': self.ui.checkBoxUmowa.isChecked()
        }

        employees = f"{person['name']} {person['lastName']} \ntel: {person['tel']} \nPesel: {person['PESEL']} \nUoP: {person['umowa']}"
        with open("./employees.txt", "a") as file:
            file.write(f"imie i nazwisko: {employees}")

        self.ui.listWidgetPracownicy.addItem(employees)
        self.clearInput()


    def saveButton(self):
        self.addPerson()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())