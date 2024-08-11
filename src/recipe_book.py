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
    recipe_book: Recipe_Book = Recipe_Book()

    # create cream of broccoli soup recipe
    recipe_group_id = recipe_book.insert_recipe_group("Cream of Broccoli Soup")
    tool_ids: list[int] = [
        recipe_book.insert_tool(tool)
        for tool
        in [
            "Large Pot",
            "Blender"
        ]
    ]
    ingredient_ids_and_amounts: list[tuple[int, int]] = []

    ingredient_brand_id_health_canada = recipe_book.insert_ingredient_brand("Health Canada")

    ingredient_type_id = recipe_book.insert_ingredient_type("Butter")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id_health_canada,
        Nutrition_Info(
            1/0.959,
            7170,
            811.1,
            513.68,
            46.39,
            0.6,
            0.0,
            0.6,
            8.5,
            2.15,
            6430.0,
            240.0,
            240.0,
            0.2,
            False,
            False,
            True,
            True,
            False,
            False,
            21.6,
            3.1,
            210.21,
            milligrams_of_vitamin_c_per_kilogram=0.0,
            micrograms_of_vitamin_d_per_kilogram=6.0,
            micrograms_of_vitamin_k_per_kilogram=70.0,
            milligrams_of_thiamine_per_kilogram=0.05,
            milligrams_of_riboflavin_per_kilogram=0.34,
            milligrams_of_niacin_per_kilogram=0.42,
            milligrams_of_vitamin_b6_per_kilogram=0.03,
            micrograms_of_vitamin_b12_per_kilogram=0.17,
            micrograms_of_folate_per_kilogram=30.0,
            milligrams_of_pantothenate_per_kilogram=1.1,
            milligrams_of_choline_per_kilogram=188.0,
            milligrams_of_phosphorous_per_kilogram=240.0,
            milligrams_of_magnesium_per_kilogram=20.0,
            milligrams_of_zinc_per_kilogram=0.9,
            micrograms_of_selenium_per_kilogram=10.0,
            milligrams_of_copper_per_kilogram=0.0,
            milligrams_of_manganese_per_kilogram=0.0
        )
    )
    ingredient_ids_and_amounts.append((ingredient_id, 15))

    ingredient_type_id = recipe_book.insert_ingredient_type("Yellow Onion")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id_health_canada,
        Nutrition_Info(
            1/368,
            1320,
            108.0,
            14.77,
            0.0,
            78.6,
            17.0,
            43.9,
            9.5,
            0.0,
            120.0,
            1330.0,
            200.0,
            2.7,
            False,
            False,
            False,
            False,
            False,
            False,
            grams_of_monounsaturated_fat_per_kilogram=21.85,
            milligrams_of_vitamin_c_per_kilogram=18.0,
            micrograms_of_vitamin_d_per_kilogram=0.0,
            micrograms_of_vitamin_k_per_kilogram=216.0,
            milligrams_of_thiamine_per_kilogram=0.49,
            milligrams_of_riboflavin_per_kilogram=0.41,
            milligrams_of_niacin_per_kilogram=0.37,
            milligrams_of_vitamin_b6_per_kilogram=2.07,
            micrograms_of_vitamin_b12_per_kilogram=0.0,
            milligrams_of_pantothenate_per_kilogram=1.72,
            milligrams_of_choline_per_kilogram=65.0,
            milligrams_of_phosphorous_per_kilogram=330.0,
            milligrams_of_magnesium_per_kilogram=90.0,
            milligrams_of_zinc_per_kilogram=2.1,
            milligrams_of_copper_per_kilogram=0.17,
            milligrams_of_manganese_per_kilogram=1.02
        )
    )
    ingredient_ids_and_amounts.append((ingredient_id, 175))

    ingredient_type_id = recipe_book.insert_ingredient_type("Garlic")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id_health_canada,
        Nutrition_Info(
            1/0.575,
            1490,
            5.0,
            0.89,
            0.0,
            330.6,
            21.0,
            10.0,
            63.6,
            0.0,
            170.0,
            4010.0,
            1810.0,
            17.0,
            False,
            False,
            False,
            False,
            False,
            False,
            grams_of_monounsaturated_fat_per_kilogram=0.11,
            milligrams_of_vitamin_c_per_kilogram=312.0,
            micrograms_of_vitamin_d_per_kilogram=0.0,
            micrograms_of_vitamin_k_per_kilogram=17.0,
            milligrams_of_thiamine_per_kilogram=2.0,
            milligrams_of_riboflavin_per_kilogram=1.1,
            milligrams_of_niacin_per_kilogram=7.0,
            milligrams_of_vitamin_b6_per_kilogram=12.35,
            micrograms_of_vitamin_b12_per_kilogram=0.0,
            milligrams_of_pantothenate_per_kilogram=5.96,
            milligrams_of_choline_per_kilogram=232.0,
            milligrams_of_phosphorous_per_kilogram=1530.0,
            milligrams_of_magnesium_per_kilogram=250.0,
            milligrams_of_zinc_per_kilogram=11.6,
            micrograms_of_selenium_per_kilogram=142.0,
            milligrams_of_copper_per_kilogram=2.99,
            milligrams_of_manganese_per_kilogram=16.72
        )
    )
    ingredient_ids_and_amounts.append((ingredient_id, 9))

    ingredient_type_id = recipe_book.insert_ingredient_type("Broccoli")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id_health_canada,
        Nutrition_Info(
            1/372,
            340,
            3.7,
            0.39,
            0.0,
            66.4,
            24.0,
            17.0,
            28.2,
            0.0,
            330.0,
            3160.0,
            470.0,
            7.3,
            False,
            False,
            False,
            False,
            False,
            False,
            grams_of_monounsaturated_fat_per_kilogram=0.11,
            milligrams_of_vitamin_c_per_kilogram=892.0,
            micrograms_of_vitamin_d_per_kilogram=0.0,
            micrograms_of_vitamin_k_per_kilogram=1016.0,
            milligrams_of_thiamine_per_kilogram=0.71,
            milligrams_of_riboflavin_per_kilogram=1.17,
            milligrams_of_niacin_per_kilogram=6.39,
            milligrams_of_vitamin_b6_per_kilogram=1.75,
            micrograms_of_vitamin_b12_per_kilogram=0.0,
            milligrams_of_pantothenate_per_kilogram=5.73,
            milligrams_of_phosphorous_per_kilogram=660.0,
            milligrams_of_magnesium_per_kilogram=210.0,
            milligrams_of_zinc_per_kilogram=4.1,
            micrograms_of_selenium_per_kilogram=25.0,
            milligrams_of_copper_per_kilogram=0.49,
            milligrams_of_manganese_per_kilogram=2.1
        )
    )
    ingredient_ids_and_amounts.append((ingredient_id, 1100))

    ingredient_type_id = recipe_book.insert_ingredient_type("Low Sodium Vegetable Broth")
    ingredient_brand_id = recipe_book.insert_ingredient_brand("Campbell's")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id,
        Nutrition_Info(
            1.0,
            80,
            0.0,
            0.0,
            0.0,
            20.0,
            0.0,
            20.0,
            0.4,
            0.0,
            60.0,
            160.0,
            40.0,
            0.4,
            False,
            False,
            False,
            False,
            False,
            False
        )
    )
    ingredient_ids_and_amounts.append((ingredient_id, 1500))

    ingredient_type_id = recipe_book.insert_ingredient_type("Avocado")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id_health_canada,
        Nutrition_Info(
            1/0.972,
            1600,
            146.6,
            21.26,
            0.0,
            85.3,
            67.0,
            6.6,
            20.0,
            0.0,
            70.0,
            4850.0,
            120.0,
            5.5,
            False,
            False,
            False,
            False,
            False,
            False,
            grams_of_monounsaturated_fat_per_kilogram=97.99,
            milligrams_of_vitamin_c_per_kilogram=100.0,
            micrograms_of_vitamin_d_per_kilogram=0.0,
            micrograms_of_vitamin_k_per_kilogram=210.0,
            milligrams_of_thiamine_per_kilogram=0.67,
            milligrams_of_riboflavin_per_kilogram=1.3,
            milligrams_of_niacin_per_kilogram=17.38,
            milligrams_of_vitamin_b6_per_kilogram=2.57,
            micrograms_of_vitamin_b12_per_kilogram=0.0,
            milligrams_of_pantothenate_per_kilogram=13.89,
            milligrams_of_phosphorous_per_kilogram=520.0,
            milligrams_of_magnesium_per_kilogram=290.0,
            milligrams_of_zinc_per_kilogram=6.4,
            micrograms_of_selenium_per_kilogram=4.0,
            milligrams_of_copper_per_kilogram=1.9,
            milligrams_of_manganese_per_kilogram=1.42
        )
    )
    ingredient_ids_and_amounts.append((ingredient_id, 201))

    ingredient_type_id = recipe_book.insert_ingredient_type("Salt")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id_health_canada,
        Nutrition_Info(
            0.25/0.3085,
            0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            387580.0,
            80.0,
            240.0,
            3.3,
            False,
            False,
            False,
            False,
            False,
            False,
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
            10.0,
            1.0,
            1.0,
            0.3,
            1.0,
            0.0,
            0.0,
            0.0
        )
    )
    ingredient_ids_and_amounts.append((ingredient_id, 10))

    ingredient_type_id = recipe_book.insert_ingredient_type("Pepper")
    ingredient_id = recipe_book.create_ingredient(
        ingredient_type_id,
        ingredient_brand_id_health_canada,
        Nutrition_Info(
            15/7,
            2510,
            32.6,
            13.92,
            0.0,
            639.5,
            253.0,
            6.4,
            103.9,
            0.0,
            200.0,
            13290.0,
            4430.0,
            97.1,
            False,
            False,
            False,
            False,
            False,
            False,
            grams_of_monounsaturated_fat_per_kilogram=7.39,
            milligrams_of_vitamin_c_per_kilogram=0.0,
            micrograms_of_vitamin_d_per_kilogram=0.0,
            micrograms_of_vitamin_k_per_kilogram=1637.0,
            milligrams_of_thiamine_per_kilogram=1.08,
            milligrams_of_riboflavin_per_kilogram=1.8,
            milligrams_of_niacin_per_kilogram=11.43,
            milligrams_of_vitamin_b6_per_kilogram=2.91,
            micrograms_of_vitamin_b12_per_kilogram=0.0,
            milligrams_of_pantothenate_per_kilogram=13.99,
            milligrams_of_phosphorous_per_kilogram=1580.0,
            milligrams_of_magnesium_per_kilogram=1710.0,
            milligrams_of_zinc_per_kilogram=11.9,
            micrograms_of_selenium_per_kilogram=49.0,
            milligrams_of_copper_per_kilogram=13.3,
            milligrams_of_manganese_per_kilogram=127.53
        )
    )
    ingredient_ids_and_amounts.append((ingredient_id, 3))

    instructions: list[Instruction] = [
        "In a large pot, melt the butter, then add the onion and garlic. Saute until softened, about 5 minutes",
        "Then add the broccoli and the broth and bring to a boil over high heat. Reduce heat to medium/low and cook with the lid on for about 5-7 minutes until the broccoli is fork tender",
        "Remove from the heat and add the avocado to the pot. Then use a blender to puree the soup until smooth. Taste and add more salt and pepper if needed. Serve"
    ]

    pictures: list[Picture] = []

    recipe_name: str = "Very Easy Vegan Cream of Broccoli Soup"

    required_time_minutes: int = 20

    recipe_id = recipe_book.create_recipe(recipe_group_id, recipe_name, required_time_minutes, pictures, instructions, ingredient_ids_and_amounts, tool_ids)

    everything = recipe_book.get_all_recipe_information(recipe_id)
    print(everything)


if __name__ == "__main__":
    main()
