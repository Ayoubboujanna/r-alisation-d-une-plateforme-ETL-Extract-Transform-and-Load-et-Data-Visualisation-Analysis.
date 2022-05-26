
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Films


@registry.register_document
class FilmsDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'films'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Films # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'rang',
            'movie_name',
            'year',
            'time',
            'rating',
            'votes',
            'gross',
            'director',
            'stars',
        ]
