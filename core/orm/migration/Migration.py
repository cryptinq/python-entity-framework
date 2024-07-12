from typing import Optional

from core.orm.migration.engine.MigrationEngine import MigrationEngine


class Migration:

    engine = MigrationEngine

    class Meta:
        table: str = "%TABLE%"
        primary_key: Optional[str] = False

    def up(self): pass
    def down(self): pass

    def meta(self, key):
        if key in dir(self.Meta): return self.Meta.__getattribute__(self.Meta, key)
        exit(f"Meta {key} does not exist for migration {self.__class__.__name__}")

    def table(self): return self.meta("table")
