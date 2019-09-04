import codecs

f=codecs.open('show.html')
u=f.read()
f.close()
print(type(u))# <type 'unicode'>
f=codecs.open('test.html','a', encoding='UTF-8')
# 写入unicode
f.write(u)
# 写入str，自动进行解码编码操作
# GBK编码的str

# 这里会先将GBK编码的str解码为unicode再编码为UTF-8写入
f.close()