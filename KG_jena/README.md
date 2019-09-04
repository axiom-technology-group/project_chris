## 首先，本系统运行在python3环境下，并且需要安装jieba、rerfo等python库。此外，还应当下载apache-jena和apache-jena-fuseki。本系统运行在apache-jena-fuseki服务器上，在cmd窗口进入apache-jena-fuseki文件输入命令./fuseki-server.bat或在文件夹下双击fuseki-server.bat文件，cmd窗口出现“Server  INFO  Started 2019/03/12 21:13:30 CST on port 3030”即表示服务器运行成功，在浏览器输入localhost:3030即可显示页面。
## 这里apache-jena的主要作用就是使用文件夹中的tdb-loader.bat文件将RDF文件转换成tdb文件，命令格式为：.\tdbloader.bat --loc="D:\tdb" "D:\kg_demo_movie.nt"，--loc参数为生成的tdb文件的文件夹，第二个参数是格式为nt的RDF文件，如果使用protege生成RDF文件，则后缀名为owl，这里可以直接修改文件的后缀名将owl文件转换成nt文件。在D:\apache-jena-fuseki-3.10.0\run\configuration文件下建立fuseki_conf.ttl文件，该文件主要有两个作用，一个是指定tdb文件的位置，另一个是对生成的数据库进行命名，完成转换tdb文件和配置完fuseki_conf.ttl文件后，执行第二段的fuseki-server.bat并打开localhost:3030后应该可以看到服务器上生成的数据库，并可以在该平台上进行SPARQL语句查询。
## 构建owl图谱文件可以使用Protégé ，具体见 https://protege.stanford.edu/products.php#desktop-protege。
## 最后是自然语言处理环节，python通过结巴分词，规则匹配将相应的自然语言转换成SPARQL查询语句，并通过和fuseki通信得到查询结果后通过结果的解析得到最后的答案形式。


