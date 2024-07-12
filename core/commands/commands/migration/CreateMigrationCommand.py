import os.path
import string
import sys
from datetime import datetime
import random
from typing import Optional

from core.commands.Command import Command
from core.helpers.file.FileSystem import FileSystem as fs


class CreateMigrationCommand(Command):

    NAME = "make:migration"
    DESCRIPTION = "Make migration"
    USAGE = "%command% [name] [table] <primary_key>"

    def run(self):

        allowed_chars = string.ascii_lowercase + string.digits + "_"

        migration_name = sys.argv[2].lower() if len(sys.argv) > 2 else None
        if migration_name is None: exit(f"Migration name is needed - {self.usage()}")
        
        for char in migration_name:
            if char not in allowed_chars:
                exit(f"Migration name is invalid, unallowed char {char}")

        migration_table = sys.argv[3] if len(sys.argv) > 3 else None
        if migration_table is None: exit(f"Table name is needed - {self.usage()}")

        primary_key = sys.argv[4] if len(sys.argv) > 4 else "None"

        if not os.path.isdir(fs.from_root("database")):
            os.mkdir(fs.from_root("database"))

        if not os.path.isdir(fs.from_root("database/migrations")):
            os.mkdir(fs.from_root("database/migrations"))

        if not os.path.isdir(fs.from_root("storage")):
            os.mkdir(fs.from_root("storage"))

        if not os.path.isdir(fs.from_root("storage/cache")):
            os.mkdir(fs.from_root("storage/cache"))

        stub_content = fs.content(fs.from_root("core/stubs/migration.stub"))

        chars = allowed_chars.replace("_", "")
        replacements = {
            "%TABLE%": migration_table,
            "%PRIMARY_KEY%": primary_key,
            "%IDENTIFIER%": "".join(
                chars[random.randint(0, len(chars) - 1)] for _ in range(12)
            ),
            "%MIGRATION_CLASS_NAME%": migration_table.capitalize()
        }

        for replacement in replacements.keys(): stub_content = stub_content.replace(
            replacement, replacements[replacement]
        )

        creation_time = datetime.now().strftime("%Y%m%d%H%M%S")
        migration_file_name = f"m{creation_time}_{migration_name}.py"

        migration_cache: Optional[dict[str, dict]] = {
            replacements["%IDENTIFIER%"]: {
                "file": migration_file_name,
                "class": f"{replacements['%MIGRATION_CLASS_NAME%']}Migration"
            },
        }

        if os.path.isfile(fs.from_root("storage/cache/migrations.py")):
            from storage.cache.migrations import MIGRATIONS
            migration_cache = migration_cache | MIGRATIONS
            fs.remove(fs.from_root("storage/cache/migrations.py"))

        fs.write(
            fs.from_root(f"database/migrations/{migration_file_name}"),
            stub_content,
        )

        stub_content = fs.content(fs.from_root("core/stubs/migration_cache.stub"))

        replacements = {
            "%CACHE%": str(migration_cache),
            "%IMPORTS%": "\n".join([
                f'from database.migrations.{migration_cache[migration_identifier]["file"].replace(".py", "")} '
                f'import {migration_cache[migration_identifier]["class"]}'
                for migration_identifier in migration_cache.keys()
            ])
        }

        for replacement in replacements.keys(): stub_content = stub_content.replace(
            replacement, replacements[replacement]
        )

        for migration_identifier in migration_cache.keys():
            migration_class = migration_cache[migration_identifier]["class"]
            stub_content = stub_content.replace(f"'{migration_class}'", f'{migration_class}')

        fs.write(
            fs.from_root(f"storage/cache/migration.py"),
            stub_content,
        )

        print(f"Created {migration_name} at 'database/migrations/{migration_file_name}'")
