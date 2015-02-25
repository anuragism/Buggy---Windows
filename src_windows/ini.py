import json, requests
import os
from bs4 import BeautifulSoup
import shutil

CF = raw_input()

url = "http://codeforces.com/contest/"+CF+"/problems"
data = requests.get(url)

soup = BeautifulSoup(data.text)
        
counter = 0
for div in soup.findAll('div', 'problemindexholder'):
    
    if (os.path.exists("C:/CF/dist/"+CF+"/"+chr(ord('A')+counter))):
        print "Folder Exists"
    else:
        os.makedirs("C:/CF/dist/"+CF+"/"+chr(ord('A')+counter))

    shutil.copyfile("C:/CF/dist/"+"f.bat","C:/CF/dist/"+CF+"/"+chr(ord('A')+counter)+"/f.bat")
    shutil.copyfile("C:/CF/dist/"+"template.cpp", "C:/CF/dist/"+CF+"/"+chr(ord('A')+counter)+"/prog.cpp" )
    
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
