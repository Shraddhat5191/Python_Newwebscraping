from task1 import sracp_movie
list=sracp_movie()
import json
import pprint
def name_of_year(movies):
    years=[]
    for i in movies:
        # print(i)
        year=i["Year"]
        # print(years)
        if year not in years:
            years.append(year)       
    years.sort()        
    movie_dict={i:[]for i in years} 
    for i in movies:
        year=i["Year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
                with open("task2.json","w")as file:
                    json.dump(movie_dict,file,indent=4)
    return movie_dict
name_of_year(list)
