from collections import Counter
import csv,time
start = time.time()
top_apps = set()
prime_genre_list = []
user_rating_list = []
applications = {}
apps_list = []
appis = {}
with open('AppleStore1.csv',mode='r',encoding="utf8") as csvfile:
    app_store = csv.DictReader(csvfile)
    for row in app_store:
        prime_genre,user_rating = row["prime_genre"],row["user_rating"]
        prime_genre_list.append(prime_genre)
        user_rating_list.append(user_rating)
    for apps in zip(prime_genre_list,user_rating_list):
        apps_list.append(apps)
    print()  
    for i,z in apps_list:
        appis[i] = z
    print(appis)

    # print(apps_list)    
    # print(sorted(top_apps, key=lambda x: x[1],reverse=True))
        


print ('It took', time.time()-start, 'seconds.')
