import urllib.request,re,bs4,sys,requests,lxml,os,json,random,io
method = json.loads(sys.argv[1])
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
class manhua:
    name = ''#类属性
    mulu = 0
    manhua = 0
   
    def __init__(self,url,name,mulu,manhua):
        self.url = url #实例属性
        self.name = name
        self.mulu = mulu
        self. manhua = manhua
    def request(self):
        headers ={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'

            }
        r = requests.get( self.url,headers=headers)
        return r.text
    def parse(self,response):
        content = bs4.BeautifulSoup(response,'lxml')
        data = content.select('.pure-g')
        data = str(data[1]).replace('src="','src="http:')
        data = data.replace('href="','href="/index.php/manhua/manhua_mulu?nb=')
        data = data.replace('http://static.fzdm.com/none.png','/images/zanwu.jpg')
        print(data)
    def parse_manhua_mulu(self,response):
        content = bs4.BeautifulSoup(response,'lxml')
        data = content.select('#content')
        #with open(r'C:\Users\Administrator\Desktop\1.html','w+') as f:
        #    f.write(str(data[0]))
       
        data = str(data[0]).replace('href="','href="/index.php/manhua/manhua_yh?nb=%s&yh='%(nb))
        print(data)
       
    def parse_manhua(self,response):
        server_list = ['http://120.52.72.23/p1.xiaoshidi.net']#,'http://101.96.10.31/p1.xiaoshidi.net','http://183.91.33.78/p1.xiaoshidi.net']
        content = bs4.BeautifulSoup(response,'lxml')
        data = content.select('body')
        title = content.select('#mh h1')
        data_img = content.select('#mh #mhimg1')
        nav = content.select('.navigation')
        nav_replace = str(nav[0]).replace('href="','href="manhua_yh_mhyh?nb=%s&yh=%s&mhyh='%(nb,yh))      
       # with open(r'C:\Users\Administrator\Desktop\1.html','w+') as f:
         #   f.write(str(data[0]))
        searchObj = re.search(r'var mhurl = "(.*)"',str(data[0]),re.M|re.I) 
        if(('2015//' in searchObj.group(1))or('2016//' in searchObj.group(1))or('2017//' in searchObj.group(1))):
             html = str(data_img[0]).replace('<div id="mhimg1">','<div id="mhimg1"><img src="http://s1.nb-pintai.com'+r'/'+searchObj.group(1)+'"/>')
        else:
             html = str(data_img[0]).replace('<div id="mhimg1">','<div id="mhimg1"><img src="'+random.choice(server_list)+r'/'+searchObj.group(1)+'"/>')

        #print(str(data[0])
        print(str(title[0])+html+ nav_replace)
try:
    shili_shouye =  manhua('http://manhua.fzdm.com/',1,1,1)    
    if method['method'] == 'manhua_shouye':
            shili_shouye.parse(shili_shouye.request())

    elif method['method'] == 'manhua_mulu':
            nb = method['nb'].replace('\/','')
            manhua_mulu = manhua(r'http://manhua.fzdm.com/'+nb+'/',1,1,1)
           
            manhua_mulu.parse_manhua_mulu(manhua_mulu.request())
    elif method['method'] == 'manhua':
            yh= method['yh'].replace('\/','')
            nb= method['nb']
            manhua_yh = manhua(r'http://manhua.fzdm.com/'+nb+r'/'+yh+'/',1,1,1)
            manhua_yh.parse_manhua( manhua_yh.request())      
    elif method['method'] == 'manhua_mhyh':
            yh= method['yh'].replace('\/','')
            nb= method['nb']
            mhyh= method['mhyh']
            if (mhyh.find("\\") == -1):#不含负一抓取下一页
                manhua_yh = manhua(r'http://manhua.fzdm.com/'+nb+r'/'+yh+r'/'+mhyh,1,1,1)
                manhua_yh.parse_manhua( manhua_yh.request())


            elif(mhyh.find("../")== -1):
                 yh = method['mhyh']
                 yh = re.search(r'..\/(.*)\/',yh,re.M|re.I)
                 yh = yh.group(1).strip('\\')
                 manhua = manhua(r'http://manhua.fzdm.com/'+nb+r'/'+yh+'/',1,1,1)
                 
                 #print(r'http://manhua.fzdm.com/'+nb+r'/'+yh)
                 manhua.parse_manhua(manhua.request())
            elif (mhyh.find("./")== -1):#抓取第一次的上一页
                manhua_yh = manhua(r'http://manhua.fzdm.com/'+nb+r'/'+yh,1,1,1)
                manhua_yh.parse_manhua( manhua_yh.request())     
               
           
except:
    pass
        
#shili_shouye =  manhua('http://manhua.fzdm.com/',1,1,1)      
#shili_shouye.parse(shili_shouye.request())主页
#shili_mulu =  manhua('http://manhua.fzdm.com/1/',1,1,1) 
#shili_mulu.parse_manhua_mulu(shili_mulu.request())漫画目录
#shili_shouye.parse(shili_shouye.request())主页
#shili_manhua=  manhua('http://manhua.fzdm.com/1/brz12/',1,1,1) 
#shili_manhua.parse_manhua(shili_manhua.request())
        
    
