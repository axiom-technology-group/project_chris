import paddlehub as hub
import pandas as pd
import numpy as np
data = pd.read_table('data/all2.txt',encoding='utf-8',delim_whitespace=True,error_bad_lines=False )
data1=data.iloc[1:,0]
data2 = np.array(data1).astype(str).tolist()  #
module = hub.Module(name="emotion_detection_textcnn")
# test_text = ["今天天气真好", "湿纸巾是干垃圾", "别来吵我"]
input_dict = {"text": data2}
results = module.emotion_classify(data=input_dict)
df = pd.DataFrame(results)

# 保存到本地excel
df.to_excel("predict/emotion_textcnn.xlsx", index=False)
for result in results:
    print(result['text'])
    print(result['emotion_label'])
    print(result['emotion_key'])
    print(result['positive_probs'])
    print(result['negative_probs'])
    print(result['neutral_probs'])