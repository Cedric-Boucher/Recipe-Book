from database import Database
from queries import Queries, Query
import config


def main():
    initial_setup_queries: list[Query] = Queries.initial_setup_queries()

    if config.STORE_IN_MEMORY:
        database: Database = Database(":memory:")
    else:
        database: Database = Database(config.DATABASE_FILE_PATH)
    database.connect()
    for initial_setup_query in initial_setup_queries:
        print(initial_setup_query)
        print(database.run_query(initial_setup_query))
    database.disconnect()


if __name__ == "__main__":
    main()
