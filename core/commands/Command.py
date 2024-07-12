class Command:

    NAME = "None"
    DESCRIPTION = "Default command description"
    USAGE = "%command%"

    def run(self): print("Not implemented")
    def usage(self):
        return self.USAGE.replace(
            "%command%",
            f"python console {self.NAME}"
        )
