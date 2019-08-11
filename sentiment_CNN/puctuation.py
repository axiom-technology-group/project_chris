import jieba
novel = open('./data/ch_auto_test.txt','r',encoding='GBK')
content=novel.read()
novel_segmented = open('./data/ch_auto_test.txt','w',encoding='utf-8')

# cutword = jieba.cut(content,cut_all=False,HMM="TRUE")
seg = ''.join(content).replace(',','').replace('。','').replace('“','').replace('”','').replace('：','').replace('…','')\
            .replace('!','').replace('？','').replace('~','').replace('（','').replace('）','').replace('、','').replace('；','') .replace('！','').replace('，','').replace('"','').replace(
'\t','').replace('neg','neg').replace('pos','pos')
print(seg,file=novel_segmented)

novel.close()
novel_segmented.close()

