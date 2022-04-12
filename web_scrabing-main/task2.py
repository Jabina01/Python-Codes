
from task1 import adventure_movie
jabeena=adventure_movie()
import json
def scrape_top_list_1(movies):
    years=[]
    for i in movies:
        # print(i['Year'])
        year = i["Year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    for i in movies:
        year=i ["Year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    with open("jabeena.json","w")as f:
        json.dump(movie_dict,f,indent=4)
    return movie_dict

scrape_top_list_1(jabeena)