from flask_restful import Resource

from ..common import verify_json_payload, error_handler
from ..models import Todo


class TodoApi(Resource):

    class Schema(object):
        get = {}

        post = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "title": "todo api",
            "description": "",
            "type": "object",
            "properties": {
                "message": {
                    "description": "todo message",
                    "type": "string",
                }
            },
            "required": ["message"],
        }

        delete = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "title": "todo 删除接口",
            "description": "",
            "type": "object",
            "properties": {
                "id": {
                    "id": "todo id",
                    "type": "integer",
                }
            },
            "required": ["id"],
        }

    @error_handler
    def get(self):
        return Todo.list()

    @error_handler
    def post(self):
        payload = verify_json_payload(self.Schema.post)
        return Todo.add(message=payload['message'])

    @error_handler
    def delete(self):
        payload = verify_json_payload(self.Schema.delete)
        return Todo.delete(id=payload['id'])
