## 此项目包含爬虫部分和数据建模部分，webcrawler为爬虫部分，其余为模型部分。
### NewsTopicAnalysis为TEXTCNN预测新闻主题，sentiment_CNN为汽车评论情感分析，topicanalysis为基于TEXTCNN汽车评论主题预测，paddlehub为利用paddlepaddle框架以及百度自建数据集进行文本分类，kashgari为迁移学习代码，keras_pretrained_bert为利用keras的预训练bert模型进行主题预测，修改自https://github.com/real-brilliant/bert_chinese_pytorch 以及 https://github.com/liuyijiang1994/bert_senta 感谢以上两位作者！
+ 爬虫使用了scrapy框架，配合selenium、随机UA/IP池等反爬手段，爬取了51auto.com等十余个汽车网站，并将数据存至数据库，已经将命令写入main.py函数，运行时只需要在里面第三个参数表明运行哪个爬虫，然后run一下即可，无需在命令行中多次输入
##  数据分析目前运用jieba分词和Word2Vector对文本进行预处理，然后进行情感分析，采用算法进行情感预测，同时做了关键词提取等工作,。
+ 深度学习采用了CNN/BERT/BILSTM等算法进行文本分类任务，分别使用tensorflow以及百度paddlehub进行预测，在百度自建数据集的预训练模型中效果最好。
+ 同时采用了kashigari迁移学习进行预测，在准确度上做了进一步提升，THUCNews新闻长文本主题分类CNN准确度达到了97%，BILSTM+BERT达到了98%，同时支持采用最新ERNIE和哈工大讯飞推出的BERT预训练模型预测，其余预训练模型模型方面有GPT-2/词袋模型等，模型支持LSTM/GRU/BILSTM/BIGRU/CNN/RCNN等
## 后续会更新预训练模型以及部分踩坑指南（hhh），以供后续的开发者使用
+  数据集链接：https://github.com/InsaneLife/ChineseNLPCorpus
+  预训练模型链接：https://blog.csdn.net/xinshucredit/article/details/89381109      https://blog.csdn.net/weixin_33842304/article/details/88004178

## 目前在尝试知识图谱构建、可视化等工作，目前尝试了使用protege构建RDF数据，并使用apache-jena-fukesi作为服务器实现问答机器人功能，同时还实现了知识图谱的可视化，目前在尝试neo4j，后续会进行代码更新。未来目标：基于知识图谱的推荐系统->基于xxxx与知识图谱融合的推荐系统
