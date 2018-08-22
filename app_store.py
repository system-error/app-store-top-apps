from collections import Counter,defaultdict
import csv,time,json 
start = time.time()
top_apps = set()
prime_genre_list = []
user_rating_list = []
track_name_list = []
applications = {}
apps_list = []
appis = defaultdict(list)
with open('AppleStore1.csv',mode='r',encoding="utf8") as csvfile:
    app_store = csv.DictReader(csvfile)
    for row in app_store:
        prime_genre,user_rating,track_name = row["prime_genre"],row["user_rating"],row["track_name"]
        if user_rating > '3.5':
            prime_genre_list.append(prime_genre)
            user_rating_list.append(user_rating)
            track_name_list.append(track_name)
        # prime_genre_list.append(prime_genre)
        # user_rating_list.append(user_rating)    

    for apps in zip(prime_genre_list,user_rating_list,track_name_list):
        apps_list.append(apps)
    print()  
    for i,z,y in apps_list:
        appis[i].append(z)
        appis[i].append(y)
    print(appis)
    # for i,z,y in apps_list:
    #     applications[i] = z,y
    #     # applications[i] = y
    # print(applications)
js = json.dumps(appis, sort_keys=False, indent=4, separators=(',', ': '))    
with open('result.json', 'w') as fp:

    fp.write(js)
    fp.close()
    
    print(apps_list)    
    # print(sorted(top_apps, key=lambda x: x[1],reverse=True))
        


print ('It took', time.time()-start, 'seconds.')
