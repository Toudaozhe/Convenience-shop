import bs4,sys,urllib.request,json
try:
    #href = sys.argv[1]
    array_json = json.loads(sys.argv[1])

                #url_href = 'http://www.23us.cc/html/101/101573/' + href
                #print(url_href)
                #url_href = 'http://www.23us.cc/html/101/101573/5367503.html'
                #req=urllib.request.Request(url_href)#请求
                #req.add_header('User-Agent:','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')#增加请求头防止被和谐


    url_href= 'http://www.23us.cc/html/'+array_json['id']+'/'+array_json['idd']

    req=urllib.request.Request(url_href)#请求
    req.add_header('User-Agent:','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')#增加请求头防止被和谐


    response = urllib.request.urlopen(url_href)#响应打开网址
    html = response.read().decode('utf8')#解码utf8,解压缩gzip

    soup = bs4.BeautifulSoup(html,"lxml")#改成bs4的对象
    contents = soup.select('#content')
    h1 = soup.select('h1')

    footlink = soup.select('.link')
              
    xiaoshuo_footlinkt_replace =  str(footlink[0]).replace('href="','href="/index.php/novel/xiaoshuo?id='+array_json['id']+'&idd=')
    xiaoshuo_footlinkt_replace_mulu =  str(footlink[0]).replace('href="','href="/index.php/novel/xiaoshuo_mulu?id='+array_json['id'])
    soup =   bs4.BeautifulSoup(xiaoshuo_footlinkt_replace ,"lxml")#改成bs4的对象
    soup_mulu =   bs4.BeautifulSoup(xiaoshuo_footlinkt_replace_mulu  ,"lxml")#改成bs4的对象
    footlink1 =  soup.a.next_sibling
    footlink2 =  soup.a.next_sibling.next_sibling

    footlink3 =  soup_mulu.a.next_sibling.next_sibling.next_sibling
    footlink4 =  soup.a.next_sibling.next_sibling.next_sibling.next_sibling
    footlink5 =  soup.a.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    footlink = r'<div class="link xb">'+str(footlink1)+str(footlink2)+str(footlink3)+str(footlink4)+str(footlink5)+r'</div>'
    print(footlink)
        #xiaoshuo_content_replace = str(footlink).replace('href="','href="/index.php/novel/xiuzhen?id=')     
                    #with open('C:\\Users\\Administrator\\Desktop\\data\\1.html','a+',encoding='utf_8_sig')as a:#目录自己定
                #xiaoshuo_footlinkt_replace = str(footlink[0]).replace('href="','href="/index.php/novel/xiaoshuo?id='+array_json['id']+'&idd=') 
         
    xiaoshuo_content_replace = str(contents[0]).replace(u'\xa0','&nbsp&nbsp')
    print(str(h1[0]) + str(xiaoshuo_content_replace) + footlink )




except:
    print('''<?php
                defined('BASEPATH') OR exit('No direct script access allowed');
                ?><!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="utf-8">
                <title>404 Page Not Found</title>
                </head>
                <body>
                <script language="javascript" type="text/javascript">

                var i = 5;var intervalid;intervalid = setInterval("fun()", 1000);
                function fun() 
                {	
                        if (i == 0) 
                        {
                                window.location.href = "/index.php/home";
                                clearInterval(intervalid);
                        }
                        document.getElementById("mes").innerHTML = i;i--;
                }
                </script>
                <style>
                p{
                 position:absolute;
                 left:95px;
                 top:90px;
                 color:#3793CC;

                }
                </style>
                <div id="errorfrm">

                        <div id="error">
                                <img src="/images/404.gif"  alt="出错啦" />
                                
                                <p>将在 <span id="mes">5</span> 秒钟后返回首页！</p>
                        </div>
                </div>
                <a style='width:150px;height:100px;position:absolute;top:570px;left:90px;border:none;background:none;' href='/index.php'>
                </a>
                </body>
                </html>''')

