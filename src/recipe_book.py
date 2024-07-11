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

    def insert_tool(self, tool_name: str) -> int:
        assert (isinstance(tool_name, str))
        query: Query = Queries.insert_tool_query(tool_name)
        self.__database.run_query(query)
        tool_id: int | None = self.__database.get_last_row_id()
        assert (tool_id is not None)

        return tool_id

    def insert_picture(self, picture: bytes) -> int:
        assert (isinstance(picture, bytes))
        query: Query = Queries.insert_picture_query()
        self.__database.run_query_insert_blob(query, (picture,))
        picture_id: int | None = self.__database.get_last_row_id()
        assert (picture_id is not None)

        return picture_id

    def get_recipe_groups(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_recipe_groups_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results

    def get_recipes(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_recipes_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results

    def get_tools(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_tools_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results

    def get_pictures(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_pictures_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results

    def get_instructions(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_instructions_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results


def main():
    recipe_book = RecipeBook()
    #recipe_group_id = recipe_book.insert_recipe_group("Test Recipe Group")
    #recipe_id = recipe_book.insert_recipe(recipe_group_id, "Test Recipe")
    recipe_groups: list[sqlite3.Row] = recipe_book.get_recipe_groups()
    if len(recipe_groups) > 0:
        columns: list[str] = recipe_groups[0].keys()
        print("RECIPE GROUPS:")
        for recipe_group in recipe_groups:
            print("[")
            [print("{}: {}".format(column, recipe_group[column])) for column in columns]
            print("]")

    recipes: list[sqlite3.Row] = recipe_book.get_recipes()
    if len(recipes) > 0:
        columns: list[str] = recipes[0].keys()
        print("RECIPES:")
        for recipe in recipes:
            print("[")
            [print("{}: {}".format(column, recipe[column])) for column in columns]
            print("]")

    tools: list[sqlite3.Row] = recipe_book.get_tools()
    if len(tools) > 0:
        columns: list[str] = tools[0].keys()
        print("TOOLS:")
        for tool in tools:
            print("[")
            [print("{}: {}".format(column, tool[column])) for column in columns]
            print("]")

    pictures: list[sqlite3.Row] = recipe_book.get_pictures()
    if len(pictures) > 0:
        columns: list[str] = pictures[0].keys()
        print("TOOLS:")
        for picture in pictures:
            print("[")
            [print("{}: {}".format(column, picture[column])) for column in columns]
            print("]")

    instructions: list[sqlite3.Row] = recipe_book.get_instructions()
    if len(instructions) > 0:
        columns: list[str] = instructions[0].keys()
        print("TOOLS:")
        for instruction in instructions:
            print("[")
            [print("{}: {}".format(column, instruction[column])) for column in columns]
            print("]")


if __name__ == "__main__":
    main()
