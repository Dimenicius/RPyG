import sys
from PyQt4.QtGui import QApplication, QDialog
from listaInventario1 import Ui_Dialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
