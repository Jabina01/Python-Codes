import requests
from bs4 import BeautifulSoup
import pprint
import json
import os
import random
import time
from task1 import adventure_movie
from task5 import main_fun
task1=adventure_movie()
url_list=[]
for i in task1:
    url_list.append(i['Movie URL'])
def scrape_movie(movie_url_list):
#     # print(scrape_movie)
    random_sleep = random.randint(1,3)
    for i in movie_url_list:
        id=i[:34]
        file_name = id+".json"
        if os.path.exists(file_name):
            fil1=("file_name.json","r")
            h=json.load(fil1)
            print(h)
                # json.dump(file_name,fil2,indent=2)
            # t = F.read()
            # dic=json.loads(t)
            # return dic
        else:
            time.sleep(random_sleep)
            page=requests.get(i)
            soup=BeautifulSoup(page.text,"html.parser")
            d={}
            main_div=soup.find("ul",class_="content-meta info")
            sub_div=main_div.find_all("li",class_="meta-row clearfix")
            for i in (sub_div):
                d[i.find("div",class_="meta-label subtle").text]=i.find("div",class_="meta-value").text
            pprint.pprint(d)
            with open("file_name.json","w")as fil:
                json.dump(d,fil,indent=2)
            # pprint()
#                 # f=a.write()Movie URL
#                 # f.close()
                

#         #     # k=o.write(json.dump(d,o,indent=2))
#         #     # c=o.close()
pprint(scrape_movie(url_list))