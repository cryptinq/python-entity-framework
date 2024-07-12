from sqeleton import connect, table, this


class DatabaseConnection:

    __INSTANCE = None
    @staticmethod
    def instance():
        return DatabaseConnection.__INSTANCE \
            if DatabaseConnection.__INSTANCE is not None \
            else DatabaseConnection()

    def __init__(self):
        DatabaseConnection.__INSTANCE = self
        self.database = None

    # @staticmethod
    # def initialize():
    #     DatabaseConnection.instance().database = connect("sqlite:///storage/database/database.db")

    @staticmethod
    def get(): return DatabaseConnection.instance().database
