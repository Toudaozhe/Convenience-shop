#!/usr/bin/env python
#coding=utf-8
# __author__ = '戴儒锋'
# http://www.linuxyw.com
"""
    执行代码前需要安装
    pip install bottle
    pip install websocket-client
    pip install bottle-websocket
"""
from bottle import get, run
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket
import json
users = set()   # 连接进来的websocket客户端集合
user_name = [] #接进来的客户名字集合
@get('/websocket/', apply=[websocket])
def chat(ws):
    users.add(ws)
    while True:
        msg = ws.receive()  # 接客户端的消息
       
        if msg :
            array = json.loads(msg)
           
            array['name_set'] = []
            if(array['content'] == '进入了聊天'):
                user_name.append(array['name'])
                for i in  user_name:
                  
                   
                    array['name_set'].append(i)
                   
            elif(array['content'] == '退出了聊天'):
                   
                    user_name.remove(array['name'])
                    for i in  user_name:
                  
                   
                        array['name_set'].append(i)
            try:
               
                msg = json.dumps(array)   
                for u in users:
                    u.send(msg) # 发送信息给所有的客户端
            except:
                pass
        else:
            break
    # 如果有客户端断开连接，则踢出users集合
    
    users.remove(ws)
run(host='172.19.234.143', port=500, server=GeventWebSocketServer)
