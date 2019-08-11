from kashgari.corpus import ChineseDailyNerCorpus
from kashgari.tasks.labeling import BiLSTM_CRF_Model

# 加载内置数据集，此处可以替换成自己的数据集，保证格式一致即可
train_x, train_y = ChineseDailyNerCorpus.load_data('train')
test_x, test_y = ChineseDailyNerCorpus.load_data('test')
valid_x, valid_y = ChineseDailyNerCorpus.load_data('valid')



import kashgari
from kashgari.tasks.labeling import BiLSTM_Model
from kashgari.embeddings import BERTEmbedding

bert_embed = BERTEmbedding('baidu_ernie',
                           task=kashgari.LABELING,
                           sequence_length=100)
model = BiLSTM_Model(bert_embed)
model.fit(train_x, train_y, valid_x, valid_y)