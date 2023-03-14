# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_menu.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_menu.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setStyleSheet("border:none;\n"
"height:35px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color:rgb(65, 184, 131);\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textEdit = QtWidgets.QTextEdit(self.frame_menu)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout.addWidget(self.frame_menu, 0, 0, 1, 1)
        self.frame_Bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_Bottom.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_Bottom.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.frame_Bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Bottom.setObjectName("frame_Bottom")
        self.gridLayout.addWidget(self.frame_Bottom, 1, 0, 1, 2)
        self.widget_content = QtWidgets.QWidget(self.centralwidget)
        self.widget_content.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_content.sizePolicy().hasHeightForWidth())
        self.widget_content.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget_content.setFont(font)
        self.widget_content.setStyleSheet("\n"
"background-color: rgb(231, 231, 231);")
        self.widget_content.setObjectName("widget_content")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_content)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_content, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
        self.menuLOGO = QtWidgets.QMenu(self.menubar)
        self.menuLOGO.setEnabled(False)
        self.menuLOGO.setTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Desktop/icon_date@1.5x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuLOGO.setIcon(icon)
        self.menuLOGO.setObjectName("menuLOGO")
        self.menu_9 = QtWidgets.QMenu(self.menubar)
        self.menu_9.setObjectName("menu_9")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_8 = QtWidgets.QMenu(self.menu)
        self.menu_8.setObjectName("menu_8")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        self.menuName = QtWidgets.QMenu(self.menubar)
        self.menuName.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menuName.setFont(font)
        self.menuName.setStyleSheet("")
        self.menuName.setObjectName("menuName")
        MainWindow.setMenuBar(self.menubar)
        self.actiondaoru = QtWidgets.QAction(MainWindow)
        self.actiondaoru.setObjectName("actiondaoru")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actiondaochu_2 = QtWidgets.QAction(MainWindow)
        self.actiondaochu_2.setObjectName("actiondaochu_2")
        self.actionbaocun = QtWidgets.QAction(MainWindow)
        self.actionbaocun.setObjectName("actionbaocun")
        self.actionchehui = QtWidgets.QAction(MainWindow)
        self.actionchehui.setObjectName("actionchehui")
        self.actionguanbi = QtWidgets.QAction(MainWindow)
        self.actionguanbi.setObjectName("actionguanbi")
        self.actiontuichu = QtWidgets.QAction(MainWindow)
        self.actiontuichu.setObjectName("actiontuichu")
        self.actiondayin = QtWidgets.QAction(MainWindow)
        self.actiondayin.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.actiondayin.setObjectName("actiondayin")
        self.actiontuichu_2 = QtWidgets.QAction(MainWindow)
        self.actiontuichu_2.setObjectName("actiontuichu_2")
        self.actionguanbi_2 = QtWidgets.QAction(MainWindow)
        self.actionguanbi_2.setObjectName("actionguanbi_2")
        self.actionEXCEL = QtWidgets.QAction(MainWindow)
        self.actionEXCEL.setObjectName("actionEXCEL")
        self.actionCSV = QtWidgets.QAction(MainWindow)
        self.actionCSV.setObjectName("actionCSV")
        self.actionSHUJUKU = QtWidgets.QAction(MainWindow)
        self.actionSHUJUKU.setObjectName("actionSHUJUKU")
        self.menu_8.addAction(self.actionEXCEL)
        self.menu_8.addAction(self.actionCSV)
        self.menu_8.addAction(self.actionSHUJUKU)
        self.menu.addAction(self.actiondaoru)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_8.menuAction())
        self.menu.addAction(self.actiondaochu_2)
        self.menu.addAction(self.actionbaocun)
        self.menu.addAction(self.actionchehui)
        self.menu.addAction(self.actionguanbi)
        self.menu.addSeparator()
        self.menu.addAction(self.actiontuichu)
        self.menu.addAction(self.actiontuichu_2)
        self.menu.addAction(self.actionguanbi_2)
        self.menu_6.addSeparator()
        self.menubar.addAction(self.menuLOGO.menuAction())
        self.menubar.addAction(self.menuName.menuAction())
        self.menubar.addAction(self.menu_9.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "姓名"))
        self.menu_9.setTitle(_translate("MainWindow", "保存"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.menu_8.setTitle(_translate("MainWindow", "导入"))
        self.menu_2.setTitle(_translate("MainWindow", "公式"))
        self.menu_3.setTitle(_translate("MainWindow", "绘图"))
        self.menu_4.setTitle(_translate("MainWindow", "筛选"))
        self.menu_5.setTitle(_translate("MainWindow", "设计"))
        self.menu_6.setTitle(_translate("MainWindow", "更多"))
        self.menuName.setTitle(_translate("MainWindow", "BI"))
        self.actiondaoru.setText(_translate("MainWindow", "新建"))
        self.action_2.setText(_translate("MainWindow", "打开"))
        self.actiondaochu_2.setText(_translate("MainWindow", "导出"))
        self.actionbaocun.setText(_translate("MainWindow", "保存"))
        self.actionchehui.setText(_translate("MainWindow", "另存为"))
        self.actionguanbi.setText(_translate("MainWindow", "打印"))
        self.actiontuichu.setText(_translate("MainWindow", "撤回"))
        self.actiondayin.setText(_translate("MainWindow", "打印"))
        self.actiontuichu_2.setText(_translate("MainWindow", "退出"))
        self.actionguanbi_2.setText(_translate("MainWindow", "关闭"))
        self.actionEXCEL.setText(_translate("MainWindow", "EXCEL"))
        self.actionCSV.setText(_translate("MainWindow", "CSV"))
        self.actionSHUJUKU.setText(_translate("MainWindow", "数据库"))
