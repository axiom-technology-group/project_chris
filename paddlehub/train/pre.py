filepath = r'D:\coding\fenci\train\data\langyi.csv'

import pandas as pd

data = pd.read_csv(open(filepath, encoding='utf8'), sep=',')
data.head()
#
# data_title_dep = data["waiguan", "Edep"].copy()#复制到新的地址，不破坏原始数据
# data_title_dep["title_dep"] = data_title_dep["Etitle"]+data_title_dep["Edep"]
# data_title_dep.head()

data_dep=data["waiguan"].copy()
data_dep.head()
import jieba

# data.loc[:, ['Etitle', 'Edep']]
output = open("res_dep.txt", "w", encoding='utf8')
stopwords_path = r"D:\coding\fenci\train\data\stopwords.txt"

stop_list = []
with open(stopwords_path, "r", encoding="utf-8") as f:
    for line in f.readlines():
        stop_list.append(line.replace("  \n", ""))

count = 0
for index, row in data_dep.iterrows():
    words = jieba.cut(row['waiguan'])
    for word in words:
        # print(word)
        if word not in stop_list:
            output.write(word + " ")
        else:
            print(word)
    output.write('\n')
    count += 1
    if count == 5:
        output.close()
        break
