import jieba
import re
from zhon.hanzi import punctuation


# 去除标点符号
def deal(x):
    chi_nopuc = re.sub("[{}]+".format(punctuation), "", x)
    chi_token = jieba.lcut(chi_nopuc)
    f = open(r"data\stopwords.txt",'r',encoding = 'UTF-8')
    stopwords_n = f.readlines()
    f.close()
    #清洗停用词数据
    stopwords = [sw.strip().replace('\n','') for sw in stopwords_n]
    final = []
    for chi in chi_token:
        if chi not in stopwords:
            final.append(chi)
    return final

print(deal("text_chinese = '自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。自然语言处理是一门融语言学、计算机科学、数学于一体的科学。因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，所以它与语言学的研究有着密切的联系，但又有重要的区别。自然语言处理并不是一般地研究自然语言，而在于研制能有效地实现自然语言通信的计算机系统，特别是其中的软件系统。因而它是计算机科学的一部分。'"))