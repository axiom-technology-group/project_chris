# coding:utf-8
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_table("./china_daily/test2.txt")
label = data['business']
# # 首先二等分
data_half_1, data_half_2, label_half_1, label_half_2 = \
    train_test_split(data, label, test_size=0.3, random_state=19970924)
#
# 第一个子集二等分
data_qua_1, data_qua_2, label_qua_1, label_qua_2 = \
    train_test_split(data_half_2, label_half_2, test_size=0.33, random_state=19931028)
#
# # 第二个子集二等分
# data_qua_3, data_qua_4, label_qua_3, label_qua_4 = \
#     train_test_split(data_half_2, label_half_2, test_size=0.5, random_state=19931028)
#
# print(data_half_1)
# # print(d)
data_half_1.to_csv('china_daily/train.csv', index=False) # part 1
data_qua_1.to_csv('china_daily/test.csv', index=False) # part 2
data_qua_2.to_csv('china_daily/dev.csv', index=False) # part 2
# data_qua_3.to_csv('test_part3.csv', index=False) # part 3
# data_qua_4.to_csv('test_part4.csv', index=False) # part 4