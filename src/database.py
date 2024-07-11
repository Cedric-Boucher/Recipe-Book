import sqlite3
import apsw.ext
from typing import Any
import os

from queries import Query
from logger import Logger

class Database:
    def __init__(self, filename: str, log_file_path: str):
        self.__logger: Logger = Logger(log_file_path)
        self.__logger.log("Starting Database")
        self.__filename: str = os.path.abspath(filename)
        self.__connection: None | sqlite3.Connection = None
        self.__cursor: None | sqlite3.Cursor = None
        self.__connect()

    def __del__(self):
        self.__disconnect()
        self.__logger.log("Ending database")

    def __connect(self) -> None:
        self.__logger.log("Connecting to database")
        try:
            self.__connection = sqlite3.connect(self.__filename)
            self.__logger.log("SQLITE version: {}".format(sqlite3.sqlite_version))
        except sqlite3.Error as e:
            self.__logger.log("SQLITE ERROR: {}: {}".format(type(e).__name__, str(e)))

        if self.__connection is not None:
            try: 
                self.__connection.row_factory = sqlite3.Row
                self.__cursor = self.__connection.cursor()
            except sqlite3.Error as e:
                self.__logger.log("SQLITE ERROR: {}: {}".format(type(e).__name__, str(e)))

        if self.__connection is not None and self.__cursor is not None:
            self.__logger.log("Successfully connected to database")
        else:
            self.__logger.log("Failed to connect to database")

    def run_query(self, query: Query) -> list[sqlite3.Row]:
        assert (self.__connection is not None)
        assert (self.__cursor is not None)
        self.__logger.log("Running query:\n{query}".format(query = query))
        self.__cursor.execute(query)
        self.__connection.commit()
        self.__logger.log("Query executed, fetching results")
        results= self.__cursor.fetchall()
        self.__logger.log("Results fetched:\n{results}".format(results = str(results)))

        return results

    def get_last_row_id(self) -> int | None:
        assert (self.__connection is not None)
        assert (self.__cursor is not None)
        row_id: int | None = self.__cursor.lastrowid

        return row_id

    def __disconnect(self) -> None:
        self.__logger.log("Disconnecting from database")
        if self.__cursor is not None:
            self.__cursor.close()
        if self.__connection is not None:
            self.__connection.commit()
            self.__connection.close()
        self.__logger.log("Disconnected from database")
