import requests
from bs4 import BeautifulSoup
import json
def sracp_movie():
    url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    r=requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent,"html.parser")
    table_tag = soup.find("table", class_="table")
    tr = table_tag.find_all("tr")  
    top_movie=[]
    # searial_number=1
    for i in tr:
        movie_rank=i.find_all("td",class_="bold")
        for j in movie_rank:
            rank=j.get_text()
            # print(rank)
        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in movie_rating:
            rating=rate.get_text().strip()
            print(rating)
        movie_name = i.find_all("a",class_="unstyled articleLink")
        for name in movie_name:
            title=name.get_text().strip()
            list=title.split()
            print(list)
            year=list[-1][1:5]
            year1=int(year)
            print(year1)
            name_lenght=len(list)-1
            name=""
            print(name_lenght)
            for l in range(name_lenght):
                print(l)
                name+=" "
                name+=list[l]
            MovieName=name
        movie_Reviews = i.find_all("td",class_="right hidden-xs")
        for rev in  movie_Reviews:
            reviews=rev.get_text()
        url=i.find_all("a",class_="unstyled articleLink") 
        for i in url: 
            link=i["href"]
            movie_link="https://www.rottentomatoes.com"+link
            details={"Movie Rank":"","Movie Rating":"","Movie Name":"","Movie Reviews":"","Movie URL":"","Year":""}
            details["Movie Rank"]=rank
            details["Movie Rating"]=rating
            details["Movie Name"]=MovieName
            details["Movie Reviews"]=reviews
            details["Movie URL"]=movie_link
            details["Year"]=year1
            top_movie.append(details.copy())
    with open("task1.json","w") as file:
        json.dump(top_movie,file,indent=3)
    return top_movie                    
screpped=sracp_movie()