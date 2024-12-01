# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

column_names = ['概况','小区名','所属地区','户型','面积','朝向','装潢','楼层高低','总楼层数','建筑类型','总价','单价','关注度','发布时间','图片地址']
iris_data = pd.read_csv('qingxi.csv', names=column_names, header=0, encoding='utf-8')
iris_data.head()
df=pd.DataFrame(iris_data)
matplotlib.rcParams['font.family'] = 'SimHei'

labels1=['南湖','中邑华章','净月区','小城子','硅谷街北','东风','吉大南岭校区'
    ,'北湖','长沈路','十里堡','柳影','客车厂','天光路','吉大前进校区','东方广场北'
    ,'桂林路','长新街','汽车广场','东方广场南','净水厂','西部新城开发区','小南'
    ,'平阳','欧美工业园','世界雕塑公园','北环沿线','奋进','人民广场西','景阳广场'
    ,'工业大学北湖校区','绿园区周边','红旗','站前','东大桥','友谊公园','和顺'
    ,'大经路','四季青市场','万通','亚泰','劳动公园','欧亚卖场','临河街','北海公园'
    ,'二道区周边','支农东','住邦城市广场','八里堡','西潘家屯','西安广场','支农西','普阳'
    ,'宽城区周边','南部新城','天嘉','硅谷街南','四联大街']
values1=np.array([214,1,156,2,121,3,84,4,82,5,52,6,43,9,40,10,33
                ,12,31,14,30,19,28,22,27,24,26,25,26,26,25,26,24,27,19,29
                ,14,30,14,33,12,34,9,41,7,43,6,54,4,83,4,85,3,135,2,168,1])

fig=plt.figure()
sub=fig.add_subplot(111)
sub.pie(values1,labels=labels1,rotatelabels=True,startangle=90,pctdistance=0.3)
fig.suptitle('房产在各区分布图',fontsize=20)
plt.show()

labels2=['2室1厅','5室4厅','3室2厅','1室2厅','1室1厅','3室3厅','1室0厅','4室1厅'
    ,'2室0厅','3室0厅','4室2厅','4室3厅','3室1厅','5室3厅','2室2厅','6室3厅']
values2=np.array([734,1,434,3,165,5,19,9,14,5,56,4,174,2,481,1])
fig=plt.figure()
sub=fig.add_subplot(111)
sub.pie(values2,labels=labels2,rotatelabels=True,labeldistance=1.3,startangle=90,pctdistance=0.3)
fig.suptitle('房产户型分布图',fontsize=20)
plt.show()

labels3=['精装','简装','其他','毛坯']
values3=np.array([1265,476,236,130])
fig=plt.figure()
sub=fig.add_subplot(111)
sub.pie(values3,labels=labels3)
sub.legend()
fig.suptitle('房产装潢分布图',fontsize=20)
fig.tight_layout()
plt.show()


