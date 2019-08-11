import paddlehub as hub
import pandas as pd
import numpy as np
data = pd.read_table('data/cnews_train.txt',encoding='utf-8',delim_whitespace=True,error_bad_lines=False )
data1=data.iloc[1:,1]
data2 = np.array(data1).astype(str).tolist()  #
#header=None:没有每列的column name，可以自己设定
#encoding='gb2312':其他编码中文显示错误
#delim_whitespace=True:用空格来分隔每行的数据
#index_col=0:设置第1列数据作为index

lac = hub.Module(name="lac")
# # test_text = ["今天是个好日子", "天气预报说今天要下雨", "下一班地铁马上就要到了"]
inputs = {"text": data2}
results = lac.lexical_analysis(data=inputs)
# seg = ' '.join(results).replace(',','').replace('。','').replace('“','').replace('”','').replace('：','').replace('…','').replace('!','').replace('？','').replace('~','').replace('（','').replace('）','').replace('、','').replace('；','') .replace('！','').replace('，','').replace('"','').replace("？",'')
df = pd.DataFrame(results)
df.to_csv('testcsv2.csv', mode='w', index=False)


