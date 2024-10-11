from helpers.database import Database, sqlite3
from queries import Queries, Query
from data_types.nutrition_info import Nutrition_Info
from data_types.ingredient import Ingredient
from data_types.recipe import Recipe
from data_types.tool import Tool
from data_types.picture import Picture
from data_types.instruction import Instruction
from data_types.ingredient_type import Ingredient_Type
from data_types.ingredient_brand import Ingredient_Brand
import config
import datetime


class Recipe_Book():
    def __init__(self):
        initial_setup_queries: list[Query] = Queries.initial_setup_queries()
        self.__database: Database

        if config.STORE_IN_MEMORY:
            self.__database = Database(":memory:", config.LOG_FILE_PATH)
        else:
            self.__database = Database(config.DATABASE_FILE_PATH, config.LOG_FILE_PATH)
        for initial_setup_query in initial_setup_queries:
            self.__database.run_query(initial_setup_query)

    def create_recipe(
            self,
            recipe_group_id: int,
            recipe_name: str,
            required_time_minutes: int | None,
            pictures: list[bytes],
            instructions: list[str],
            ingredient_ids_and_amounts: list[tuple[int, int]],
            tool_ids: list[int]
    ) -> int:
        recipe_id: int = self.__insert_recipe(recipe_group_id, recipe_name, required_time_minutes)
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

    def __insert_recipe(self, recipe_group_id: int, recipe_name: str, required_time_minutes: int | None) -> int:
        assert (isinstance(recipe_group_id, int))
        assert (recipe_group_id > 0)
        assert (isinstance(recipe_name, str))
        assert (isinstance(required_time_minutes, int) or required_time_minutes is None)
        if (isinstance(required_time_minutes, int)):
            assert (required_time_minutes > 0)

        query: Query = Queries.insert_recipe_query(recipe_group_id, recipe_name, required_time_minutes)
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
                nutrition_info.micrograms_of_iodide_per_kilogram,
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

    # TODO remove "dumb" getters that just return raw database data

    def get_recipes(self) -> list[sqlite3.Row]:
        query: Query = Queries.get_recipes_query()
        results: list[sqlite3.Row] = self.__database.run_query(query)

        return results

    def __get_recipe_info(self, recipe_id: int) -> tuple[str, int]:
        """returns (recipe_name, required_time_minutes)
        """
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        query: Query = Queries.get_recipe_query(recipe_id)
        results: list[sqlite3.Row] = self.__database.run_query(query)
        assert (len(results) == 1)
        recipe_name: str = results[0]["name"]
        required_time_minutes: int = results[0]["required_time_minutes"]

        return (recipe_name, required_time_minutes)

    def __get_recipe_group_for_recipe(self, recipe_id: int) -> str:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        query: Query = Queries.get_recipe_group_query(recipe_id)
        results: list[sqlite3.Row] = self.__database.run_query(query)
        assert (len(results) == 1)
        recipe_group_name: str = results[0]["name"]

        return recipe_group_name

    def __get_recipe_usage(self, recipe_id: int) -> list[datetime.datetime]:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        query: Query = Queries.get_recipe_usage_query(recipe_id)
        results: list[sqlite3.Row] = self.__database.run_query(query)
        recipe_usage_datetimes: list[datetime.datetime] = [
            datetime.datetime.strptime(result["datetime"], "%Y-%m-%d %H:%M:%S")
            for result
            in results
        ]

        return recipe_usage_datetimes

    def __get_tools_for_recipe(self, recipe_id: int) -> list[Tool]:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        query: Query = Queries.get_tools_query(recipe_id)
        results: list[sqlite3.Row] = self.__database.run_query(query)
        tools: list[Tool] = [result["name"] for result in results]

        return tools

    def __get_pictures_of_recipe(self, recipe_id: int) -> list[Picture]:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        query: Query = Queries.get_pictures_query(recipe_id)
        results: list[sqlite3.Row] = self.__database.run_query(query)
        pictures: list[Picture] = [result["picture"] for result in results]

        return pictures

    def __get_instructions_for_recipe(self, recipe_id: int) -> list[Instruction]:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        unsorted_instructions: list[tuple[int, Instruction]] = []
        query: Query = Queries.get_instructions_query(recipe_id)
        results: list[sqlite3.Row] = self.__database.run_query(query)
        for result in results:
            instruction_number: int = result["instruction_number"]
            instruction: Instruction = result["instruction"]
            unsorted_instructions.append((instruction_number, instruction))
        unsorted_instructions.sort(key = lambda x: x[0])
        instructions: list[Instruction] = [instruction[1] for instruction in unsorted_instructions]

        return instructions

    def __get_ingredients_in_recipe(self, recipe_id: int) -> list[Ingredient]:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        ingredients: list[Ingredient] = []
        query: Query = Queries.get_ingredients_query(recipe_id)
        results: list[sqlite3.Row] = self.__database.run_query(query)
        for result in results:
            ingredient_type: Ingredient_Type = result["ingredient_type"]
            ingredient_brand: Ingredient_Brand = result["ingredient_brand"]
            nutrition_info: Nutrition_Info = Nutrition_Info(
                result["l_per_kg"],
                result["kilocalories_per_kg"],
                result["g_fat_per_kg"],
                result["g_saturated_fat_per_kg"],
                result["g_trans_fat_per_kg"],
                result["g_carbohydrate_per_kg"],
                result["g_dietary_fibre_per_kg"],
                result["g_sugars_per_kg"],
                result["g_protein_per_kg"],
                result["g_cholesterol_per_kg"],
                result["mg_sodium_per_kg"],
                result["mg_potassium_per_kg"],
                result["mg_calcium_per_kg"],
                result["mg_iron_per_kg"],
                bool(result["has_gluten"]),
                bool(result["is_meat"]),
                bool(result["is_dairy"]),
                bool(result["is_animal_product"]),
                bool(result["is_nut"]),
                bool(result["is_soy"]),
                result["g_omega6_polyunsaturated_fat_per_kg"],
                result["g_omega3_polyunsaturated_fat_per_kg"],
                result["g_monounsaturated_fat_per_kg"],
                result["g_soluble_fibre_per_kg"],
                result["g_insoluble_fibre_per_kg"],
                result["g_sugar_alcohols_per_kg"],
                result["g_starch_per_kg"],
                result["ug_vitamin_a_per_kg"],
                result["mg_vitamin_c_per_kg"],
                result["ug_vitamin_d_per_kg"],
                result["mg_vitamin_e_per_kg"],
                result["ug_vitamin_k_per_kg"],
                result["mg_thiamine_per_kg"],
                result["mg_riboflavin_per_kg"],
                result["mg_niacin_per_kg"],
                result["mg_vitamin_b6_per_kg"],
                result["ug_folate_per_kg"],
                result["ug_vitamin_b12_per_kg"],
                result["ug_biotin_per_kg"],
                result["mg_pantothenate_per_kg"],
                result["mg_choline_per_kg"],
                result["mg_phosphorous_per_kg"],
                result["ug_iodide_per_kg"],
                result["mg_magnesium_per_kg"],
                result["mg_zinc_per_kg"],
                result["ug_selenium_per_kg"],
                result["mg_copper_per_kg"],
                result["mg_manganese_per_kg"],
                result["ug_chromium_per_kg"],
                result["ug_molybdenum_per_kg"],
                result["mg_chloride_per_kg"]
            )
            amount_grams: int = result["amount_grams"]
            ingredient: Ingredient = Ingredient(
                ingredient_type,
                ingredient_brand,
                nutrition_info,
                amount_grams
            )
            ingredients.append(ingredient)

        return ingredients

    def get_all_recipe_information(self, recipe_id: int) -> Recipe:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)

        # get info from recipes table
        recipe_name: str
        required_time_minutes: int
        recipe_name, required_time_minutes = self.__get_recipe_info(recipe_id)
        recipe_group_name: str = self.__get_recipe_group_for_recipe(recipe_id)
        ingredients: list[Ingredient] = self.__get_ingredients_in_recipe(recipe_id)
        instructions: list[Instruction] = self.__get_instructions_for_recipe(recipe_id)
        tools: list[Tool] = self.__get_tools_for_recipe(recipe_id)
        pictures: list[Picture] = self.__get_pictures_of_recipe(recipe_id)
        recipe_usage_datetimes: list[datetime.datetime] = self.__get_recipe_usage(recipe_id)

        # combine all results into Recipe object
        recipe: Recipe = Recipe(
            recipe_name,
            recipe_group_name,
            ingredients,
            instructions,
            tools,
            pictures,
            required_time_minutes,
            recipe_usage_datetimes
        )

        return recipe


def main():
    pass


if __name__ == "__main__":
    main()
