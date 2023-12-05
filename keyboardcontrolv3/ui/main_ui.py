# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(parent=self.centralwidget)
        self.header.setEnabled(True)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.header)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(parent=self.header)
        self.label.setStyleSheet("font: 22pt \"Sans Serif\";")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.header)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.apply = QtWidgets.QPushButton(parent=self.frame)
        self.apply.setObjectName("apply")
        self.gridLayout.addWidget(self.apply, 3, 2, 1, 1)
        self.actions_area = QtWidgets.QStackedWidget(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actions_area.sizePolicy().hasHeightForWidth())
        self.actions_area.setSizePolicy(sizePolicy)
        self.actions_area.setStyleSheet("")
        self.actions_area.setObjectName("actions_area")
        self.gridLayout.addWidget(self.actions_area, 2, 1, 1, 1)
        self.event_area = QtWidgets.QScrollArea(parent=self.frame)
        self.event_area.setWidgetResizable(True)
        self.event_area.setObjectName("event_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 274, 367))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(248, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.event_list = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.event_list.setObjectName("event_list")
        self.verticalLayout_3.addWidget(self.event_list)
        self.event_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.event_area, 2, 2, 1, 1)
        self.tryaction = QtWidgets.QPushButton(parent=self.frame)
        self.tryaction.setObjectName("tryaction")
        self.gridLayout.addWidget(self.tryaction, 3, 1, 1, 1)
        self.widget = QtWidgets.QWidget(parent=self.frame)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.item_name = QtWidgets.QLabel(parent=self.widget)
        self.item_name.setStyleSheet("font-size: 18px; \n"
"font-weight: bold;")
        self.item_name.setObjectName("item_name")
        self.gridLayout_2.addWidget(self.item_name, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 2)
        self.description = QtWidgets.QLabel(parent=self.frame)
        self.description.setStyleSheet("font-size: 14px; ")
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 1, 1, 1, 2)
        self.sidebar__area = QtWidgets.QScrollArea(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar__area.sizePolicy().hasHeightForWidth())
        self.sidebar__area.setSizePolicy(sizePolicy)
        self.sidebar__area.setMinimumSize(QtCore.QSize(100, 0))
        self.sidebar__area.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sidebar__area.setWidgetResizable(True)
        self.sidebar__area.setObjectName("sidebar__area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 198, 435))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.item_list = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_list.sizePolicy().hasHeightForWidth())
        self.item_list.setSizePolicy(sizePolicy)
        self.item_list.setObjectName("item_list")
        self.verticalLayout_2.addWidget(self.item_list)
        self.sidebar__area.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.sidebar__area, 0, 0, 3, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Keyboard Control"))
        self.apply.setText(_translate("MainWindow", "Apply"))
        self.tryaction.setText(_translate("MainWindow", "Try this"))
        self.item_name.setText(_translate("MainWindow", "No item selected"))
        self.description.setText(_translate("MainWindow", "Item description"))
        self.label_2.setText(_translate("MainWindow", "Items"))
