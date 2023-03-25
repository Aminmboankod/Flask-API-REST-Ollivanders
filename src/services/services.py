from flask import fields, marshal_with, abort
from repository.apiDB import item

class Service():

    resource_fields = {
        'name': fields.String,
        'sell_in': fields.Integer,
        'quality': fields.Integer
    }

    @staticmethod
    @marshal_with(resource_fields)
    def get_item(name):

        if not name:
            abort(404, message="Es necesario el nombre del item")
        
        object_item = item(name)
        
        if not object_item:
            abort(404, message="El item {} no existe".format(name))

        return { 'name': item[0], 'sell_in': item[1], 'quality': item[2] }
    