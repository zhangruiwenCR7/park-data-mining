���񣺻�ȡ��԰����

һ���ļ�˵��
1.getparklist.py�ļ�
���ݸߵµ�ͼ����API������Ҫ���ҵĳ��У����ɶ�Ӧ��URL����ȡ����԰��������ݣ������������ݲο�https://lbs.amap.com/api/webservice/guide/api/search/��ɸѡ�������֡���ں;����ַ�Ĺ�԰������԰����Ϣ������./parkdata�ļ����ж�Ӧ���е�txt�ļ��

2.getparkdetail.py�ļ�
���ƹȸ�chrome���������ȡ��԰�ľ�����Ϣ��URL=��https://www.amap.com/detail/get/detail?id=����id�Ǳ�����parkdata/XX.txt�У���ȡ����԰�ľ�����Ϣ����parkdetail/XX/BXX.html����Ϊhtml��ҳ��ʽ����Ҫʹ�ÿؼ�chromedriver��

������װʹ��˵��
windows+python3.5
��������selenium urllib bs4 html5lib json
�ؼ���chromedriver.exe

����˵����
1.python getparklist.py
2.��chrome�������װλ�ã�Ĭ��λ��C:\Program Files (x86)\Google\Chrome\Application��Ȼ���Ҽ�CMD���������chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"������python getparkdetail.py��

