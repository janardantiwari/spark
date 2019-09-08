import time as t

from datetime import datetime as d

temp="hosts"
path=r"/etc/hosts"

ip="127.0.0.1"

weblist=["www.facebook.com","facebook.com","www.google.com","google.com"]

t1=d(d.now().year,d.now().month,d.now().day,7)
t2=d(d.now().year,d.now().month,d.now().day,22,59) 

while True:
    if t1 < d.now() < t2 :
      
      print("BUSY")
      
      with open(path,"r+") as f:
        
         c=f.read()
        
         for w in weblist :
             if w not in c:
                 f.write(ip + " " + w + "\n")

        
    else :
        print("FREE")
    
        with open(path,"r+") as  f:
            c=f.readlines()
            f.seek(0)

            for i in c:
                if not any( w in i for w in weblist):
                   f.write(i)
            f.truncate()
    t.sleep(5)


 
