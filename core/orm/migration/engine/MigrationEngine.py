from typing import List, Tuple, Union

from pypika import Table, Query, Schema

from core.orm.connection.DatabaseConnection import DatabaseConnection
from core.orm.migration.schema.Field import Field


class MigrationEngine:

    @staticmethod
    def database():
        return DatabaseConnection.instance().database

    @classmethod
    def create_table(cls, table_name: str, table_schema: list[Field]) -> None:
        serialized_scheme = [field.sql() for field in table_schema]
        q = Query.create_table(Table(table_name)).columns(*serialized_scheme)
        for field in table_schema:
            if field.meta("primary"): q = q.primary_key(field.sql())
        print(str(q))
        # result = cls.database().query(tbl.create(), bool)
        # if not result: exit(f"An error occured while creating table {table_name}")

    @classmethod
    def drop_table(cls, table_name: str) -> None:
        pass
        # tbl = table(table_name)
        # result = cls.database().query(tbl.drop(), bool)
        # if not result: exit(f"An error occured while dropping table {table_name}")
