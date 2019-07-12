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
        import requests
        cookies_str = "guid=e420-0e8a-e642-52dd; UM_distinctid=16b93f002ee2c-098d80bc665fd1-3a65420e-121886-16b93f002ef4d; dev_help=gjXPnoSKjmBfnmbHzpc%2FR2VmNjQ3Njc3Yjc3NTVmM2NlYjIzYjZmOGI1YzgzMDk1ODc1N2I1NTBhOTVmYmM1NTgzYzY0OWQ0ZmQ2ZDQ3YzkuCsOFQJOsYe5fXvjXlMfmZnRT7r59cLBUin2b%2BUN9rJLN53MJlQq2hjQs35lh3X5ZOcqh%2BpcQ8btsooAaoCTVqG%2FEs%2BbGphfN1DYR2YuR7oXVI4EedM9zUmRzq1h9ZhY%3D; cna=YVLnE30SIiECAbe9Y6Tkilbk; _uab_collina=156155638102756661875732; key=bfe31f4e0fb231d29e1d3ce951e2c780; x-csrf-token=68d432f27258df9a10ea37587c165791; x5sec=7b22617365727665723b32223a226464653532353837333630663931303331393631353635313835373232316637434c482b674f6b46454f2b6c676276637949766755673d3d227d; CNZZDATA1255626299=995970047-1561553975-https%253A%252F%252Fwww.baidu.com%252F%7C1562394054; l=bBg8LOmrqTqtd4HFBOfgCDpLkxyUgIRb8sPr9_Mh5ICPOq1p5avNWZnYVB89C3NVa6n6R3u14VQUBSLEfyzHh; isg=BLy8yEujzW_XCvkAM7E2FYv1jVrZGCalpsZjPpY9UaeKYV3rvsSPbv3XQcm_KZg3" 
        cookies_dict = {} 
        for cookie in cookies_str.split(";"): 
            k, v = cookie.split("=", 1) 
            cookies_dict[k.strip()] = v.strip() 
        header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Cookie': 'guid=e420-0e8a-e642-52dd; \
                    UM_distinctid=16b93f002ee2c-098d80bc665fd1-3a65420e-121886-16b93f002ef4d; \
                    dev_help=gjXPnoSKjmBfnmbHzpc%2FR2VmNjQ3Njc3Yjc3NTVmM2NlYjIzYjZmOGI1YzgzMDk1ODc1N2I1NTBhOTVmYmM1NTgzYzY0OWQ0ZmQ2ZDQ3YzkuCsOFQJOsYe5fXvjXlMfmZnRT7r59cLBUin2b%2BUN9rJLN53MJlQq2hjQs35lh3X5ZOcqh%2BpcQ8btsooAaoCTVqG%2FEs%2BbGphfN1DYR2YuR7oXVI4EedM9zUmRzq1h9ZhY%3D; \
                    cna=YVLnE30SIiECAbe9Y6Tkilbk; \
                    _uab_collina=156155638102756661875732; \
                    key=bfe31f4e0fb231d29e1d3ce951e2c780; \
                    x-csrf-token=68d432f27258df9a10ea37587c165791; \
                    x5sec=7b22617365727665723b32223a226464653532353837333630663931303331393631353635313835373232316637434c482b674f6b46454f2b6c676276637949766755673d3d227d; \
                    CNZZDATA1255626299=995970047-1561553975-https%253A%252F%252Fwww.baidu.com%252F%7C1562394054; \
                    l=bBg8LOmrqTqtd4HFBOfgCDpLkxyUgIRb8sPr9_Mh5ICPOq1p5avNWZnYVB89C3NVa6n6R3u14VQUBSLEfyzHh; \
                    isg=BLy8yEujzW_XCvkAM7E2FYv1jVrZGCalpsZjPpY9UaeKYV3rvsSPbv3XQcm_KZg3',
            'amapuuid': '04651b83-b995-41a3-82fc-0fd2a64131d5',
            'Connection': 'keep-alive',
            'Host': 'www.amap.com',

            }
        if len(poiList)==0: #没有数据时则跳出
            break
        for poi in poiList:
            if poi.biz_ext.rating.get_text() != '' and poi.address.get_text() != '' and poi.entr_location.get_text() != '':
                poiid = poi.id.get_text()
                poiidList.append(poiid.encode("utf8"))
                header['Referer']='https://www.amap.com/place/'+poiid
                url = "http://www.amap.com/detail/get/detail?%s" % urllib.parse.urlencode({'id' : poiid})
                f = urllib.request.urlretrieve(url,'test.html')
                req=urllib.request.Request(url, headers=header)
                #req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
                #req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
                #req.add_header('Accept-Encoding', 'gzip, deflate, br')
                #req.add_header('Cookie', 'guid=e420-0e8a-e642-52dd; UM_distinctid=16b93f002ee2c-098d80bc665fd1-3a65420e-121886-16b93f002ef4d; dev_help=gjXPnoSKjmBfnmbHzpc%2FR2VmNjQ3Njc3Yjc3NTVmM2NlYjIzYjZmOGI1YzgzMDk1ODc1N2I1NTBhOTVmYmM1NTgzYzY0OWQ0ZmQ2ZDQ3YzkuCsOFQJOsYe5fXvjXlMfmZnRT7r59cLBUin2b%2BUN9rJLN53MJlQq2hjQs35lh3X5ZOcqh%2BpcQ8btsooAaoCTVqG%2FEs%2BbGphfN1DYR2YuR7oXVI4EedM9zUmRzq1h9ZhY%3D; cna=YVLnE30SIiECAbe9Y6Tkilbk; _uab_collina=156155638102756661875732; key=bfe31f4e0fb231d29e1d3ce951e2c780; x-csrf-token=68d432f27258df9a10ea37587c165791; x5sec=7b22617365727665723b32223a226464653532353837333630663931303331393631353635313835373232316637434c482b674f6b46454f2b6c676276637949766755673d3d227d; CNZZDATA1255626299=995970047-1561553975-https%253A%252F%252Fwww.baidu.com%252F%7C1562394054; l=bBg8LOmrqTqtd4HFBOfgCDpLkxyUgIRb8sPr9_Mh5ICPOq1p5avNWZnYVB89C3NVa6n6R3u14VQUBSLEfyzHh; isg=BLy8yEujzW_XCvkAM7E2FYv1jVrZGCalpsZjPpY9UaeKYV3rvsSPbv3XQcm_KZg3')
                #req.add_header('Referer', 'https://www.amap.com/place/'+poiid)
                http = request.urlopen(req)
                jsonStr = http.read().decode('utf-8')

                # page = requests.get(url=url,cookies=cookies_dict,headers=header)
                # time.sleep(5)
                # print(page.text)
                # json_1 = json.loads(page.text)
                # print(json_1)
                
                print(url)
                print(jsonStr)
                park = json.loads(jsonStr)
                print(park)
                spec = park["status"]["spec"]
                for key in spec:
                    if key=="mining_shape":  #有 面状或线状 信息
                        shape = spec[key]["shape"]
                        area =  spec[key]['area']

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
