# from task1 import adventure_movie
# from task2 import adventure_movie
# jabeena=adventure_movie()
# import json
# jabeena_data=adventure_movie()
# movie_by_year=adventure_movie(jabeena_data)
# def scrappe_top_list_2(movies):
#     moviedic={}
#     list=[]
#     for i in movies:
#         mod=movie_by_year%10
#         decade=movie_by_year-mod
#         if decade not in list:
#             list.append(decade)
#         list.sort
#     for i in list:
#         moviedic[i]=[]
#     for i in moviedic:
#         decade=i+9
#         for x in movies:
#             if x<=decade and x>=i:
#                 for j in movies[x]:
#                     moviedic[i].append(j)
#                     with open ("seerat.json",)as data:
#                         json.dump(moviedic,data,i)
#                     return moviedic
# scrappe_top_list_2(movie_by_year)





from task1 import adventure_movie
import json
name=adventure_movie()
def group_by_decade(movise):
    movisedec={}
    list1=[]
    for index in movise:
        mod=index["Year"]%10
        decode=index["Year"]-mod
        if decode not in list1:
            list1.append(decode)
    print(list1)    
    list1.sort()
    # print(list1) 
    for i in list1:
        movise_list=[]
        # movisedec[i]=[]
        # print(movisedec)  
        # for i in movisedec:
            # dec10=i+9
        for x in movise:
                # if x["Year"]<=dec10 and x["Year"]:
            if x["Year"]>=i and x["Year"]<=i+10:
                movise_list.append(x)
                movisedec[i]=movise_list
                    # for v in movise[x]:
                    #     movisedec[i].append(v)
                with open("Aabiru.json","w")as file:
                        json.dump(movisedec,file,indent=3)
                print(movisedec)    
    print(movisedec)                    
group_by_decade(name)