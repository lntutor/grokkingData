from elasticsearch import Elasticsearch
from config import ES_HOSTS

print ES_HOSTS

client = Elasticsearch(
    hosts=ES_HOSTS
)
