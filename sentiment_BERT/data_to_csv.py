import json
import pandas as pd
from collections import Counter

# confidence_gate = 0.7
# result_cont = 0
label = []
text = []
with open('data/test.txt', 'r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        ob = json.loads(line)
        for su in ob:
            label.append(su['label'])
            text.append(su['text'].replace(' ,', '，'))

save = pd.DataFrame({'label': label, 'text': text})
save.to_csv('data/end.csv', index=False, sep=',')
count = Counter(label)
print(count)
