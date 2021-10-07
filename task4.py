import requests
from bs4 import BeautifulSoup
import json
def sracp_movies():
    dict={}
    list=[]
    url="https://www.rottentomatoes.com/m/black_panther_2018/"
    all=requests.get(url)
    code=BeautifulSoup(all.text,"html.parser")
    ul_class=code.find('ul',class_="content-meta info")
    li=ul_class.find_all("li",class_="meta-row clearfix")
    for i in li:
        rating=i.find("div",class_="meta-value").get_text().strip().replace("\n","")
        genre=i.find("div",class_="meta-label subtle").get_text()
        dict1=dict.update({genre:rating})
        list.append(dict1)
        with open("task4.json","w")as f:
            json.dump(dict,f,indent=5)
    return list        
sracp_movies() 





