from selenium import webdriver
from multiprocessing import Process#进程
from multiprocessing import Pool#进程池子
from multiprocessing import Lock#进程锁
import urllib.parse
import bs4,lxml
import queue
import os
import pymysql
def mysql_query(Img_Path,Name,Miaoshu,Danjia):
   db = pymysql.connect('localhost','root','1993524','user_info',charset='utf8')
   cursor = db.cursor()
   sql = "insert into user_shop (Img_Path,Name,Miaoshu,Danjia)values('%s','%s','%s','%s')"%(Img_Path,Name,Miaoshu,Danjia)
#keyword = urllib.parse.quote('路由器')
   try:
   
      cursor.execute(sql)
      db.commit()
   except:
      db.callback()
   
  
   db.close()
def parse_html(name,page):
  
   browser= webdriver.PhantomJS()
   keyword = urllib.parse.quote(name)
   browser.get('https://search.jd.com/Search?keyword=%s&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=%s&s=30&click=0'%(keyword,page))
   data = browser.page_source
   #with open(r'C:\Users\Administrator\Desktop\1.txt','w+',encoding='utf8') as f:
   #    f.write(data)
   soup = bs4.BeautifulSoup(data,'lxml')
   #content = soup.select('.tab-content-item')
   content = soup.select('.gl-item')
   #lock.acquire()
   print('开启')
   for i in range(len(content)):
      
         title = content[i].select('.p-name a em')
         price= content[i].select('.p-price strong i')
         img= content[i].select('.p-img a img')
        # print(title[0].get_text())
        # with open(path +r'\1.txt','a+',encoding='utf8') as f:
          #print('存入')
        #  f.write(title[0].get_text())
        #  f.write('\n')
         
         #print(price[0].get_text())
        # with open(path +r'\1.txt','a+',encoding='utf8') as f:
        #  f.write(price[0].get_text())
       #   f.write('\n')
         for key in img[0].attrs:#图片
            if 'src' in key:
              # print(img[0].attrs['src'])
             #  with open(path +r'\1.txt','a+',encoding='utf8') as f:
              #     f.write(img[0].attrs['src'])
              #     f.write('\n')
                mysql_query(img[0].attrs['src'],'测试',title[0].get_text(),price[0].get_text())
            elif 'data-lazy-img' in key:
              # with open(path +r'\1.txt','a+',encoding='utf8') as f:
               #    f.write(img[0].attrs['data-lazy-img'])
               #    f.write('\n')
                mysql_query(img[0].attrs['data-lazy-img'],'测试',title[0].get_text(),price[0].get_text())
           # print(img[0].attrs['data-lazy-img'])
      
   browser.quit()
   #lock.release()
   print('释放')


   
product = ['火腿肠','醋','米','酱油','指甲钳','牛奶']#设置为外部变量
num =10#设置所需页数
q = queue.Queue(maxsize = 10)
parse_html('火腿肠',1)
'''path = os.getcwd()
lock = Lock() 
for w in range(len(product)):
   q.put(product[w])
if __name__=='__main__':
   p = Pool(4)#开进程池,限制进程数
   for x in range(len(product)):
      name = q.get()
      for j in range(1,num):
         p.apply_async(parse_html,args=(name,j))#维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        
   #p =  Process(target=parse_html, args=('路由器',))

   p.close()

   p.join() #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
'''
'''for i in range(len(content)):
   
    title = content[i].select('.p-img a')
    print(title[0].attrs['title'])'''

'''for i in range(len(content)):
    for key in content[i].attrs:
        if 'title' in key:
       
            print(content[i].attrs['title'])
     
        else:
            pass
for j in range(len(content)):
    img_soup = bs4.BeautifulSoup(str(content[j]),'lxml')
    img = img_soup.select('img')
    for key in img[0].attrs:
        if 'src' in key:
            print(img[0].attrs['src'])
        elif 'data-lazy-img' in key:
            
            print(img[0].attrs['data-lazy-img'])
        else:
            pass
           
         
for w in range(len(price)):
    print(price[w].attrs('data-price'))'''

