import json, requests
import os
from bs4 import BeautifulSoup
import shutil
import urllib, urllib2
import sys

CF = raw_input()

url = "http://codeforces.com/contest/"+CF+"/problems"
flag=0
try:
    data = requests.get(url)
    flag = 1
except Exception, e:
    print "Direct Connection Failed, trying Proxy"
    fo = open("proxy.txt", "r+")
    http_proxy = fo.read(100)
    fo.close()

    proxyDict = { 
                   "http"  : "http://"+http_proxy
                }

    data = requests.get(url, proxies=proxyDict)
    flag=1

if flag==0:
    print "Error in Connection to Internet"


soup = BeautifulSoup(data.text)

present=1

for x in soup.findAll('li', 'current'):
    present=0

if present == 0:
    sys.exit(0)
        
counter = 0
for div in soup.findAll('div', 'problemindexholder'):
    
    if (os.path.exists("C:/CF/dist/"+CF+"/"+chr(ord('A')+counter))):
        print "Folder Exists"
    else:
        os.makedirs("C:/CF/dist/"+CF+"/"+chr(ord('A')+counter))

    shutil.copyfile("C:/CF/dist/"+"zy.bat","C:/CF/dist/"+CF+"/"+chr(ord('A')+counter)+"/zy.bat")
    shutil.copyfile("C:/CF/dist/"+"zz.bat","C:/CF/dist/"+CF+"/"+chr(ord('A')+counter)+"/zz.bat")
    shutil.copyfile("C:/CF/dist/"+"template.cpp", "C:/CF/dist/"+CF+"/"+chr(ord('A')+counter)+"/aprog.cpp" )
    
    detach_dir = "C:/CF/dist/"+CF+"/"+chr(ord('A')+counter)+"/"
    att_path = os.path.join(detach_dir, chr(ord('A')+counter)+".cpp")
    counter+=1
    incounter = 1
    for item in div.findAll('pre'):
        if incounter%2 == 1:
            att_path = os.path.join(detach_dir, "in"+str(incounter/2)+".txt")
            print att_path
            f = open(att_path, 'wb')
        else:
            att_path = os.path.join(detach_dir, "out"+str((incounter/2)-1)+".txt")
            print att_path
            f = open(att_path, 'wb')
        incounter+=1
        item = str(item).replace("<pre>", "")
        item = str(item).replace("</pre>", "")
        item = str(item).replace("<br/>", "\n")
        f.write(item)