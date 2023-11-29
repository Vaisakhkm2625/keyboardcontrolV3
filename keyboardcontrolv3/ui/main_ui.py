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
        self.label = QtWidgets.QLabel(parent=self.header)
        self.label.setGeometry(QtCore.QRect(310, 20, 111, 16))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.header)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.event_list_area = QtWidgets.QWidget(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.event_list_area.sizePolicy().hasHeightForWidth())
        self.event_list_area.setSizePolicy(sizePolicy)
        self.event_list_area.setStyleSheet("background-color:red;")
        self.event_list_area.setObjectName("event_list_area")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.event_list_area)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.event_list_area)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 280, 417))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.event_list_area, 0, 2, 1, 1)
        self.actions_stacked_widget_area = QtWidgets.QStackedWidget(parent=self.frame)
        self.actions_stacked_widget_area.setStyleSheet("background-color:blue;\n"
"")
        self.actions_stacked_widget_area.setObjectName("actions_stacked_widget_area")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.actions_stacked_widget_area.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.actions_stacked_widget_area.addWidget(self.page_4)
        self.gridLayout.addWidget(self.actions_stacked_widget_area, 0, 1, 1, 1)
        self.apply = QtWidgets.QPushButton(parent=self.frame)
        self.apply.setObjectName("apply")
        self.gridLayout.addWidget(self.apply, 1, 2, 1, 1)
        self.sidebar = QtWidgets.QWidget(parent=self.frame)
        self.sidebar.setMinimumSize(QtCore.QSize(150, 0))
        self.sidebar.setStyleSheet("background-color: green;")
        self.sidebar.setObjectName("sidebar")
        self.gridLayout.addWidget(self.sidebar, 0, 0, 2, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Keyboard Control"))
        self.apply.setText(_translate("MainWindow", "Apply"))
