from core.commands.Command import Command
from core.commands.commands.HelpCommand import HelpCommand
from core.commands.commands.ListCommand import ListCommand
from core.commands.commands.migration.RunMigrationCommand import RunMigrationCommand
from core.commands.commands.migration.CreateMigrationCommand import CreateMigrationCommand

COMMANDS = {
    # "None": Command,
    "help": HelpCommand,
    "list": ListCommand,
    "make:migration": CreateMigrationCommand,
    "migration:migrate": RunMigrationCommand,
}
