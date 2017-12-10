# -*-coding:UTF-8-*-
import sys
from PyQt4 import QtGui, QtCore


class Window():
    def __init__(self):
        self.itemType = 0
        self.item_name = ''

    def run(self):

        app = QtGui.QApplication(sys.argv)
        self.w = QtGui.QMainWindow()
        self.w.setGeometry(100, 100, 300, 500)
        self.w.setWindowTitle('RPyG - Admin Tools')

        # Create main menu
        mainMenu = self.w.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('&File')

        # New Items button
        NewItem = QtGui.QAction(QtGui.QIcon('exit24.png'), 'New Item', self.w)
        NewItem.setShortcut('Ctrl+I')
        NewItem.setStatusTip('Create New Item')
        NewItem.triggered.connect(self.newItem)
        fileMenu.addAction(NewItem)

        # New Items button
        NewEnemy = QtGui.QAction(QtGui.QIcon(
            'exit24.png'), 'New Enemy', self.w)
        NewEnemy.setShortcut('Ctrl+E')
        NewEnemy.setStatusTip('Create New Enemy')
        NewEnemy.triggered.connect(self.newEnemy)
        fileMenu.addAction(NewEnemy)

        # Add exit button
        exitButton = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self.w)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.w.close)
        fileMenu.addAction(exitButton)

        self.w.show()
        sys.exit(app.exec_())

    def newItem(self):
        #
        # NEW ITEM PAGE
        #
        self.win = QtGui.QWidget()

        self.NewItem_page = QtGui.QFormLayout()

        name = QtGui.QLineEdit()
        name.textChanged.connect(self.nameChange)
        self.NewItem_page.addRow("Name:", name)

        # self.Type = QtGui.QLabel("Type:", self)
        # self.Type.move(10, 80)

        typeBox = QtGui.QComboBox()
        typeBox.addItem("Equipable")
        typeBox.addItem("Consumible")
        typeBox.setCurrentIndex(self.itemType)
        typeBox.currentIndexChanged.connect(self.slotSelect)

        self.NewItem_page.addRow("Type:", typeBox)

        # self.Slot = QtGui.QLabel("Slot:", self)

    # if self.itemType == 0:
        self.slotBox = QtGui.QComboBox()
        self.slotBox.addItem("Amulet")
        self.slotBox.addItem("1 Hand")
        self.slotBox.addItem("2 Hands")
        self.slotBox.addItem("Armor")
        self.slotBox.addItem("Boots")
        self.NewItem_page.addRow("Slot:", self.slotBox)
    # else:

        Statsgrid = QtGui.QGridLayout()
        self.stats = []
        Statsgrid.addWidget(QtGui.QLabel("STR:"), 0, 0)
        self.stats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.stats[0], 0, 1)
        Statsgrid.addWidget(QtGui.QLabel("POL:"), 1, 0)
        self.stats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.stats[1], 1, 1)
        Statsgrid.addWidget(QtGui.QLabel("END:"), 2, 0)
        self.stats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.stats[2], 2, 1)
        Statsgrid.addWidget(QtGui.QLabel("CHA:"), 3, 0)
        self.stats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.stats[3], 3, 1)
        Statsgrid.addWidget(QtGui.QLabel("INT:"), 0, 3)
        self.stats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.stats[4], 0, 4)
        Statsgrid.addWidget(QtGui.QLabel("AGI:"), 1, 3)
        self.stats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.stats[5], 1, 4)
        Statsgrid.addWidget(QtGui.QLabel("LOV:"), 2, 3)
        self.stats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.stats[6], 2, 4)

        self.NewItem_page.addRow("Stats:", Statsgrid)

        Effectgrid = QtGui.QGridLayout()
        self.stats = []
        Effectgrid.addWidget(QtGui.QLabel("Burn:"), 0, 0)
        self.stats.append(QtGui.QSpinBox())
        Effectgrid.addWidget(self.stats[0], 0, 1)
        Effectgrid.addWidget(QtGui.QLabel("Stun:"), 1, 0)
        self.stats.append(QtGui.QSpinBox())
        Effectgrid.addWidget(self.stats[1], 1, 1)
        Effectgrid.addWidget(QtGui.QLabel("Freeze:"), 2, 0)
        self.stats.append(QtGui.QSpinBox())
        Effectgrid.addWidget(self.stats[2], 2, 1)
        Effectgrid.addWidget(QtGui.QLabel("Poison:"), 3, 0)
        self.stats.append(QtGui.QSpinBox())
        Effectgrid.addWidget(self.stats[3], 3, 1)

        self.NewItem_page.addRow("Effects:", Effectgrid)

        Confirmgrid = QtGui.QGridLayout()

        self.cancelButton = QtGui.QPushButton("Reset")
        Confirmgrid.addWidget(self.cancelButton, 0, 0)
        self.cancelButton.clicked.connect(self.reset)

        self.okButton = QtGui.QPushButton("Add to file")
        Confirmgrid.addWidget(self.okButton, 0, 1)

        self.NewItem_page.addRow(None, Confirmgrid)

        self.win.setLayout(self.NewItem_page)

        self.w.setCentralWidget(self.win)

    def newEnemy(self):
        #
        # NEW ENEMY PAGE
        #

        self.Enemywin = QtGui.QWidget()

        self.NewEnemy_page = QtGui.QFormLayout()

        name = QtGui.QLineEdit()
        name.textChanged.connect(self.nameChange)
        self.NewEnemy_page.addRow("Name:", name)

        Statsgrid = QtGui.QGridLayout()
        self.Enemystats = []
        Statsgrid.addWidget(QtGui.QLabel("STR:"), 0, 0)
        self.Enemystats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.Enemystats[0], 0, 1)
        Statsgrid.addWidget(QtGui.QLabel("POL:"), 1, 0)
        self.Enemystats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.Enemystats[1], 1, 1)
        Statsgrid.addWidget(QtGui.QLabel("END:"), 2, 0)
        self.Enemystats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.Enemystats[2], 2, 1)
        Statsgrid.addWidget(QtGui.QLabel("CHA:"), 3, 0)
        self.Enemystats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.Enemystats[3], 3, 1)
        Statsgrid.addWidget(QtGui.QLabel("INT:"), 0, 3)
        self.Enemystats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.Enemystats[4], 0, 4)
        Statsgrid.addWidget(QtGui.QLabel("AGI:"), 1, 3)
        self.Enemystats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.Enemystats[5], 1, 4)
        Statsgrid.addWidget(QtGui.QLabel("LOV:"), 2, 3)
        self.Enemystats.append(QtGui.QSpinBox())
        Statsgrid.addWidget(self.Enemystats[6], 2, 4)

        self.NewEnemy_page.addRow("Stats:", Statsgrid)

        Confirmgrid = QtGui.QGridLayout()

        self.EnemyokButton = QtGui.QPushButton("Add to file")
        Confirmgrid.addWidget(self.EnemyokButton, 0, 0)

        self.EnemycancelButton = QtGui.QPushButton("Reset")
        Confirmgrid.addWidget(self.EnemycancelButton, 0, 1)
        self.EnemycancelButton.clicked.connect(self.reset)

        self.NewEnemy_page.addRow(None, Confirmgrid)

        self.Enemywin.setLayout(self.NewEnemy_page)

        self.w.setCentralWidget(self.Enemywin)

    def nameChange(self, text):
        self.item_name = text

    def reset(self):
        print('reset')

    def slotSelect(self, data):
        self.itemType = data
        if self.itemType == 1:
            self.slotBox.clear()
            self.slotBox.addItem("Free")
            self.slotBox.addItem("In Battle")
        else:
            self.slotBox.clear()
            self.slotBox.addItem("Amulet")
            self.slotBox.addItem("1 Hand")
            self.slotBox.addItem("2 Hands")
            self.slotBox.addItem("Armor")
            self.slotBox.addItem("Boots")

    def textchanged(self, text):
        print "contents of text box: " + text

    def enterPress():
        print "edited"


if __name__ == '__main__':
    window = Window()
    window.run()
