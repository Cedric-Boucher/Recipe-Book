from database import Database
from queries import Queries, Query


def main():
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


if __name__ == "__main__":
    main()
