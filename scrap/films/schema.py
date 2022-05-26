import graphene
from graphene_django import DjangoObjectType
from .models import Films

class FilmsInfo(DjangoObjectType):
    class Meta :
        model = Films
        fields = ("rang","movie_name","year","time","rating","votes","gross","director","stars")

class Query(graphene.ObjectType):
    all_films = graphene.List(FilmsInfo) 
    def resolve_all_films(root, info):
        return Films.objects.all()        
schema = graphene.Schema(query=Query)