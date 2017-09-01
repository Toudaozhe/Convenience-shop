import bs4,requests,lxml,pymysql,json,sys,xml.dom.minidom
#array_json = json.loads(sys.argv[1])
contents_title_list = []
min_contents = []
hrefs_list = []
jpg_list = []
def mysql_query(xinwen_title,xinwen_jpg,xinwen_min_content,xinwei_content):#执行插入
   db = pymysql.connect('localhost','root','1993524','user_info',charset='utf8')
   cursor = db.cursor()#第四个变量改成超链接了，后期开发可以扩展
   xinwen_title = xinwen_title.replace("'",'"')
   
   
  #print (xinwen_title)
   sql = "insert into xinwen_dict (xinwen_title,xinwen_jpg,xinwen_min_content,xinwei_content)values('%s','%s','%s','%s')"%(xinwen_title,xinwen_jpg,xinwen_min_content,xinwei_content)
   
   try:
   
      cursor.execute(sql)
      db.commit()
   except:
      db.callback()
   
  
   db.close()
def mysql_del_query():#执行到点删除
   db = pymysql.connect('127.0.0.1','root','1993524','user_info',charset='utf8')
   cursor = db.cursor()
   sql = "delete from xinwen_dict"
   sql_xiaoshuo = "delete from xiaoshuo_dict"
   sql_yinyue = "delete from yinyue_dict"
   sql_tianqi = "delete from user_tianqi"
   try:
   
      cursor.execute(sql)
      db.commit()
   except:
      db.callback()
   try:
   
      cursor.execute(sql_xiaoshuo)
      db.commit()
   except:
      db.callback()
   try:
   
      cursor.execute(sql_yinyue)
      db.commit()
   except:
      db.callback()
   try:
   
      cursor.execute(sql_tianqi)
      db.commit()
   except:
      db.callback()
   
  
   db.close()
def mysql_xiaoshuo_query(xiaoshuo_content):#执行到点删除
   db = pymysql.connect('127.0.0.1','root','1993524','user_info',charset='utf8')
   cursor = db.cursor()
   sql = "insert into xiaoshuo_dict(xiaoshuo_content)values('%s')"%(xiaoshuo_content)
  
   try:
   
      cursor.execute(sql)
      db.commit()
   except:
      db.callback()
   
  
   db.close()
def mysql_music_query(yinyue_content):#执行到点删除
   db = pymysql.connect('127.0.0.1','root','1993524','user_info',charset='utf8')
   cursor = db.cursor()
  
   sql = "insert into yinyue_dict(yinyue_content)values('%s')"%(yinyue_content)
   try:
   
      cursor.execute(sql)
      db.commit()
   except:
      db.callback()
   
  
   db.close()
def mysql_tianqi_query(a):#执行到点删除
   db = pymysql.connect('127.0.0.1','root','1993524','user_info',charset='utf8')
   cursor = db.cursor()
  
   sql = "insert into user_tianqi(City,Tianqi,Tianqi1,Fengxiang,Wengdu,Wengdu1,Riqi)values('%s','%s','%s','%s','%s','%s','%s')"%(a.getElementsByTagName('city')[0].childNodes[0].data,a.getElementsByTagName('status1')[0].childNodes[0].data,a.getElementsByTagName('status2')[0].childNodes[0].data,a.getElementsByTagName('direction1')[0].childNodes[0].data,a.getElementsByTagName('temperature1')[0].childNodes[0].data,a.getElementsByTagName('temperature2')[0].childNodes[0].data,a.getElementsByTagName('savedate_weather')[0].childNodes[0].data)
  
   try:
   
      cursor.execute(sql)
      db.commit()
   except:
      db.callback()
   
  
   db.close()
def url_response(url):#封装http get请求
   headers = {
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'

      }
   r =requests.get(url,headers=headers)
   r.encoding = 'utf8'
   soup =bs4.BeautifulSoup(r.text,'lxml')
   return soup

def parse_titles_hrefs(soup):#bs4解析标题及超链接
   result = soup.select('.img')
   
   for i in range(len(result)):
      soup_result = bs4.BeautifulSoup(str(result[i]),'lxml')
      
      contents = soup_result.img['alt']
      #print(contents)
      hrefs =soup_result.a['href']
      contents_title_list.append(contents)#
      #print(contents)
      hrefs_list.append( hrefs)
def parse_titles_jpg(soup):#bs4解析图片
   result = soup.select('.img a img')
   for w in range(len(result)):
      soup_result = bs4.BeautifulSoup(str(result[w]),'lxml')
      jpg_list.append( soup_result.img['src'])
def parse_min_contents(soup):#bs4解析标题下简略内容
  
   result = soup.select('.brief2')
   for i in result:
      min_contents.append(i.get_text())
      
   
def parse_contents(soup):
    #弃用
   result = soup.select('.text')
   #print(str(result[0]))
def parse_xiaoshuo_shouye(soup):
   
   result = soup.select('.hot')
   result_replace = str(result[0]).replace('/html/','/index.php/novel/xiaoshuo_mulu?id=')
   result_replace_two = result_replace.replace("'",'"')
   result_replace_three = result_replace_two.replace("data-original",'src')
   return result_replace_three
def parse_music_shouye(soup):
   result = soup.select('.panel-songs-item-name span')
   string_full = ''
   for i in range(len(result)):
       string =  '''<div class="panel-songslist-item">
                   <a href ="/index.php/music/music_name?id=%s">
                    %s
                 </div>'''%(result[i].get_text(),result[i])
       string_full = string_full+string
   return string_full
  
   
def place_hrefs_list(hrefs_list):#扩展xinwen_content的超链接，暂不开发
   return hrefs_list.replace('http://news.jschina.com.cn/','')



mysql_del_query()#执行到点删除
url = 'http://www.jnwb.net' 
url_tianqi = 'http://php.weather.sina.com.cn/xml.php?city=%ce%de%ce%fd&password=DJOYnieT8234jlsK&day=0'

parse_titles_hrefs(url_response(url))
parse_titles_jpg(url_response(url))
parse_min_contents(url_response(url))
mysql_xiaoshuo_query(parse_xiaoshuo_shouye(url_response('http://m.23us.cc')))
mysql_music_query(parse_music_shouye(url_response('http://m.kugou.com')))
a = xml.dom.minidom.parseString(str(url_response(url_tianqi)))#解析xml
mysql_tianqi_query(a)
for j in range(9):
  
   mysql_query(contents_title_list[j],jpg_list[j],min_contents[j],hrefs_list[j])
  
