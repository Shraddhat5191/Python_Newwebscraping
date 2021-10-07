from task1 import sracp_movie
import json
list1=sracp_movie()
def group_by_decade(movies):
    list1=[]
    for i in movies:
        # print(i)
        a=i["Year"]%10
        d=i["Year"]-a
        if d not in list1:
            list1.append(d)
    list1.sort()
    # print(list1)
    moviedec={}
    for i in list1:
        d_year=[]
        for x in movies:
                # print(x)
            if x["Year"]>=i and x["Year"]<=i+10:
                d_year.append(x)
                moviedec[i]=d_year
                with open("task3.json","w")as f:
                    json.dump(moviedec,f,indent=5)
    return moviedec            


group_by_decade(list1)