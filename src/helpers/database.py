import sqlite3
import os

from helpers.logger import Logger
from data_types.query import Query

class Database:
    def __init__(self, filename: str, log_file_path: str):
        self.__logger: Logger = Logger(log_file_path)
        self.__logger.log("Starting Database")
        self.__filename: str = os.path.abspath(filename)
        self.__connection: None | sqlite3.Connection = None
        self.__cursor: None | sqlite3.Cursor = None

        folder: str = os.path.dirname(self.__filename)

        self.__logger.log("Using database file at '{}'".format(self.__filename))
        self.__logger.log("In folder '{}'".format(folder))

        if (not os.path.exists(folder) or not os.path.isdir(folder)):
            self.__logger.log("Specified folder for database file does not exist, creating it")
            os.makedirs(folder)
            self.__logger.log("Database folder recursively created")

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
        self.__logger.log("Running query:\n{query}\nwith parameters:\n{parameters}".format(
            query = query.sql_query,
            parameters = query.parameters
        ))
        self.__cursor.execute(query.sql_query, query.parameters)
        self.__connection.commit()
        self.__logger.log("Query executed, fetching results")
        results: list[sqlite3.Row] = self.__cursor.fetchall()
        if len(results) > 0:
            columns: list[str] = results[0].keys()
            self.__logger.log("Result columns:\n{columns}".format(columns = columns))
            results_string: str = str()
            for result in results:
                results_string += str(list(result))
                results_string += "\n"
            self.__logger.log("Results fetched:\n{results}".format(results = results_string))
        else:
            self.__logger.log("No results")

        return results

    @property
    def last_row_id(self) -> int | None:
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
