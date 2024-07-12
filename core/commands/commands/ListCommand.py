from core.commands.Command import Command


class ListCommand(Command):

    NAME = "list"
    DESCRIPTION = "List available commands"
    USAGE = "%command%"

    def run(self):
        from core.configuration.commands import COMMANDS
        for command_str in COMMANDS.keys():
            command_cls = COMMANDS[command_str]
            print(f"python console {command_str} - {command_cls.DESCRIPTION}")
