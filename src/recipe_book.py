import sqlite3
from typing import Any
import os
from queries import Queries, Query

class Database:
    def __init__(self, filename: str):
        self.__filename: str = os.path.abspath(filename)
        self.__connection: None | sqlite3.Connection = None
        self.__cursor: None | sqlite3.Cursor = None

    def connect(self) -> None:
        try:
            self.__connection = sqlite3.connect(self.__filename)
            print("sqlite3 version: {}".format(sqlite3.sqlite_version))
        except sqlite3.Error as e:
            print("SQLITE ERROR: {}".format(e))

        if self.__connection is not None:
            try:
                self.__cursor = self.__connection.cursor()
            except sqlite3.Error as e:
                print("SQLITE ERROR: {}".format(e))

    def run_query(self, query: Query) -> list[Any]:
        assert (self.__cursor is not None)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def disconnect(self) -> None:
        if self.__cursor is not None:
            self.__cursor.close()
        if self.__connection is not None:
            self.__connection.close()

if __name__ == "__main__":
    initial_setup_queries: list[Query] = Queries.initial_setup_queries()

    STORE_IN_MEMORY: bool = False
    DATABASE_FILE_PATH: str = "C:/Users/onebi/Documents/GitHub/Recipe-Book/database/recipe_book.sqlite3"

    if STORE_IN_MEMORY:
        database: Database = Database(":memory:")
    else:
        database: Database = Database(DATABASE_FILE_PATH)
    database.connect()
    for initial_setup_query in initial_setup_queries:
        print(initial_setup_query)
        print(database.run_query(initial_setup_query))
    database.disconnect()
