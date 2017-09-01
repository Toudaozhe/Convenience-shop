import requests,bs4,lxml,os,json,sys,json,urllib.request

array_json = json.loads(sys.argv[1])

path = os.getcwd()
url = 'http://fanyi.baidu.com/v2transapi'

language_dict = {"日本":"jp","俄国":"ru","韩国":"kor","中国":"zh","繁体":"cht","英语":"en"}

from_data = language_dict[array_json['country_src']]
to_data = language_dict[array_json['country_des']]

conntect_data = urllib.request.quote(array_json['fanyi_src'])

data = 'from='+from_data+'&to='+to_data +'&query='+conntect_data+'&transtype=realtime&simple_means_flag=3'
headers = {
           'Host': 'fanyi.baidu.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
          
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'http://fanyi.baidu.com/',

           'Connection': 'keep-alive'}
 
r = requests.post(url,headers = headers ,data = data)
response = r.text
content = json.loads(response)
try:
   
    print(content['trans_result']['data'][0]['dst'])
   
except:
    print('')


