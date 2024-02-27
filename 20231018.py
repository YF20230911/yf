import requests
import re
import time
import random

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
url="https://ybu.edu.cn"

response=requests.get(url,headers=header)
print(response.status_code)
print(response.encoding)

##content=response.text  外网直接访问
content=response.content.decode("utf-8")
#print(content)

part=re.compile(r'<a.+?her="(.+?.htm)".*?>')
a_list=part.findall(content)
for i in a_list:
    tmp=requests.get(url+"/"+i,headers=header).content.decode("utf-8")
    a2_list=part.findall(tmp)
    print(f"url:{i}\n有{len(a2_list)}个链接")
    print(url+"/"+i)
    time.sleep(random.randint(3,5))
    input("等待点击继续")


# class MySpyder():
#     def __init__(self) -> None:
#         self.header={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
#         } 
#         self.url=url
#         self.mark=mark

# def  response(self):
#     return requests.get(self.url,headers=header)

# def responseText(self):
#     return self.response.text

# def fname(arg):
#     pass
# def getMarkData(self):
#     part=re.compile(self.mark)
#     content=self.responseUtf8()
#     l=part.findall(content)
#     return l
# def get(self):
#     return self.getMarkData()
 
# if __name__=="_main_":
#     url