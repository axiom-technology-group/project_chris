import kashgari
import tensorflow
import tqdm
import keras
from kashgari.tasks.classification import CNNModel
import  jieba
from kashgari.utils import load_model
import tqdm
import jieba
import numpy as np
import pandas as pd
data_caijing = pd.read_csv('test_data/caijing.csv', encoding='utf-8',sep=',')
data_shizheng = pd.read_csv('test_data/shizheng.csv', encoding='utf-8',sep=',')
data_cj = data_caijing.iloc[:,4]
data_sz = data_caijing.iloc[:, 4]
data_cj1 = np.array(data_cj).astype(str).tolist()  #
data_xz1 = np.array(data_sz).astype(str).tolist()  #

# print(data_cj)
# cj_list=[]
# for cj in data_cj1:

# new_model = CNNModel.get_default_hyper_parameters('./model_cnn')


x1,x2=[],[]
new_model=load_model('model_cnn')
for cj in data_cj1:
    y=jieba.cut(cj,cut_all=False)
    x1.append(y)

for sz in data_xz1:
    y=jieba.cut(sz,cut_all=False)
    x2.append(y)
# print(x)
q=new_model.predict(x1)
w=new_model.predict(x2)
print(q)
df1 = pd.DataFrame(q,columns=['prediction'])
df2 = pd.DataFrame(w,columns=['prediction'])

data_re=pd.concat([data_caijing,df1], axis=1)
data_re2=pd.concat([data_shizheng,df2], axis=1)
data_re.to_csv('test_data/caijing.csv', mode='w',index=False)
data_re2.to_csv('test_data/shizheng.csv', mode='w',index=False)



