from database import Database
from queries import Queries, Query
import config

class RecipeBook():
    def __init__(self):
        initial_setup_queries: list[Query] = Queries.initial_setup_queries()
        self.__database: Database

        if config.STORE_IN_MEMORY:
            self.__database = Database(":memory:", config.LOG_FILE_PATH)
        else:
            self.__database = Database(config.DATABASE_FILE_PATH, config.LOG_FILE_PATH)
        for initial_setup_query in initial_setup_queries:
            self.__database.run_query(initial_setup_query)

    def insert_recipe_group(self, group_name: str) -> None:
        assert (isinstance(group_name, str))
        query: Query = Queries.insert_recipe_group_query(group_name)
        self.__database.run_query(query)

    def get_recipe_groups(self):
        query: Query = Queries.get_recipe_groups_query()
        results = self.__database.run_query(query)

        return results

def main():
    recipe_book = RecipeBook()
    #recipe_book.insert_recipe_group("Test Recipe Group")
    results = recipe_book.get_recipe_groups()
    print(dict(results))

if __name__ == "__main__":
    main()
