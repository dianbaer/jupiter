# firstaio

FirstAIO一款异步IO的Web框架，使用FirstAIO开发者可以快速的开发高并发的Web项目。

FirstAIO包含：配置、异步IO-ORM、注解、日志、模板、异步IO-Http等功能。


FirstAIO依赖：

	Python3.5+
	
	aiohttp-2.2.5
	
	aiomysql-0.0.9
	
	jinja2-2.9.6


快速开始(example\firstaio-example)：

	1、ConfigOverride.py：

		配置文件，配置数据库与http相关参数

	2、main.py：

		运行文件
		
	3、handler文件夹：

		解析http相关注解的处理函数
		
	4、static文件夹：
		
		http静态内容文件夹
		
	5、templates文件夹：

		模板文件夹（基于jinja2）
		
	6、model文件夹：

		ORM映射类文件夹

	
运行，执行指令：

	python main.py
