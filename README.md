一天爬虫学习日记

学的是最简单的scrapy，有这么好用的工具干嘛不用呢哈哈

爬虫的基本思路：
1、首先给定入口start_urls
2、爬下一级的入口
3、在目标页面爬取所需要的数据

在定义一个spider(crawlspider）类之后，首先给定start_urls
然后就可以开始写回调函数了
一般是写成
def parse(self,response)
函数里面写上请求，可以用一个yield的生成器,request里的callback对于不同层级的页面应该不同
在最终的需要爬取的页面用items存起来，items需要事先在上一级文件里编写好格式
具体提取数据的方法我用的是xpath，对于学校的bbs是挺好用的

最后可以在运行时写入csv文档
scrapy crawl xxxx -o xxx.csv
