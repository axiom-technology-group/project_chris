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

test_x, test_y = read_data_file('topic_data/test.txt')
train_x, train_y = read_data_file('topic_data/train.txt')
val_x, val_y = read_data_file('topic_data/dev.txt')

# 初始化 word2vec embedding

import kashgari
# 初始化 word2vec embedding
from kashgari.embeddings import WordEmbedding

from kashgari.embeddings import GPT2Embedding
from kashgari.tasks.classification import BiLSTM_Model
#lstm-acc: 0.8291
embed = GPT2Embedding('GPT-2',
                           task=kashgari.CLASSIFICATION,
                           sequence_length=100)
model =BiLSTM_Model(embed)
# 初始化 BERT embedding
# from kashgari.embeddings import BERTEmbedding
# # embedding = BERTEmbedding('bert-base-chinese', sequence_length=600)
# #
# # # 使用 embedding 初始化模型
# # from kashgari.tasks.classification import CNNModel
# # model = CNNModel(embedding)


model.fit(train_x, train_y, val_x, val_y, batch_size=16,epochs=5)
model.evaluate(test_x, test_y)
model.save('./topic_gpt-2+bilstm')

