from typing import Any

class Query:
    def __init__(self, sql_query: str, parameters: tuple[Any, ...] = ()):
        self.__sql_query: str
        self.__parameters: tuple[Any, ...]

        assert (isinstance(sql_query, str)), "SQL query must be a string"
        assert (isinstance(parameters, tuple)), "Query parameters must be a tuple"
        assert (sql_query.count("?") == len(parameters)), \
        "Query parameters must have the same length as the number of \"?\" in SQL query"

        self.__sql_query = sql_query
        self.__parameters = parameters

    @property
    def sql_query(self) -> str:
        return self.__sql_query

    @property
    def parameters(self) -> tuple[Any, ...]:
        return self.__parameters
