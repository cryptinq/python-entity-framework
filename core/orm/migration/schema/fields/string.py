from pypika import Column

from core.orm.migration.schema.Field import Field


class String(Field):
    class Meta:
        length: int = 255

    def length(self, str_length: int):
        self.Meta.length = str_length
        return self

    def sql(self): return Column(self.meta("field"), f"VARCHAR({self.meta('length')})", nullable=False)
