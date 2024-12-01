# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

column_names = ['概况','小区名','所属地区','户型','面积','朝向','装潢','楼层高低','总楼层数','建筑类型','总价','单价','关注度','发布时间','图片地址']
iris_data = pd.read_csv('二手房数据（2880条）.csv', names=column_names, header=0)
iris_data.head()
df=pd.DataFrame(iris_data)
df['概况']=df['概况'].str.replace('\n',' ')
df['小区名']=df['小区名'].str.replace(' ','')
df['所属地区']=df['所属地区'].str.replace(' ','')
df['户型']=df['户型'].str.replace(' ','')
df['面积']=df['面积'].str.replace(' ','')
df['面积']=df['面积'].str.replace('平米','')
#df['面积']=df['面积'].astype(np.float64)
df['朝向']=df['朝向'].map(str.strip)
df['装潢']=df['装潢'].str.replace(' ','')
df['楼层高低']=df['楼层高低'].str.replace(' ','')
df['建筑类型']=df['建筑类型'].str.replace(' ','')
df['总价']=df['总价'].str.replace('万','')
#df['总价']=df['总价'].astype(np.float64)
df['单价']=df['单价'].str.replace(',','')
df['单价']=df['单价'].str.replace('元/平','')
#df['单价']=df['单价'].astype(np.int32)
df['关注度']=df['关注度'].str.replace('人关注','')
df['关注度']=df['关注度'].str.replace(' ','')
#df['关注度']=df['关注度'].astype(np.int32)
df['发布时间']=df['发布时间'].str.replace(' ','')
df['发布时间'] = df['发布时间'].str.replace('以前发布', '前')
df['发布时间'] = df['发布时间'].str.replace('前发布', '前')
df['总楼层数'] = df['总楼层数'].astype(int, errors='ignore')
df = df.astype({'单价': float, '总价': float, '面积': float ,'关注度': int})
df = df.drop_duplicates(subset=['概况','小区名','所属地区','户型','面积','朝向','装潢','楼层高低','总楼层数','建筑类型','总价','单价','关注度','发布时间','图片地址'])
df = df[df['总楼层数'] != '未知数据']
print(df['总楼层数'].value_counts())

df.to_excel("qingxi.xlsx", index=False)
