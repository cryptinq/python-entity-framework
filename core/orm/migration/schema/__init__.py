from .fields.integer import Integer
from .fields.primary_key import PrimaryKey
from .fields.string import String


class Field:
    PRIMARY_KEY = PrimaryKey
    STRING = String
    INTEGER = Integer

    def sql(self): return ""
