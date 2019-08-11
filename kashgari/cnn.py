import tqdm
import jieba

def read_data_file(path):
    lines = open(path, 'r', encoding='utf-8').read().splitlines()
    x_list = []
    y_list = []
    for line in tqdm.tqdm(lines):
        rows = line.split('\t')
        if len(rows) >= 2:
            y_list.append(rows[0])
            x_list.append(list(jieba.cut('\t'.join(rows[1:]))))
        else:
            print(rows)
    return x_list, y_list

test_x, test_y = read_data_file('cnews/cnews.test.txt')
train_x, train_y = read_data_file('cnews/cnews.train.txt')
val_x, val_y = read_data_file('cnews/cnews.val.txt')

# 初始化 word2vec embedding

import kashgari
# 初始化 word2vec embedding
from kashgari.embeddings import WordEmbedding


from kashgari.tasks.classification import CNNModel
model = CNNModel()
# 初始化 BERT embedding
# from kashgari.embeddings import BERTEmbedding
# # embedding = BERTEmbedding('bert-base-chinese', sequence_length=600)
# #
# # # 使用 embedding 初始化模型
# # from kashgari.tasks.classification import CNNModel
# # model = CNNModel(embedding)


model.fit(train_x, train_y, val_x, val_y, batch_size=128)
model.evaluate(test_x, test_y)
model.save('./model_cnn')

