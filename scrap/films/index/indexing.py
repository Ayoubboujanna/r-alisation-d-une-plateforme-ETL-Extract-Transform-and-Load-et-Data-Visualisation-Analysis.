import elasticsearch


def add_data_to_elastic(rang, movie_name, year,time,rating,votes,gross,director,stars):
    INDEX_NAME = 'films'

    ELASTIC_HOST = 'http://localhost:9200/'

    client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

    data = {
        'rang': rang,
        'movie_name' : movie_name,
        'year' : year,
        'time': time,
        'rating' : rating,
        'votes' : votes,
        'gross': gross,
        'director' : director,
        'stars' : stars,
    }

    client.index(index= INDEX_NAME, body= data)