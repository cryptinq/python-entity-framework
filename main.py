import sys

from core.commands.Command import Command
from core.configuration.commands import COMMANDS
from core.orm.connection.DatabaseConnection import DatabaseConnection

if __name__ == '__main__':

    commands = COMMANDS
    user_command = sys.argv[1] if len(sys.argv) > 1 else None

    if not len(sys.argv) > 1: exit("Too few arguments given")
    if user_command not in commands: exit(f'Command "{user_command}" not found.')

    # DatabaseConnection.initialize()

    command: Command = commands[user_command]
    (command()).run()

