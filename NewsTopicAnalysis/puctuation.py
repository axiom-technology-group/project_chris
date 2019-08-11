import jieba
novel = open('./data/out.txt','r',encoding='utf-8')
content=novel.read()
novel_segmented = open('./data/out.txt','w',encoding='utf-8')

cutword = jieba.cut(content,cut_all=False)
seg = ''.join(content).replace('。','').replace('“','').replace('”','').replace('：','').replace('…','')\
            .replace('!','').replace('？','').replace('~','').replace('（','').replace('）','').replace('、','').replace('；','') .replace('！','').replace('，','').replace('"','').replace(',','')\
            .replace("每","").replace("ㄜ","").replace("＊","").replace("谷","").replace("㏒","").replace("＆","").replace("?","")
print(seg,file=novel_segmented)
novel.close()
novel_segmented.close()


