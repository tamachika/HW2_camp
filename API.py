import time
import requests


topNEWS = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")

dicN = topNEWS.json()

title,url = [],[]
for i in range(30):
    time.sleep(1) # ここで1秒止まる
    res = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{dicN[i]}.json?print=pretty")
    dic = res.json()
    
    lis = list(dic.keys())
    j=0
    while len(dic) > 2:
        if lis[j] != "title" and lis[j] != "url":
            del dic[lis[j]]
            del lis[j]
        else:
            j+=1
            
    print(dic)
    
    # print(dic["title"])
    # print(dic["url"])
    #url += [requests.get(f"https://hacker-news.firebaseio.com/v0/item/{dic[i]}.json?print=pretty")["url"] ]
    