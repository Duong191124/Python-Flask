from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Int(required=True)
    
class StoreSchema(Schema):
    id = fields.str(dump_only=True)
    name = fields.str(required=True)    