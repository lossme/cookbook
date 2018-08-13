import sys

from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES


def search(image_file):
    es = Elasticsearch(hosts=["127.0.0.1:9200"])
    ses = SignatureES(es, index='images', doc_type='image')
    result = ses.search_image(image_file)
    print(result)


if __name__ == '__main__':
    image_file = sys.argv[1]
    search(image_file)
