from pypika import Column


class Field:

    def __init__(self, field_name: str):
        self.Meta.field = field_name

    class Meta:
        field_name: str = ""

    def meta(self, key):
        if key in dir(self.Meta): return self.Meta.__getattribute__(self.Meta, key)
        # print(f"Meta '{key}' does not exist for field {self.__class__.__name__}")
        return False

    def sql(self): return Column(self.meta("field"), f"INTEGER")

