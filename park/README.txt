任务：获取公园数据

一、文件说明
1.getparklist.py文件
根据高德地图开发API，输入要查找的城市，生成对应的URL，爬取到公园的相关数据，具体数据内容参考https://lbs.amap.com/api/webservice/guide/api/search/，筛选出有评分、入口和具体地址的公园，将公园的信息保存在./parkdata文件夹中对应城市的txt文件里。

2.getparkdetail.py文件
控制谷歌chrome浏览器，获取公园的具体信息，URL=“https://www.amap.com/detail/get/detail?id=”，id是保存在parkdata/XX.txt中，获取到公园的具体信息，在parkdetail/XX/BXX.html保存为html网页格式。需要使用控件chromedriver。

二、安装使用说明
windows+python3.5
依赖包：selenium urllib bs4 html5lib json
控件：chromedriver.exe

运行说明：
1.python getparklist.py
2.打开chrome浏览器安装位置，默认位置C:\Program Files (x86)\Google\Chrome\Application，然后右键CMD。输入命令：chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"；运行python getparkdetail.py。

