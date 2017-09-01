import requests,bs4,urllib.parse,json,sys
code_list =[]
if True:
    method = json.loads(sys.argv[1])
    num = method['num']
    string_full =''
    url = 'http://www.kuaidi100.com/autonumber/autoComNum?text=%s'%(num)

    headers = {
        
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',

           
        }
    r =  requests.get(url,headers=headers)
    #a = urllib.parse.unquote(r.text).replace('jsoncallback','').strip('\r\n\r\n()"')
    b = json.loads(r.text)
    
    for i in range(len(b['auto'])):
       if b['auto'][i]['noCount'] =='':
           pass
       else:
           code_list.append(b['auto'][i]['noCount'])
   
    for i in range(len(b['auto'])):
       if b['auto'][i]['noCount'] == max(code_list):
           code = b['auto'][i]['comCode']
  
    url_full = 'https://www.kuaidi100.com/query?type=%s&postid=%s&id=1&valicode=&temp=0.11480142333169707'%(code,num)
    headers_full = {
            'Host': 'www.kuaidi100.com',
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
        }
    r_full =  requests.get(url_full,headers=headers_full)

    contents = json.loads(r_full.text)
    for j in range(len(contents['data'])):

        string = '''
                <div id="result" class="result-list">
                    <li class="first">
                        <div class="col1">
                         <dl><dt>%s</dt>
                              <dd>%s</dd></dl>
                        </div>
                        <div class="col3">%s</div>
                    </li>
                    
          
                
                </div>
             
             
    </section>





    '''%(contents['data'][j]['ftime'].split(' ')[0],contents['data'][j]['ftime'].split(' ')[1],contents['data'][j]['context'])
        
        string_full = string_full + string
    if(string_full !=''):
         print(string_full)

    
