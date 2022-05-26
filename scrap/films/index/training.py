import csv
from pymongo import MongoClient
import pandas as pd

def connect():
    client =MongoClient("mongodb://localhost:27017")
    df= pd.read_csv('Top_100_IMDB_Movies.csv',on_bad_lines='skip')
    data = df.to_dict(orient="records")
    db = client["films"]
    db.films_films.insert_many(p for p in data)
if __name__ == '__main__':
    connect()
