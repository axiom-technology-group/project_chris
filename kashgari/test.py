import kashgari
import tensorflow
import tqdm
import keras
from kashgari.tasks.classification import CNNModel
import  jieba
from kashgari.utils import load_model
x=[]
# new_model = CNNModel.get_default_hyper_parameters('./model_cnn')
new_model=load_model('topic_bigru')
news=['耗油好多啊']
# y=jieba.cut((news[0]),cut_all=False)
x.append(news)

# print(x)
q=new_model.predict(x)
print(q)