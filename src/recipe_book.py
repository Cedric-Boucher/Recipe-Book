from database import Database
from queries import Queries, Query
import config


def main():
    initial_setup_queries: list[Query] = Queries.initial_setup_queries()

    if config.STORE_IN_MEMORY:
        database: Database = Database(":memory:", config.LOG_FILE_PATH)
    else:
        database: Database = Database(config.DATABASE_FILE_PATH, config.LOG_FILE_PATH)
    for initial_setup_query in initial_setup_queries:
        database.run_query(initial_setup_query)


if __name__ == "__main__":
    main()
