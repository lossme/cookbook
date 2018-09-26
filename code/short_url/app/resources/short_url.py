import re

from flask import request, redirect, current_app
from flask_restful import Resource

from ..services.short_url import URLShorter


class Encode(Resource):
    url_pattern = re.compile(r"^https?://[^\s]+")

    def get(self):
        url = request.args.get('url')
        if url and self.url_pattern.match(url):
            short_url = URLShorter.encode(url=url)
            return {
                "short_url": '{}/{}'.format(current_app.config['HOST'], short_url)
            }
        else:
            return {
                "msg": "url不合法"
            }


class Decode(Resource):

    def get(self, short_url):
        url = URLShorter.decode(short_url=short_url)
        if url:
            return redirect(url)
        else:
            return "not found"
