# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/andi/Sandbox/IDP/client-app/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from rabbit_mq import AsyncMessageManager
from storage import Storage
from threading import Thread


def is_valid_shipment_id(input):
    if not input:
        return False
    try:
        val = int(input)
    except ValueError:
        return False

    return True


def consume(async_manager):
    async_manager.receive()


class Ui_MainWindow(object):
    def __init__(self):
        self.storage = Storage()
        self.model = QStandardItemModel()
        self.async_manager = AsyncMessageManager(self.storage)
        self.shipment_consumer = Thread(target=consume, args=(self.async_manager,))
        self.shipment_consumer.daemon = True
        self.shipment_consumer.start()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 164, 60);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 10, 721, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.shipment = QtWidgets.QWidget()
        self.shipment.setObjectName("shipment")
        self.frame = QtWidgets.QFrame(self.shipment)
        self.frame.setGeometry(QtCore.QRect(-11, -11, 741, 551))
        self.frame.setStyleSheet("background-color: rgb(184, 255, 253);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(620, 220, 88, 29))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 270, 88, 29))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 44, 25);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(35, 31, 551, 451))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(610, 90, 111, 61))
        self.label.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 500, 181, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 242, 140);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.shipment)
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setObjectName("main_widget")
        self.main_widget_frame = QtWidgets.QFrame(self.main_widget)
        self.main_widget_frame.setGeometry(QtCore.QRect(200, 0, 311, 501))
        self.main_widget_frame.setStyleSheet("background-color: rgb(255, 250, 103);")
        self.main_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_widget_frame.setObjectName("main_widget_frame")
        self.submit_button = QtWidgets.QPushButton(self.main_widget_frame)
        self.submit_button.setGeometry(QtCore.QRect(150, 390, 141, 51))
        self.submit_button.setStyleSheet("background-color: rgb(169, 240, 255);")
        self.submit_button.setObjectName("submit_button")
        self.input_line_edit = QtWidgets.QLineEdit(self.main_widget_frame)
        self.input_line_edit.setGeometry(QtCore.QRect(150, 290, 141, 51))
        self.input_line_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-color: rgb(0, 0, 0);")
        self.input_line_edit.setObjectName("input_line_edit")
        self.shipment_id_label = QtWidgets.QLabel(self.main_widget_frame)
        self.shipment_id_label.setGeometry(QtCore.QRect(20, 290, 121, 51))
        self.shipment_id_label.setObjectName("shipment_id_label")
        self.shipment_selection_label = QtWidgets.QLabel(self.main_widget_frame)
        self.shipment_selection_label.setGeometry(QtCore.QRect(0, 0, 311, 171))
        self.shipment_selection_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.shipment_selection_label.setObjectName("shipment_selection_label")
        self.warning_label = QtWidgets.QLabel(self.main_widget_frame)
        self.warning_label.setGeometry(QtCore.QRect(40, 200, 231, 61))
        self.warning_label.setStyleSheet("background-color: rgb(255, 93, 61);")
        self.warning_label.setObjectName("warning_label")
        self.stackedWidget.addWidget(self.main_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bind_actions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT"))
        self.shipment_id_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline;\">Shipment ID:</span></p></body></html>"))
        self.shipment_selection_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\"> Shipment Selection</span></p></body></html>"))
        self.warning_label.setText(_translate("MainWindow", "Warning: "))
        self.pushButton.setText(_translate("MainWindow", "Complete"))
        self.pushButton_2.setText(_translate("MainWindow", "Returned"))
        self.pushButton_3.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">DONE!</span></p></body></html>"))

    def populate_table(self):
        if not self.async_manager.is_already_populated():
            return
        shipment_info = self.async_manager.get_shipment_info()
        self.tableView.clearSpans()

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'Status', 'Warehouse ID', 'Address'])
        for order_id, order in shipment_info.items():
            row = [
                QStandardItem(str(order['id'])),
                QStandardItem(str(order['status'])),
                QStandardItem(str(order['warehouse_id'])),
                QStandardItem(str(order['address']))
            ]
            self.model.appendRow(row)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()

    def change_window(self):
        index = 0 if self.stackedWidget.currentIndex() == 1 else 1
        self.stackedWidget.setCurrentIndex(index)

    def submit_shipment(self):
        if is_valid_shipment_id(self.input_line_edit.text()):
            self.async_manager.send_shipment_id(int(self.input_line_edit.text()))
        self.change_window()

    def order_done(self, source="done"):
        orderId = [row.data() for row in self.tableView.selectionModel().selectedRows()]
        if not orderId:
            return
        message = {
            "order_id": orderId,
            "source": source
        }
        self.async_manager.send_order_done(message)
        self.refresh()

    def refresh(self):
        self.populate_table()

    def order_returned(self):
        self.order_done("returned")

    def bind_actions(self):
        self.submit_button.clicked.connect(self.submit_shipment)
        self.pushButton_3.clicked.connect(self.refresh)
        self.pushButton.clicked.connect(self.order_done)
        self.pushButton_2.clicked.connect(self.order_returned)
