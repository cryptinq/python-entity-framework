from pypika import Column

from core.orm.migration.schema.Field import Field


class PrimaryKey(Field):

    def __init__(self, field_name: str) -> None:
        super().__init__(field_name)

    class Meta:
        primary: bool = True

    def sql(self): return Column(self.meta("field"), "INT", nullable=False)
