#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys
import threading

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = '223.68.193.78'

# 设置端口好
port = 5222

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
#data="client:"+input('client:')+'\n\r'
true = 1
def rec(s):  
    global true 
    while true:
        try:
            t=s.recv(1024).decode('utf8')  #函数的核心语句就一条接收方法  
            if t == "exit":  
                true=False  
            print(t)
        except:
            pass
trd=threading.Thread(target=rec,args=(s,))  
trd.start()  
while True:
    content = input(socket.gethostname() +":")
    content = socket.gethostname() +":"+content 
    s.send(content.encode('utf8'))




s.close()

    #a=s.send(data.encode('utf-8'))


'''ss= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host1 = '192.168.0.211'

# 设置端口好
port1 = 501

# 连接服务，指定主机和端口
ss.connect((host1, port1))

# 接收小于 1024 字节的数据
msg = ss.recv(1024)

ss.close()'''

   

