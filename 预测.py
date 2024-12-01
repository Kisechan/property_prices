# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
from PyQt5.QtWidgets import QMessageBox

# 目标编码
def target_encoding(df, feature, target):
    encoding_map = df.groupby(feature)[target].mean()
    return df[feature].map(encoding_map)


def df_change_to_features(df):
    features = df.loc[:, ['所属地区', '户型', '小区名', '朝向', '装潢', '楼层高低', '建筑类型']].copy()
    encoding_maps = {}
    for col in ['小区名', '所属地区', '户型', '朝向', '装潢', '楼层高低', '建筑类型']:
        encoding_maps[col] = df.groupby(col)['单价'].mean()
    for col in ['小区名', '所属地区', '户型', '朝向', '装潢', '楼层高低', '建筑类型']:
        features[col + '_encoded'] = df[col].map(encoding_maps[col])
    features = features.drop(['小区名', '所属地区', '户型', '朝向', '装潢', '楼层高低', '建筑类型'], axis=1)
    with open('encoding_maps.pkl', 'wb') as f:
        pickle.dump(encoding_maps, f)
    return features


def df_change_to_features_for_prediction(df):
    features = df.loc[:, ['所属地区', '户型', '小区名', '朝向', '装潢', '楼层高低', '建筑类型']].copy()
    with open('encoding_maps.pkl', 'rb') as f:
        encoding_maps = pickle.load(f)
    for col in ['小区名', '所属地区', '户型', '朝向', '装潢', '楼层高低', '建筑类型']:
        features[col + '_encoded'] = df[col].map(encoding_maps.get(col, {}))
    features = features.drop(['小区名', '所属地区', '户型', '朝向', '装潢', '楼层高低', '建筑类型'], axis=1)
    return features

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1370, 700)
        self.setWindowTitle("预测系统")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setStyleSheet("#centralwidget{border-image:url('page.png');}")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(350, 40, 151, 31))
        self.title.setObjectName("title")


        self.suoshudiqu = QtWidgets.QComboBox(self.centralwidget)
        self.suoshudiqu.setGeometry(QtCore.QRect(20, 150, 250, 80))
        self.suoshudiqu.setObjectName("suoshudiqu")
        self.suoshudiqu.addItems(df['所属地区'].unique())
        self.suoshudiqu.highlighted.connect(self.on_combobox_highlight)
        self.suoshudiqu.currentIndexChanged.connect(self.on_combobox_currentIndexChange)

        self.xiaoquming = QtWidgets.QComboBox(self.centralwidget)
        self.xiaoquming.setGeometry(QtCore.QRect(280, 150, 400, 80))
        self.xiaoquming.setObjectName("xiaoquming")

        self.huxing = QtWidgets.QComboBox(self.centralwidget)
        self.huxing.setGeometry(QtCore.QRect(690, 150, 130, 80))
        self.huxing.setObjectName("huxing")
        self.huxing.addItems(df['户型'].unique())

        self.chaoxiang = QtWidgets.QComboBox(self.centralwidget)
        self.chaoxiang.setGeometry(QtCore.QRect(830, 150, 160, 80))
        self.chaoxiang.setObjectName("chaoxiang")
        self.chaoxiang.addItems(df['朝向'].unique())

        self.zhuanghuang = QtWidgets.QComboBox(self.centralwidget)
        self.zhuanghuang.setGeometry(QtCore.QRect(1000, 150, 100, 80))
        self.zhuanghuang.setObjectName("zhuanghuang")
        self.zhuanghuang.addItems(df['装潢'].unique())

        self.loucenggaodi = QtWidgets.QComboBox(self.centralwidget)
        self.loucenggaodi.setGeometry(QtCore.QRect(1110, 150, 120, 80))
        self.loucenggaodi.setObjectName("loucenggaodi")
        self.loucenggaodi.addItems(df['楼层高低'].unique())

        self.jianzhuleixing = QtWidgets.QComboBox(self.centralwidget)
        self.jianzhuleixing.setGeometry(QtCore.QRect(1240, 150, 120, 80))
        self.jianzhuleixing.setObjectName("jianzhuleixing")
        self.jianzhuleixing.addItems(df['建筑类型'].unique())

        self.pushButton = QtWidgets.QPushButton("确认", self)
        self.pushButton.setGeometry(QtCore.QRect(1160, 400, 200, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_button_click)

        self.show1 = QtWidgets.QLabel("预测结果将在这里显示", self)
        self.show1.setGeometry(QtCore.QRect(240, 360, 351, 71))
        self.show1.setObjectName("show1")

        self.show2 = QtWidgets.QLabel("房价预测", self)
        font = QFont()
        font.setPointSize(20)
        self.show2.setFont(font)
        self.show2.setGeometry(QtCore.QRect(300, 50, 351, 71))
        self.show2.setObjectName("show2")

    def on_button_click(self):
        if self.xiaoquming.currentText()=="":
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
            '单价':[float(10000)]
        }
        df1=pd.DataFrame(data1)
        prediction = model.predict(df_change_to_features_for_prediction(df1))
        self.show1.setText(f"{prediction[0]:.2f}元/平米")  # 显示预测结果

    def on_combobox_highlight(self):
        self.xiaoquming.addItems(df[df['所属地区'] == self.suoshudiqu.currentText()]['小区名'].unique())
    def on_combobox_currentIndexChange(self):
        self.xiaoquming.clear()
        region = self.suoshudiqu.currentText()
        items = df[df['所属地区'] == region]['小区名'].unique()
        self.xiaoquming.addItems(items)



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "房价预测"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">房价预测</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "确认"))

if __name__ == "__main__":
    column_names = ['概况', '小区名', '所属地区', '户型', '面积', '朝向', '装潢', '楼层高低', '总楼层数', '建筑类型', '总价', '单价', '关注度', '发布时间',
                    '图片地址']
    iris_data = data = pd.read_excel('updated.xlsx', usecols=column_names, engine='openpyxl')
    df = pd.DataFrame(iris_data)
    target = iris_data['单价']  # 单价与'小区名', '所属地区', '户型', '朝向', '装潢', '楼层高低', '建筑类型'相关
    model = LinearRegression()
    model.fit(df_change_to_features(df), target)
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
