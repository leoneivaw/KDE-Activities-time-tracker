import datetime
from datetime import date

from Janela import *
import sys
import time


class teste:
    # chamar janela https://stackoverflow.com/questions/43260595/attributeerror-ui-mainwindow-object-has-no-attribute-setcentralwidget
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        ex = Ui_MainWindow()
        w = QtWidgets.QMainWindow()
        ex.setupUi(w)
        w.show()

        today = date.today()
        hoje = str("today")
        ex.label_3.setText(hoje)



        current_time = str(datetime.datetime.now().time())
        ex.label.setText(current_time)

        timer = QtCore.QTimer()
        timer.timeout.connect(update_label)
        timer.start(10000)  # every 10,000 milliseconds
        sys.exit(app.exec_())