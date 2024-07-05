import sqlite3
from typing import Any
import os

from queries import Query

class Database:
    def __init__(self, filename: str):
        self.__filename: str = os.path.abspath(filename)
        self.__connection: None | sqlite3.Connection = None
        self.__cursor: None | sqlite3.Cursor = None
        self.__connect()

    def __del__(self):
        self.__disconnect()

    def __connect(self) -> None:
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

    def __disconnect(self) -> None:
        if self.__cursor is not None:
            self.__cursor.close()
        if self.__connection is not None:
            self.__connection.close()
