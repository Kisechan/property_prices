# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
import pandas as pd

def get_row_by_column_value(df, column_name, value):#未加任何限定条件的平均最大最小值
    row = df[df[column_name] == value]
    if row.empty:
        return None
    return row
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1590, 1400)
        self.setWindowTitle("统计系统")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setStyleSheet("#centralwidget{border-image:url('page2.jpg');}")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(350, 40, 151, 31))
        self.title.setObjectName("title")

        self.suoshudiqu = QtWidgets.QComboBox(self.centralwidget)
        self.suoshudiqu.setGeometry(QtCore.QRect(20, 150, 250, 80))
        self.suoshudiqu.setObjectName("suoshudiqu")
        self.suoshudiqu.addItems(df['所属地区'].unique())
        self.suoshudiqu.setCurrentIndex(-1)
        self.suoshudiqu.highlighted.connect(self.on_combobox_highlight)
        self.suoshudiqu.currentIndexChanged.connect(self.on_combobox_currentIndexChange)

        self.xiaoquming = QtWidgets.QComboBox(self.centralwidget)
        self.xiaoquming.setGeometry(QtCore.QRect(280, 150, 400, 80))
        self.xiaoquming.setObjectName("xiaoquming")

        self.huxing = QtWidgets.QComboBox(self.centralwidget)
        self.huxing.setGeometry(QtCore.QRect(690, 150, 130, 80))
        self.huxing.setObjectName("huxing")
        self.huxing.addItems(df['户型'].unique())
        self.huxing.setCurrentIndex(-1)

        self.chaoxiang = QtWidgets.QComboBox(self.centralwidget)
        self.chaoxiang.setGeometry(QtCore.QRect(830, 150, 160, 80))
        self.chaoxiang.setObjectName("chaoxiang")
        self.chaoxiang.addItems(df['朝向'].unique())
        self.chaoxiang.setCurrentIndex(-1)

        self.zhuanghuang = QtWidgets.QComboBox(self.centralwidget)
        self.zhuanghuang.setGeometry(QtCore.QRect(1000, 150, 100, 80))
        self.zhuanghuang.setObjectName("zhuanghuang")
        self.zhuanghuang.addItems(df['装潢'].unique())
        self.zhuanghuang.setCurrentIndex(-1)

        self.loucenggaodi = QtWidgets.QComboBox(self.centralwidget)
        self.loucenggaodi.setGeometry(QtCore.QRect(1110, 150, 120, 80))
        self.loucenggaodi.setObjectName("loucenggaodi")
        self.loucenggaodi.addItems(df['楼层高低'].unique())
        self.loucenggaodi.setCurrentIndex(-1)

        self.jianzhuleixing = QtWidgets.QComboBox(self.centralwidget)
        self.jianzhuleixing.setGeometry(QtCore.QRect(1240, 150, 120, 80))
        self.jianzhuleixing.setObjectName("jianzhuleixing")
        self.jianzhuleixing.addItems(df['建筑类型'].unique())
        self.jianzhuleixing.setCurrentIndex(-1)

        self.duixiang = QtWidgets.QComboBox(self.centralwidget)
        self.duixiang.setGeometry(QtCore.QRect(1260, 270, 180, 80))
        self.duixiang.setObjectName("duixiang")
        self.duixiang.addItems(['面积','总楼层数','总价','单价','关注度'])
        self.duixiang.setCurrentIndex(-1)

        self.tongji = QtWidgets.QComboBox(self.centralwidget)
        self.tongji.setGeometry(QtCore.QRect(1450, 270, 120, 80))
        self.tongji.setObjectName("tongji")
        self.tongji.addItems(['最大值','最小值','平均值'])
        self.tongji.setCurrentIndex(-1)

        self.pushButton = QtWidgets.QPushButton("确认", self)
        self.pushButton.setGeometry(QtCore.QRect(1400, 400, 200, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_button_click)

        self.pushButton1 = QtWidgets.QPushButton("一键清空", self)
        self.pushButton1.setGeometry(QtCore.QRect(1400, 510, 200, 100))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.on_button_click1)

        self.show1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.show1.setGeometry(QtCore.QRect(240, 360, 1000, 1000))
        self.show1.setObjectName("show1")

        self.show2 = QtWidgets.QLabel("房产统计", self)
        font = QFont()
        font.setPointSize(20)
        self.show2.setFont(font)
        self.show2.setGeometry(QtCore.QRect(720, 50, 351, 71))
        self.show2.setObjectName("show2")

    def on_button_click(self):
        if self.duixiang.currentText()=="" or self.tongji.currentText()=="":
            QMessageBox.warning(self, '提示', '请确认筛选内容', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if self.suoshudiqu.currentText()=="" and self.huxing.currentText()==""and self.xiaoquming.currentText()==""and self.chaoxiang.currentText()==""and self.zhuanghuang.currentText()==""and self.loucenggaodi.currentText()==""and self.jianzhuleixing.currentText()=="":
            QMessageBox.warning(self, '提示', '请确认筛选内容', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        data1 = {
            '所属地区': [self.suoshudiqu.currentText()],
            '户型': [self.huxing.currentText()],
            '小区名': [self.xiaoquming.currentText()],
            '朝向': [self.chaoxiang.currentText()],
            '装潢': [self.zhuanghuang.currentText()],
            '楼层高低': [self.loucenggaodi.currentText()],
            '建筑类型': [self.jianzhuleixing.currentText()],
            '对象':[self.duixiang.currentText()],
            '统计':[self.tongji.currentText()]
        }
        df1=pd.DataFrame(data1)
        filtered_df=df.copy()
        for col in ['小区名', '所属地区', '户型', '朝向', '装潢', '楼层高低', '建筑类型']:
            if df1[col].values[0]!="":
                filtered_df = filtered_df[filtered_df[col] == df1[col].values[0] ]
        if filtered_df.empty:
            QMessageBox.warning(self, '提示', '没有符合条件的内容', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if self.tongji.currentText()=="平均值":
            self.show1.setText(f"{self.duixiang.currentText()}的{self.tongji.currentText()}为{filtered_df[self.duixiang.currentText()].mean():.2f}")
        elif self.tongji.currentText()=="最大值":
            max_value = filtered_df[self.duixiang.currentText()].max()
            result = get_row_by_column_value(filtered_df, self.duixiang.currentText(), max_value)
            text = ""
            for index, row in result.iterrows():
                text += str(row.to_dict()) + "\n\n"
            self.show1.setText(f"{self.duixiang.currentText()}的{self.tongji.currentText()}为{max_value:.2f}\n\n{text}")
        elif self.tongji.currentText()=="最小值":
            min_value = filtered_df[self.duixiang.currentText()].min()
            result = get_row_by_column_value(filtered_df, self.duixiang.currentText(), min_value)
            text = ""
            for index, row in result.iterrows():
                text += str(row.to_dict()) + "\n\n"
            self.show1.setText(f"{self.duixiang.currentText()}的{self.tongji.currentText()}为{min_value:.2f}\n\n{text}")

    def on_combobox_highlight(self):
        self.xiaoquming.addItems(df[df['所属地区'] == self.suoshudiqu.currentText()]['小区名'].unique())
        self.xiaoquming.setCurrentIndex(-1)
    def on_combobox_currentIndexChange(self):
        self.xiaoquming.clear()
        region = self.suoshudiqu.currentText()
        items = df[df['所属地区'] == region]['小区名'].unique()
        self.xiaoquming.addItems(items)
        self.xiaoquming.setCurrentIndex(-1)

    def on_button_click1(self):
        self.tongji.setCurrentIndex(-1)
        self.duixiang.setCurrentIndex(-1)
        self.suoshudiqu.setCurrentIndex(-1)
        self.xiaoquming.setCurrentIndex(-1)
        self.huxing.setCurrentIndex(-1)
        self.chaoxiang.setCurrentIndex(-1)
        self.zhuanghuang.setCurrentIndex(-1)
        self.loucenggaodi.setCurrentIndex(-1)
        self.jianzhuleixing.setCurrentIndex(-1)
        self.show1.clear()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "房价预测"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">房价预测</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "确认"))

if __name__ == "__main__":
    column_names = ['概况', '小区名', '所属地区', '户型', '面积', '朝向', '装潢', '楼层高低', '总楼层数', '建筑类型', '总价', '单价', '关注度', '发布时间',
                    '图片地址']
    iris_data = pd.read_excel('updated.xlsx', usecols=column_names, engine='openpyxl')
    df = pd.DataFrame(iris_data)


    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
