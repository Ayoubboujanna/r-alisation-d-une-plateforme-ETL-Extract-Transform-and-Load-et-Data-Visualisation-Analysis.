from django.shortcuts import render
import pandas as pd   #to create dataframe
import requests       #to send the request to the URL
from bs4 import BeautifulSoup #to get the content in the form of HTML
import numpy as np  # to count the values (in our case)

# Create your views here.


def scrap1():
    #assigning the URL with variable name url
    url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
    #request allow you to send HTTP request
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #creating an empty list, so that we can append the values
    rang=[]
    movie_name = []
    year = []
    time = []
    rating = []
    votes = []
    gross = []
    Director = []
    Stars = []
    #storing the meaningfull required data in the variable
    movie_data = soup.findAll('div', attrs= {'class': 'lister-item mode-advanced'})

    #calling one by one using for loop
    for store in movie_data:
      rang1 = store.h3.find('span', class_ = 'lister-item-index unbold text-primary').text.replace('.', '')
      rang.append(rang1)

      name = store.h3.a.text
      movie_name.append(name)
    
      year_of_release = store.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
      year.append(year_of_release)
    
      runtime = store.p.find('span', class_ = 'runtime').text.replace(' min', '')
      time.append(runtime)
    
      rate = store.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n', '')
      rating.append(rate)
    
      #since, gross and votes have same attributes, that's why we had created a common variable and then used indexing
      value = store.find_all('span', attrs = {'name': 'nv'})
    
      vote = value[0].text
      votes.append(vote)
      grosses = value[1].text if len(value) >1 else '0'
      gross.append(grosses)
      
    
      #Cast Details -- Scraping Director name and Stars -- Not explained in Video
      cast = store.find("p", class_ = '')
      cast = cast.text.replace('\n', '').split('|')
      cast = [x.strip() for x in cast]
      cast = [cast[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
      Director.append(cast[0])
      Stars.append([x.strip() for x in cast[1].split(",")])
    #creating a dataframe using pandas library
    movie_DF = pd.DataFrame({'rang': rang,'movie_name': movie_name, 'year': year, 'time': time, 'rating': rating, 'votes': votes, 'gross': gross, "director": Director, 'stars': Stars})
    #Saving data in csv file:

    movie_DF.to_csv("Top_100_IMDB_Movies_1.csv")
    movie_DF.head(7)   
if __name__ == '__main__':
  scrap1()    