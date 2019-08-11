import os
import time
from datetime import timedelta
import numpy as np
from collections import Counter
import tensorflow.contrib.keras as kr
from CONFIG import CONFIG
from utils import load_word2id, load_corpus_word2vec


def cat_to_id(classes=None):
    """
    :param classes: 分类标签；默认为pos, neg
    :return: {分类标签：id}
    """
    if not classes:
        classes = ['pos', 'neg']
    cat2id = {cat: idx for (idx, cat) in enumerate(classes)}
    return classes, cat2id


def load_corpus(path, word2id, max_sen_len=50):
    """
    :param path: 样本语料库的文件
    :return: 文本内容contents，以及分类标签labels(onehot形式)
    """
    _, cat2id = cat_to_id()
    contents, labels = [], []
    with open(path, encoding='utf-8') as f:
        for line in f.readlines():
            sp = line.strip().split()
            label = sp[0]
            content = [word2id.get(w, 0) for w in sp[1:]]
            content = content[:max_sen_len]
            if len(content) < max_sen_len:
                content += [word2id['_PAD_']] * (max_sen_len - len(content))
            labels.append(label)
            contents.append(content)
    counter = Counter(labels)
    print('总样本数为：%d' % (len(labels)))
    print('各个类别样本数如下：')
    for w in counter:
        print(w, counter[w])

    contents = np.asarray(contents)
    i=0
    for l in labels:
        i=i+1
        print(i)
        labels = cat2id[l]
    labels = kr.utils.to_categorical(labels, len(cat2id))

    return contents, labels

config = CONFIG()
word2id = load_word2id(config.word2id_path)
load_corpus(config.train_path, word2id, max_sen_len=config.max_sen_len)
