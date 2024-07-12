from core.commands.Command import Command


class HelpCommand(Command):

    NAME = "help"
    DESCRIPTION = "Help command"
    USAGE = "%command% [command]"

    def run(self):
        print("Not implemented")
