from typing import Optional

from core.orm.migration.Migration import Migration
from core.orm.migration.schema import Field


class UserMigration(Migration):

    class Meta:
        identifier: str = "c0em1o3r9jrx"
        table: str = "user"
        primary_key: Optional[str] = None

    def up(self):
        self.engine.create_table(self.table(), [
            Field.PRIMARY_KEY("id"),
            Field.STRING("name").length(50)
        ])

    def down(self):
        self.engine.drop_table(self.table())
