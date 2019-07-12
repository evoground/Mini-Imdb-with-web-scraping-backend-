from bs4 import BeautifulSoup
import requests
import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user = "postgres",
                                password = "qwerty",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "postgres")
cursor = connection.cursor()

create_tb =  '''CREATE TABLE IMDB
                (ID INT PRIMARY KEY NOT NULL,
                MovieName TEXT NOT NULL,
                Raing TEXT NOT NULL,
                Star_Cast TEXT NOT NULL); '''
cursor.execute(create_tb)
connection.commit()
print("Table created successfully in PostgreSQL ")

#movieName = []
#imdbRating = []
#starCast = []
count=1
for page_idx in range(1,1100,50):
    response = requests.get("https://www.imdb.com/search/title/?title=a&start="+str(page_idx)+"&ref_=adv_nxt")
    soup = BeautifulSoup(response.content,"lxml")
    for i in soup.findAll('div',attrs={'class' : 'lister-item-content'}):
        print(count)
        cast=[]
        for temp in i.findAll('a'):
                if len(temp.text)>4:
                        cast.append(temp.text)

        movie=cast[0]
        rating = i.find('strong') 
        if rating== None :
                rating="Not Rated"
        else:
                rating=rating.text
        cast=str(";".join(cast[1:]))


        #movieName.append(movie)
        #imdbRating.append(rating)
        #starCast.append(cast)

        insert_tb = ''' INSERT INTO IMDB 
                                 VALUES (%s,%s,%s,%s) '''
        value_tb = (str(count),movie,rating,cast)
        count+=1

        cursor.execute(insert_tb,value_tb)
        connection.commit()

if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
