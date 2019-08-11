import jieba
novel = open('./data/all1.txt','r',encoding='utf-8')
content=novel.read()
novel_segmented = open('./data/all2.txt','w',encoding='utf-8')

# cutword = jieba.cut(content,cut_all=False)
# seg = ''.join(content).replace(',','').replace('。','').replace('“','').replace('”','').replace('：','').replace('…','')\
# #             .replace('!','').replace('？','').replace('~','').replace('（','').replace('）','').replace('、','').replace('；','') .replace('！','').replace('，','').replace('"','')\
# #             .replace('neg','').replace('pos','')
seg=''.join(content).replace(' ','')
print(seg,file=novel_segmented)

novel.close()
novel_segmented.close()

# import pandas as pd
# import numpy as np
# data = pd.read_table('data/cnews_train.txt',encoding='utf-8',delim_whitespace=True,error_bad_lines=False )
# data1=data.iloc[1:,1]
# data2 = np.array(data1).astype(str).tolist()  #
#header=None:没有每列的column name，可以自己设定
#encoding='gb2312':其他编码中文显示错误
#delim_whitespace=True:用空格来分隔每行的数据
#index_col=0:设置第1列数据作为index
