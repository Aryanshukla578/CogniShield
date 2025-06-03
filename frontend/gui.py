# GUI placeholder using PyQt5
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('CogniShield GUI')
label = QLabel('<h1>Welcome to CogniShield</h1>', parent=window)
window.show()
sys.exit(app.exec_())
