#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys
import time
import threading
# 创建 socket 对象
list_pool =[]
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# 获取本地主机名
host = socket.gethostname()
port = 500
# 绑定端口
serversocket.bind((host, port))
# 设置最大连接数，超过后排队
serversocket.listen(5)
# 建立客户端连接
#开3个线程
  
  

def rec(clientsocket,addr):
    true = 1
    
    print('进入成功')
    while true:
         time.sleep(1)
         try:
            print('正在深度进入')
            t=clientsocket.recv(1024).decode('utf8')  #函数的核心语句就一条接收方法
            print(clientsocket)
            print(t)
            print(len(list_pool))
            for i in range(len(list_pool)):
                if(list_pool[i] == clientsocket):
                    pass
                else:
                    list_pool[i].send(t.encode('utf8'))
         except:
            print('失败')
            true = False
            list_pool.remove(clientsocket)
            
            clientsocket.close()
            
    
    print('结束了')
    
        

while True:
        clientsocket,addr = serversocket.accept()# 建立客户端连接
        print('接入成功')
        list_pool.append( clientsocket)
        trd=threading.Thread(target=rec,args=(clientsocket,addr))#必须使用变量
  
        trd.start()
        print('线程启动成功')
       
       



    
    

