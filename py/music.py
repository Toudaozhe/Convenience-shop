import bs4,sys,urllib.request,json,requests,re,base64
method = json.loads(sys.argv[1])

class music:
  name = 'xilou'
  id_name = 1
  def __init__(self,name,id_name):
        self.name = name
        self.id_name = id_name
  def music_name(self):	
        url = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery191034642999175022426_1489023388639&keyword=%s&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641'%(self.name)
        headers = {
                'Host': 'songsearch.kugou.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://www.kugou.com/yy/html/search.html',
                'Cookie': 'kg_mid=3af81d5237db90c04a517a5dc12ef8ee; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1497918589; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1497934809',
                'Connection': 'keep-alive'
            }
        r = requests.get(url,headers = headers )
        response = r.text
        matchObj = re.search( r'jQuery191034642999175022426_1489023388639(.*)', response, re.M|re.I)
        content = matchObj.group(1).strip('()')
        content = json.loads(content)
        for i in range(0,10):
          try:
             html =  '''<div class= 'music'>
				  <a  href = '/index.php/music/music_audio?name=%s'>%s</a>
				<span> %s </span>
			</div>
			'''%(content["data"]["lists"][i]["FileHash"],content["data"]["lists"][i]["SongName"],content["data"]["lists"][i]["SingerName"])
             print(html)
          except:
            
             pass
	   
	                
	     
  def song_name(self):
        url = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery191034642999175022426_1489023388639&keyword=%s&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641'%(self.name)
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
          }
        r = requests.get(url,headers = headers )
        response = r.text
        matchObj = re.search( r'jQuery191034642999175022426_1489023388639(.*)', response, re.M|re.I)
        content = matchObj.group(1).strip('()')
        content = json.loads(content)
        url_parse =  'http://www.kugou.com/yy/index.php?r=play/getdata&hash='+ content["data"]["lists"][0]["FileHash"]
        r_parse = requests.get(url_parse,headers=headers)
        response = json.loads(r_parse.text)
        data =  '''
        <div id='jpg_div'>
              
            <img id='jpg' src="%s"/>
        
		
        <div id="audio_name">%s
        </div>
         
	<div id='geci'>%s</div>
        <div id ="play">
            <div id='audio' >%s</div>
        </div>
        </div>
        '''%(base64.b64encode(response['data']['img'].encode('utf8')),response['data']['audio_name'],base64.b64encode(response['data']['lyrics'].encode('utf8')),base64.b64encode(response['data']['play_url'].encode('utf8')))
        try:      
          print(data)
        except:
          pass
        
      
  def song(self):
        array_json = "44D1C80714260F96C902D0A4599D6B32"
        url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash='+self.id_name
        headers = {
                'Host': 'www.kugou.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'Cookie': 'kg_mid=3af81d5237db90c04a517a5dc12ef8ee; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1497918589; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1497934809',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                
            }
        r = requests.get(url,headers = headers )
        response = json.loads(r.text)
        data = '''
        <div id='jpg_div'>
              
            <img id='jpg' src="%s"/>
        
		
        <div id="audio_name">%s
        </div>
         
	<div id='geci'>%s</div>
        <div id ="play">
            <div id='audio' >%s</div>
        </div>
        </div>
        '''%(base64.b64encode(response['data']['img'].encode('utf8')),response['data']['audio_name'],base64.b64encode(response['data']['lyrics'].encode('utf8')),base64.b64encode(response['data']['play_url'].encode('utf8')))
        try:      
          print(data)
        except:
          pass
  
if method['method'] == 'sousuo':
    music(method['song_name'],0).music_name()
elif method['method'] == 'audio':
    music(0,method['song_id']).song()
elif method['method'] == 'song_name':
    music(method['song_name'],0).song_name()         

