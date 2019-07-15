# -*- coding:utf-8 -*-
import json
import time
import urllib
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup
import html5lib

#citylist=['北京','上海','南京','深圳']
citylist=['北京']
AMAP_API_KEY = "6a37f08a862115f828b0cf217fdcd231" #高德地图密匙
urlParamJson = {
    #'city' : city,
    'output' : 'xml',
    'key' : AMAP_API_KEY,
    'keywords' : '公园',
    'citylimit' : 'true', #只返回指定城市数据
    'offset' : '20',#每页条数
    'extensions' : 'all'
}
MAX_PAGE = 50 #最大页数

def getParkPoiid(city):
    poiidList = []
    for page in range(1,MAX_PAGE) : #页数
        urlParamJson["page"] = page
        urlParamJson["city"] = city
        params = urllib.parse.urlencode(urlParamJson)
        
        url = "http://restapi.amap.com/v3/place/text?%s" % params
        print(city, "当前 %s 页..." % page)
        http = urllib.request.urlopen(url)
        dom = BeautifulSoup(http,"html5lib")
        poiList = dom.findAll("poi")
        
        if len(poiList)==0: #没有数据时则跳出
            break
        for poi in poiList:
            if poi.biz_ext.rating.get_text() != '' and poi.address.get_text() != '' and poi.entr_location.get_text() != '':
                poiid = poi.id.get_text()
                poiidList.append(poiid.encode("utf8"))
                with open(city+'.txt','a') as f:    #设置文件对象
                    f.write(poi.id.get_text()+'\t')
                    f.write(poi.find('name').get_text()+'\t')
                    f.write(poi.location.get_text()+'\t')
                    f.write(poi.biz_ext.rating.get_text()+'\t')
                    f.write(poi.biz_ext.cost.get_text()+'\t')
                    f.write(poi.entr_location.get_text()+'\t')
                    #f.write(poi.exit_location.get_text()+'\t')
                    f.write(poi.pname.get_text()+'\t')
                    f.write(poi.cityname.get_text()+'\t')
                    f.write(poi.adname.get_text()+'\t')
                    f.write(poi.address.get_text()+'\t')
                    f.write(area+'\t')   
                    f.write(shape+'\r')      
    return poiidList


if __name__ == '__main__':
    for c in citylist:
        poiidList = getParkPoiid(c) #得到公园id
        print(c+"已得到 %s 个公园POI ID" %(len(poiidList)))