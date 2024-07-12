from pypika import Column

from core.orm.migration.schema.Field import Field


class Integer(Field):

    # class Meta:
    #     min: int = 0
    #     max: int = 100000
    #
    # def min(self, min_value: int):
    #     self.Meta.min = min_value
    #     return self
    #
    # def max(self, max_value: int):
    #     self.Meta.max = max_value
    #     return self

    def sql(self): return Column(self.meta("field"), f"INTEGER")
