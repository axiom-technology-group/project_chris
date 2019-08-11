import jieba
novel = open('./pretreatment/out.txt','r',encoding='utf-8')
content=novel.read()
novel_segmented = open('./data/out.txt','w',encoding='utf-8')

cutword = jieba.cut(content,cut_all=False)
seg = ' '.join(cutword).replace('。','').replace('“','').replace('”','').replace('：','').replace('…','')\
            .replace('!','').replace('？','').replace('~','').replace('（','').replace('）','').replace('、','').replace('；','') .replace('！','').replace('，','').replace('"','').replace(',','')
print(seg,file=novel_segmented)
novel.close()
novel_segmented.close()


