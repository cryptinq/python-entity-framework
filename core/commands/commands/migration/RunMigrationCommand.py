import os.path
import string
import sys
from datetime import datetime
import random
from typing import Optional

from core.commands.Command import Command
from core.helpers.file.FileSystem import FileSystem as fs
from core.orm.migration.Migration import Migration


class RunMigrationCommand(Command):

    NAME = "migration:migrate"
    DESCRIPTION = "Execute migration"
    USAGE = "%command% [identifier] <up | down>"

    def run(self):

        migration_identifier = sys.argv[2] if len(sys.argv) > 2 else None
        if migration_identifier is None: exit(f"Migration identifier is needed - {self.usage()}")

        if not os.path.isfile(fs.from_root("storage/cache/migration.py")):
            exit(f"Migration identifier '{migration_identifier}' does not exist")

        from storage.cache.migration import MIGRATIONS
        migration_cache = MIGRATIONS

        if migration_identifier not in migration_cache.keys():
            exit(f"Migration identifier '{migration_identifier}' does not exist")

        migration_class: Migration = migration_cache[migration_identifier]["class"]

        migration_direction = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] in ["up", "down"] else "up"
        if migration_direction == "up": (migration_class()).up()
        if migration_direction == "down": (migration_class()).down()

        print(f"Migration completed: {migration_identifier}")
