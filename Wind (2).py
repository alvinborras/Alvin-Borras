# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wind.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, 20, 801, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("WIND LOGO.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.adminlog = QtWidgets.QPushButton(self.centralwidget)
        self.adminlog.setGeometry(QtCore.QRect(260, 270, 141, 28))
        self.adminlog.setObjectName("adminlog")
        self.guestlog = QtWidgets.QPushButton(self.centralwidget)
        self.guestlog.setGeometry(QtCore.QRect(260, 320, 141, 28))
        self.guestlog.setObjectName("guestlog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.adminlog.setText(_translate("MainWindow", "Admin Login"))
        self.guestlog.setText(_translate("MainWindow", "Guest Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
