from recipe_book import Recipe_Book
from data_types.nutrition_info import Nutrition_Info
from data_types.instruction import Instruction
from data_types.picture import Picture

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
