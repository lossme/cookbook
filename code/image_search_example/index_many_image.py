import os

from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES


def walk(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        # for dirname in dirnames:
        #     yield dirname
        for filename in filenames:
            yield os.path.join(parent, filename)


def main():
    image_dir = '/home/key/图片/image_search_data'
    es = Elasticsearch(hosts=["127.0.0.1:9200"])
    ses = SignatureES(es, index='images', doc_type='image')

    for file in walk(image_dir):
        ses.add_image(file)
        print('index image: {}'.format(file))


if __name__ == '__main__':
    main()
