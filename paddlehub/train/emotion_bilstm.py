import paddlehub as hub
import pandas as pd
import numpy as np
data = pd.read_excel('data/chengdu_reviews_end.xlsx')
data1=data.iloc[0:50000,3]
test_text = [""]
data2 = np.array(data1).astype(str).tolist()  #
print(data2)
module = hub.Module(name="senta_bilstm")
input_dict = {"text": data2}
results = module.sentiment_classify(data=input_dict)
df = pd.DataFrame(results)

# 保存到本地excel
df.to_excel("predict/chengdu_reviews_bilstm.xlsx", index=False)
# for result in results:
#     print(result['text'])
#     print(result['sentiment_label'])
#     print(result['sentiment_key'])
#     print(result['positive_probs'])
#     print(result['negative_probs'])