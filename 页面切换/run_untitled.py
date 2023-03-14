from idlelib import window

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRegExp
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTableView, QVBoxLayout
from untitled import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel


def data():
    return [
        ["John", "Doe", 30],
        ["Jane", "Smith", 25],
        ["Bob", "Johnson", 45],
    ]

class pages_Window(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 循环遍历所有单元格，并添加数据
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                text = f"({row+1}, {col+1})"
                item.setText(text)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, col, item)



        # 设置信号与槽

        import csv
        def export_to_csv(table_widget, filename):
            with open(filename, "w", newline='') as file:
                writer = csv.writer(file)
                for row in range(table_widget.rowCount()):
                    row_data = []
                    for column in range(table_widget.columnCount()):
                        item = table_widget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append("")  # 补充空值
                    writer.writerow(row_data)

        # 使用示例
        # export_to_csv(table_widget, "data.csv")

        # 获取左侧按钮1、2和3
        # self.pushButton = self.ui.pushButton
    #     self.pushButton_2 = self.ui.pushButton_2
    #     self.pushButton_3 = self.ui.pushButton_3
    #     #点击左侧按钮1切换到第一个页面
    #     self.pushButton.clicked.connect(self.display_page1)
    #     # 点击左侧按钮2切换到第二个页面
    #     self.pushButton_2.clicked.connect(self.display_page2)
    #     # 点击左侧按钮3切换到第三个页面
    #     self.pushButton_3.clicked.connect(self.display_page3)
    #
    # def display_page1(self):
    #     self.ui.stackedWidget.setCurrentIndex(0)
    # def display_page2(self):
    #     self.ui.stackedWidget.setCurrentIndex(1)
    # def display_page3(self):
    #     self.ui.stackedWidget.setCurrentIndex(2)


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # mainWindow = pages_Window()
    # mainWindow.show()
    # sys.exit(app.exec_())
    app = QtWidgets.QApplication([])
    window = pages_Window()
    window.show()
    app.exec_()
