path="D:\coding\SentimentAnalysis-master\data\ch_auto_train.txt"
with open(path, encoding='utf-8') as f:
    i=0
    for line in f.readlines():
        i=i+1
        print(i)
        sp = line.strip().split()
        label = sp[0]
        print(label)
