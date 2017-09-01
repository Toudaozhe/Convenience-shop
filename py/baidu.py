from selenium import webdriver
import urllib
import time
import bs4
import random
import os
import sys
import json
import shutil

try:
    a = json.loads(sys.argv[1])
    search = a['w']

    num = a['x']


    count = 0
    count_gundong = 1000

   # cap = webdriver.DesiredCapabilities.PHANTOMJS
    #cap["phantomjs.page.settings.userAgent"] = headers['User-Agent']    #设置请求header头信息
   # cap["phantomjs.page.settings.loadImages"] = False    
    browser= webdriver.PhantomJS()#desired_capabilities=cap)#Firefox()#PhantomJS()
    browser.get("https://image.baidu.com/")

    browser.elem = browser.find_element_by_id('kw').send_keys(search) # Find the search box  # Find the search box
    browser.find_element_by_class_name('s_btn').click()
    time.sleep(1)

    #sreach_window=browser.current_window_handle 
    #handles = browser.current_window_handle 
    #js="var q=document.documentElement.scrollTop=100"#滚动条下拉1000px
    #browser.execute_script(js)
    #js1="var q=document.documentElement.scrollTop=10000"#滚动条下拉1000px
    for i in range(int(num)):#换成变量
        count_gundong = count_gundong + 1000
        browser.execute_script('window.scrollBy(0,%d)'%(count_gundong))
    #browser.execute_script(js)
        time.sleep(1)
        #browser.implicitly_wait(50)#隐式等待
    browser.implicitly_wait(50)#隐式等待
    data = browser.page_source.encode('utf8')

    path = os.getcwd()

    if os.path.exists(path+'\\py\\sucai'):
        pass
    else:
        os.mkdir(path+'\\py\\sucai')
    soup = bs4.BeautifulSoup(data,"lxml")

    ip= soup.select('img[class="main_img img-hover"]')
        #检测压缩文件大小
    path_des = path+'\\py\\sucai_dabao'

    def remove_path(path_des):
        size = 0
        for i in os.walk(path_des):
               i[2]
        for j in i[2]:
            size = os.path.getsize(path_des+os.sep+j) + size
        if size > 1073741824:#1超过1G删除
            shutil.rmtree(path_des)
            os.mkdir(path_des)
    remove_path(path_des)
        #print(data)
        #print(browser.title)
    for i in range(len(ip)):
        count = count + 1
        urllib.request.urlretrieve(ip[i].attrs["src"],path+'\\py\\sucai\\'+'%s.jpg'%(count))
    source = [r'E:\xampp\htdocs\py\sucai']#目标打包目录
    target_dir = r'E:\xampp\htdocs\py\sucai_dabao'
    time_data = time.strftime('%Y%m%d%H%M%S')
    target = target_dir+'\\'+time_data+'.zip'#打包日期zip
    zip_command=r"winrar a -ep1 -o+ -ibck  -df  %s  %s"%(target,''.join(source))

    if os.system(zip_command) == 0:print(r'<div id=beijing><div id=xiazai><a href=\py\sucai_dabao'+'\\'+time_data +r'.zip><span style=padding:20px;font-size:20px;>下载链接:</span><img style=width:50px;height:50px;vertical-align:text-bottom;   src=\images\xiazai.jpg  /></a></div></div>')
            
    else:
        print(r'<script language="javascript" type="text/javascript">var i = 5;var intervalid;intervalid = setInterval("fun()", 1000);function fun() {if (i == 0) {window.location.href = "http://www.localhostabc.com/caiji.php";clearInterval(intervalid);}document.getElementById("mes").innerHTML = i;i--;}</script><div id="errorfrm"><h3>出错啦~~~</h3><div id="error"><img src="images/error.gif" mce_src="images/error.gif" alt="" /><p>系统出错，请联系管理员！</p><p>将在 <span id="mes">5</span> 秒钟后返回首页！</p></div></div>')


    browser.quit()
except:
    pass



    

















