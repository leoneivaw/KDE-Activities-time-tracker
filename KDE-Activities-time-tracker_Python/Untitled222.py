import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("untitled.ui")

    window.show


def slot(object):
    print("Key was pressed, id is:", cs_group.id(object))

    if cs_group.id(object) == 4:
        print("é quatro")  # Leonardo



window.show()
app.exec()