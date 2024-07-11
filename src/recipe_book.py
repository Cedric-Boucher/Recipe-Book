from database import Database, sqlite3
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

    def insert_recipe_group(self, group_name: str) -> int:
        assert (isinstance(group_name, str))
        query: Query = Queries.insert_recipe_group_query(group_name)
        self.__database.run_query(query)
        recipe_group_id: int | None = self.__database.get_last_row_id()
        assert (recipe_group_id is not None)

        return recipe_group_id

    def insert_recipe(self, recipe_group_id: int, recipe_name: str) -> int:
        assert (isinstance(recipe_group_id, int))
        assert (recipe_group_id > 0)
        assert (isinstance(recipe_name, str))
        query: Query = Queries.insert_recipe_query(recipe_group_id, recipe_name)
        self.__database.run_query(query)
        recipe_id: int | None = self.__database.get_last_row_id()
        assert (recipe_id is not None)

        return recipe_id

    def get_recipe_groups(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_recipe_groups_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results

    def get_recipes(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_recipes_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results

def main():
    recipe_book = RecipeBook()
    #recipe_group_id = recipe_book.insert_recipe_group("Test Recipe Group")
    #recipe_id = recipe_book.insert_recipe(recipe_group_id, "Test Recipe")
    recipe_groups: list[sqlite3.Row] = recipe_book.get_recipe_groups()
    if recipe_groups is not None:
        columns: list[str] = recipe_groups[0].keys()
        print("RECIPE GROUPS:")
        for recipe_group in recipe_groups:
            print("[")
            [print("{}: {}".format(column, recipe_group[column])) for column in columns]
            print("]")

    recipes: list[sqlite3.Row] = recipe_book.get_recipes()
    if recipes is not None:
        columns: list[str] = recipes[0].keys()
        print("RECIPES:")
        for recipe in recipes:
            print("[")
            [print("{}: {}".format(column, recipe[column])) for column in columns]
            print("]")

if __name__ == "__main__":
    main()
