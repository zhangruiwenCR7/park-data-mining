from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
browser.implicitly_wait(10)
city='西安'
filename = 'C:\document\王思博课题\park\parkdata\\'+city+'.txt'
print(filename)
with open(filename, encoding="utf8") as f:
    for line in f.readlines():
        line=line.split()
        id = line[0]
        browser.get('https://www.amap.com/detail/get/detail?id='+id)
        time.sleep(3)
        f = open('C:\document\王思博课题\park\parkdetail\\'+city+'\\'+id+'.html','wb')
        f.write(browser.page_source.encode("gbk", "ignore")) # 忽略非法字符
        f.close()   

# chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--start-maximized")
#browser = webdriver.Chrome()
#browser = webdriver.Edge(executable_path="MicrosoftWebDriver.exe")
# browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
# browser.implicitly_wait(10)
# browser.get('https://www.amap.com/')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# time.sleep(1)
# browser.get('https://www.amap.com/place/B000A7I1OL')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[2])
# time.sleep(1)

# browser.get('https://www.amap.com/detail/get/detail?id=B000A7I1OL')
# time.sleep(3)
# print(browser.title)
# f = open(browser.title+'.html','wb')
# f.write(browser.page_source.encode("gbk", "ignore")) # 忽略非法字符
# f.close()   
# html = browser.page_source
# print(html.text)
#browser.close()
# register = browser.find_element_by_name("shape")
# print(register)
# results = parse_html(html)
# print(results)