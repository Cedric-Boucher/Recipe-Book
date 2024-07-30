from database import Database, sqlite3
from queries import Queries, Query
from nutrition_info import Nutrition_Info
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

    # TODO make some bigger functions to do multiple things in one go:
    # TODO create smarter code that will do EVERYTHING in one function, insert things if necessary otherwise link existing

    # using something in (recipe_group, tool, ingredient, ingredient_brand, ingredient_type)
    # should be a dropdown selection for users so they are incentivized to use existing options,
    # with a way to create a new one if needed

    def create_recipe(
            self,
            recipe_group_id: int,
            recipe_name: str,
            pictures: list[bytes],
            instructions: list[str],
            ingredient_ids_and_amounts: list[tuple[int, int]],
            tool_ids: list[int]
    ) -> int:
        recipe_id: int = self.__insert_recipe(recipe_group_id, recipe_name)
        for picture in pictures:
            picture_id: int = self.__insert_picture(picture)
            self.__link_picture_to_recipe(recipe_id, picture_id)
        for instruction_number, instruction in enumerate(instructions):
            instruction_id: int = self.__insert_instruction(instruction)
            self.__link_instruction_to_recipe(recipe_id, instruction_id, instruction_number+1)
        for ingredient_id_and_amount in ingredient_ids_and_amounts:
            ingredient_id: int = ingredient_id_and_amount[0]
            ingredient_amount: int = ingredient_id_and_amount[1]
            self.__link_ingredient_to_recipe(recipe_id, ingredient_id, ingredient_amount)
        for tool_id in tool_ids:
            self.__link_tool_to_recipe(recipe_id, tool_id)

        return recipe_id

    def create_ingredient(
            self,
            ingredient_type_id: int,
            ingredient_brand_id: int,
            nutrition_info: Nutrition_Info
    ) -> int:
        nutrition_info_id: int = self.__insert_nutrition_info(nutrition_info)
        ingredient_id: int = self.__insert_ingredient(ingredient_type_id, ingredient_brand_id, nutrition_info_id)

        return ingredient_id

    def insert_recipe_group(self, group_name: str) -> int:
        assert (isinstance(group_name, str))
        query: Query = Queries.insert_recipe_group_query(group_name)
        self.__database.run_query(query)
        recipe_group_id: int | None = self.__database.get_last_row_id()
        assert (recipe_group_id is not None)

        return recipe_group_id

    def __insert_recipe(self, recipe_group_id: int, recipe_name: str) -> int:
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

    def __insert_picture(self, picture: bytes) -> int:
        assert (isinstance(picture, bytes))
        query: Query = Queries.insert_picture_query()
        self.__database.run_query_insert_blob(query, (picture,))
        picture_id: int | None = self.__database.get_last_row_id()
        assert (picture_id is not None)

        return picture_id

    def __insert_instruction(self, instruction: str) -> int:
        assert (isinstance(instruction, str))
        query: Query = Queries.insert_instruction_query(instruction)
        self.__database.run_query(query)
        instruction_id: int | None = self.__database.get_last_row_id()
        assert (instruction_id is not None)

        return instruction_id

    def __insert_ingredient(self, ingredient_type_id: int, ingredient_brand_id: int, nutrition_info_id: int) -> int:
        assert (isinstance(ingredient_type_id, int))
        assert (ingredient_type_id > 0)
        assert (isinstance(ingredient_brand_id, int))
        assert (ingredient_brand_id > 0)
        assert (isinstance(nutrition_info_id, int))
        assert (nutrition_info_id > 0)
        query: Query = Queries.insert_ingredient_query(ingredient_type_id, ingredient_brand_id, nutrition_info_id)
        self.__database.run_query(query)
        ingredient_id: int | None = self.__database.get_last_row_id()
        assert (ingredient_id is not None)

        return ingredient_id

    def insert_ingredient_type(self, ingredient_type_name: str) -> int:
        assert (isinstance(ingredient_type_name, str))
        query: Query = Queries.insert_ingredient_type_query(ingredient_type_name)
        self.__database.run_query(query)
        ingredient_type_id: int | None = self.__database.get_last_row_id()
        assert (ingredient_type_id is not None)

        return ingredient_type_id

    def insert_ingredient_brand(self, ingredient_brand_name: str) -> int:
        assert (isinstance(ingredient_brand_name, str))
        query: Query = Queries.insert_ingredient_brand_query(ingredient_brand_name)
        self.__database.run_query(query)
        ingredient_brand_id: int | None = self.__database.get_last_row_id()
        assert (ingredient_brand_id is not None)

        return ingredient_brand_id

    def __insert_nutrition_info(self, nutrition_info: Nutrition_Info) -> int:
        assert (isinstance(nutrition_info, Nutrition_Info))
        query: Query = Queries.insert_nutrition_info_query(
                nutrition_info.litres_per_kilogram,
                nutrition_info.kilocalories_per_kilogram,
                nutrition_info.grams_of_fat_per_kilogram,
                nutrition_info.grams_of_saturated_fat_per_kilogram,
                nutrition_info.grams_of_trans_fat_per_kilogram,
                nutrition_info.grams_of_carbohydrate_per_kilogram,
                nutrition_info.grams_of_dietary_fibre_per_kilogram,
                nutrition_info.grams_of_sugars_per_kilogram,
                nutrition_info.grams_of_protein_per_kilogram,
                nutrition_info.grams_of_cholesterol_per_kilogram,
                nutrition_info.milligrams_of_sodium_per_kilogram,
                nutrition_info.milligrams_of_potassium_per_kilogram,
                nutrition_info.milligrams_of_calcium_per_kilogram,
                nutrition_info.milligrams_of_iron_per_kilogram,
                nutrition_info.has_gluten,
                nutrition_info.is_meat,
                nutrition_info.is_dairy,
                nutrition_info.is_animal_product,
                nutrition_info.is_nut,
                nutrition_info.is_soy,
                nutrition_info.grams_of_omega6_polyunsaturated_fat_per_kilogram,
                nutrition_info.grams_of_omega3_polyunsaturated_fat_per_kilogram,
                nutrition_info.grams_of_monounsaturated_fat_per_kilogram,
                nutrition_info.grams_of_soluble_fibre_per_kilogram,
                nutrition_info.grams_of_insoluble_fibre_per_kilogram,
                nutrition_info.grams_of_sugar_alcohols_per_kilogram,
                nutrition_info.grams_of_starch_per_kilogram,
                nutrition_info.micrograms_of_vitamin_a_per_kilogram,
                nutrition_info.milligrams_of_vitamin_c_per_kilogram,
                nutrition_info.micrograms_of_vitamin_d_per_kilogram,
                nutrition_info.milligrams_of_vitamin_e_per_kilogram,
                nutrition_info.micrograms_of_vitamin_k_per_kilogram,
                nutrition_info.milligrams_of_thiamine_per_kilogram,
                nutrition_info.milligrams_of_riboflavin_per_kilogram,
                nutrition_info.milligrams_of_niacin_per_kilogram,
                nutrition_info.milligrams_of_vitamin_b6_per_kilogram,
                nutrition_info.micrograms_of_folate_per_kilogram,
                nutrition_info.micrograms_of_vitamin_b12_per_kilogram,
                nutrition_info.micrograms_of_biotin_per_kilogram,
                nutrition_info.milligrams_of_pantothenate_per_kilogram,
                nutrition_info.milligrams_of_choline_per_kilogram,
                nutrition_info.milligrams_of_phosphorous_per_kilogram,
                nutrition_info.micrograms_of_iodide_per_kilograms,
                nutrition_info.milligrams_of_magnesium_per_kilogram,
                nutrition_info.milligrams_of_zinc_per_kilogram,
                nutrition_info.micrograms_of_selenium_per_kilogram,
                nutrition_info.milligrams_of_copper_per_kilogram,
                nutrition_info.milligrams_of_manganese_per_kilogram,
                nutrition_info.micrograms_of_chromium_per_kilogram,
                nutrition_info.micrograms_of_molybdenum_per_kilogram,
                nutrition_info.milligrams_of_chloride_per_kilogram
        )
        self.__database.run_query(query)
        nutrition_info_id: int | None = self.__database.get_last_row_id()
        assert (nutrition_info_id is not None)

        return nutrition_info_id

    def __link_ingredient_to_recipe(self, recipe_id: int, ingredient_id: int, amount_grams: int) -> int:
        assert (isinstance(ingredient_id, int))
        assert (ingredient_id > 0)
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(amount_grams, int))
        assert (amount_grams > 0)
        query: Query = Queries.insert_recipe_ingredient_query(recipe_id, ingredient_id, amount_grams)
        self.__database.run_query(query)
        recipe_ingredient_id: int | None = self.__database.get_last_row_id()
        assert (recipe_ingredient_id is not None)

        return recipe_ingredient_id

    def __link_instruction_to_recipe(self, recipe_id: int, instruction_id: int, instruction_number: int) -> int:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(instruction_id, int))
        assert (instruction_id > 0)
        assert (isinstance(instruction_number, int))
        assert (instruction_number > 0)
        query: Query = Queries.insert_recipe_instruction_query(recipe_id, instruction_id, instruction_number)
        self.__database.run_query(query)
        recipe_instruction_id: int | None = self.__database.get_last_row_id()
        assert (recipe_instruction_id is not None)

        return recipe_instruction_id

    def __link_picture_to_recipe(self, recipe_id: int, picture_id: int) -> int:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(picture_id, int))
        assert (picture_id > 0)
        query: Query = Queries.insert_recipe_picture_query(recipe_id, picture_id)
        self.__database.run_query(query)
        recipe_picture_id: int | None = self.__database.get_last_row_id()
        assert (recipe_picture_id is not None)

        return recipe_picture_id

    def __link_tool_to_recipe(self, recipe_id: int, tool_id: int) -> int:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(tool_id, int))
        assert (tool_id > 0)
        query: Query = Queries.insert_recipe_tool_query(recipe_id, tool_id)
        self.__database.run_query(query)
        recipe_tool_id: int | None = self.__database.get_last_row_id()
        assert (recipe_tool_id is not None)

        return recipe_tool_id

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

    def get_ingredient(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_ingredients_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results

    def get_all_recipe_information(self, recipe_id: int) -> list[sqlite3.Row]:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        return [] # TODO


def main():
    recipe_book = RecipeBook()
    recipe_group_id = recipe_book.insert_recipe_group("Test Recipe Group")
    tool_id = recipe_book.insert_tool("Test Tool")
    ingredient_type_id = recipe_book.insert_ingredient_type("Test Ingredient Type")
    ingredient_brand_id = recipe_book.insert_ingredient_brand("Test Ingredient Brand")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id,
        Nutrition_Info(
            0.0,
            0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            False,
            False,
            False,
            False,
            False,
            False
        )
    )
    recipe_id = recipe_book.create_recipe(recipe_group_id, "Test Recipe", [bytes(range(64))], ["Test Instruction"], [(ingredient_id, 1)], [tool_id])
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

    everything = recipe_book.get_all_recipe_information(recipe_id)
    print(everything)


if __name__ == "__main__":
    main()
