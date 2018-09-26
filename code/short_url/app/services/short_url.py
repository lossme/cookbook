from ..models import URLDB

BASE_LIST = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(BASE_LIST)


def encode(num):
    result = []
    if num == 0:
        result.append(BASE_LIST[0])
    while num > 0:
        result.append(BASE_LIST[num % BASE])
        num //= BASE

    return "".join(reversed(result))


def decode(code):
    num = 0
    code_list = list(code)
    for index, code in enumerate(reversed(code_list)):
        num += BASE_LIST.index(code) * BASE ** index
    return num


class URLShorter():

    @staticmethod
    def encode(url):
        item = URLDB.add(url)
        short_url = encode(item.id + 1000000000)
        return short_url

    @staticmethod
    def decode(short_url):
        id = decode(short_url)
        item = URLDB.query(id - 1000000000)
        if item:
            return item.url
