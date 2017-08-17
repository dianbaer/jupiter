# firstaio

[![Build Status](https://travis-ci.org/dianbaer/firstaio.svg?branch=master)](https://travis-ci.org/dianbaer/firstaio)

FirstAIO一款异步IO的Web框架，使用FirstAIO开发者可以快速的开发高并发的Web项目。

FirstAIO包含：配置、异步IO-ORM、注解、日志、模板、异步IO-Http等功能。


依赖：

	jinja2
		jinja2 markupsafe
		
		Jinja2-2.9.6-py2.py3-none-any.whl
		MarkupSafe-1.0.tar.gz
	aiohttp
		aiohttp async_timeout chardet multidict yarl
		
		aiohttp-2.2.5-cp36-cp36m-win_amd64.whl
		async_timeout-1.2.1-py3-none-any.whl
		yarl-0.12.0-cp36-cp36m-win_amd64.whl
		multidict-3.1.3-cp36-cp36m-win_amd64.whl
		chardet-3.0.4-py2.py3-none-any.whl
	aiomysql
		aiomysql pymysql
		
		aiomysql-0.0.9.tar.gz
		PyMySQL-0.7.11-py2.py3-none-any.whl
	

推荐环境：

	MariaDB-10.1.22

	CentOS-7-1611
	
	Python3.6


快速开始(example\firstaio-example)：

	1、将firstaio文件夹考入项目根目录或者Python第三方插件目录site-packages
	
	2、ConfigOverride.py：

		配置文件，配置数据库与http相关参数

	3、main.py：

		运行文件
		
	4、handler文件夹：

		解析http相关注解的处理函数
		
	5、static文件夹：
		
		http静态内容文件夹
		
	6、templates文件夹：

		模板文件夹（基于jinja2）
		
	7、model文件夹：

		ORM映射类文件夹

	8、执行指令：

		python main.py
	
	9、注册服务：
		
		执行registerervice.sh
		
		包含文件
		firstaioexample.service
		registerervice.sh
		startservice.sh
	
