创建一个scrapy项目：scrapy startpreject + 项目名

创建一个new spider： scrapy genspider +名称 +url地址

scrapy shell应用命令：

{

	进入shell命令菜单：scrapy shell + url

	用response定位信息：response.css(".class").extract()

	(备注：class中有空格要将空格改写成.)

	通过class提取里面的href：response.css(".class::attr(href)").extract()

	通过class提取里面的text:response.css(".class::text").extract()


}

