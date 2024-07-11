import datetime

Query = str

class Queries():
    @staticmethod
    def enable_foreign_keys_query() -> Query:
        query: Query = "PRAGMA foreign_keys = ON;"

        return query

    @staticmethod
    def create_table_recipe_groups_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `recipe_groups` (
                `recipe_group_id` INTEGER NOT NULL PRIMARY KEY,
                `name` TEXT NOT NULL UNIQUE
            );
        """

        return query

    @staticmethod
    def create_table_recipes_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `recipes` (
                `recipe_id` INTEGER NOT NULL PRIMARY KEY,
                `recipe_group_id` INTEGER NOT NULL,
                `name` TEXT NOT NULL UNIQUE,
                `required_time_minutes` INTEGER NULL,
                FOREIGN KEY (`recipe_group_id`)
                REFERENCES `recipe_groups` (`recipe_group_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
        """

        return query

    @staticmethod
    def create_table_tools_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `tools` (
                `tool_id` INTEGER NOT NULL PRIMARY KEY,
                `name` TEXT NOT NULL UNIQUE
            );
        """

        return query

    @staticmethod
    def create_table_ingredient_types_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `ingredient_types` (
                `ingredient_type_id` INTEGER NOT NULL PRIMARY KEY,
                `ingredient_type` TEXT NOT NULL UNIQUE
            );
        """

        return query

    @staticmethod
    def create_table_ingredient_brands_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `ingredient_brands` (
                `ingredient_brand_id` INTEGER NOT NULL PRIMARY KEY,
                `name` TEXT NOT NULL UNIQUE
            );
        """

        return query

    @staticmethod
    def create_table_nutrition_info_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `nutrition_info` (
                `nutrition_info_id` INTEGER NOT NULL PRIMARY KEY,
                `l_per_kg` REAL NOT NULL,
                `kilocalories_per_kg` INTEGER NOT NULL,
                `g_fat_per_kg` REAL NOT NULL,
                `g_saturated_fat_per_kg` REAL NOT NULL,
                `g_trans_fat_per_kg` REAL NOT NULL,
                `g_omega6_polyunsaturated_fat_per_kg` REAL NULL,
                `g_omega3_polyunsaturated_fat_per_kg` REAL NULL,
                `g_monounsaturated_fat_per_kg` REAL NULL,
                `g_carbohydrate_per_kg` REAL NOT NULL,
                `g_dietary_fibre_per_kg` REAL NOT NULL,
                `g_soluble_fibre_per_kg` REAL NULL,
                `g_insoluble_fibre_per_kg` REAL NULL,
                `g_sugars_per_kg` REAL NOT NULL,
                `g_sugar_alcohols_per_kg` REAL NULL,
                `g_starch_per_kg` REAL NULL,
                `g_protein_per_kg` REAL NOT NULL,
                `g_cholesterol_per_kg` REAL NOT NULL,
                `mg_sodium_per_kg` REAL NOT NULL,
                `mg_potassium_per_kg` REAL NOT NULL,
                `mg_calcium_per_kg` REAL NOT NULL,
                `mg_iron_per_kg` REAL NOT NULL,
                `ug_vitamin_a_per_kg` REAL NULL,
                `mg_vitamin_c_per_kg` REAL NULL,
                `ug_vitamin_d_per_kg` REAL NULL,
                `mg_vitamin_e_per_kg` REAL NULL,
                `ug_vitamin_k_per_kg` REAL NULL,
                `mg_thiamine_per_kg` REAL NULL,
                `mg_riboflavin_per_kg` REAL NULL,
                `mg_niacin_per_kg` REAL NULL,
                `mg_vitamin_b6_per_kg` REAL NULL,
                `ug_folate_per_kg` REAL NULL,
                `ug_vitamin_b12_per_kg` REAL NULL,
                `ug_biotin_per_kg` REAL NULL,
                `mg_pantothenate_per_kg` REAL NULL,
                `mg_choline_per_kg` REAL NULL,
                `mg_phosphorous_per_kg` REAL NULL,
                `ug_iodide_per_kg` REAL NULL,
                `mg_magnesium_per_kg` REAL NULL,
                `mg_zinc_per_kg` REAL NULL,
                `ug_selenium_per_kg` REAL NULL,
                `mg_copper_per_kg` REAL NULL,
                `mg_manganese_per_kg` REAL NULL,
                `ug_chromium_per_kg` REAL NULL,
                `ug_molybdenum_per_kg` REAL NULL,
                `mg_chloride_per_kg` REAL NULL,
                `has_gluten` INTEGER NOT NULL CHECK (has_gluten IN (0, 1)),
                `is_meat` INTEGER NOT NULL CHECK (is_meat IN (0, 1)),
                `is_dairy` INTEGER NOT NULL CHECK (is_dairy IN (0, 1)),
                `is_animal_product` INTEGER NOT NULL CHECK (is_animal_product IN (0, 1)),
                `is_nut` INTEGER NOT NULL CHECK (is_nut IN (0, 1)),
                `is_soy` INTEGER NOT NULL CHECK (is_soy IN (0, 1))
            );
        """

        return query

    @staticmethod
    def create_table_pictures_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `pictures` (
                `picture_id` INTEGER NOT NULL PRIMARY KEY,
                `picture` BLOB NOT NULL
            );
        """

        return query

    @staticmethod
    def create_table_instructions_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `instructions` (
                `instruction_id` INTEGER NOT NULL PRIMARY KEY,
                `instruction` TEXT NOT NULL
            );
        """

        return query

    @staticmethod
    def create_table_ingredients_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `ingredients` (
                `ingredient_id` INTEGER NOT NULL PRIMARY KEY,
                `ingredient_type_id` INTEGER NOT NULL,
                `ingredient_brand_id` INTEGER NOT NULL,
                `nutrition_info_id` INTEGER NOT NULL,
                FOREIGN KEY (`nutrition_info_id`)
                REFERENCES `nutrition_info` (`nutrition_info_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (`ingredient_type_id`)
                REFERENCES `ingredient_types` (`ingredient_type_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (`ingredient_brand_id`)
                REFERENCES `ingredient_brands` (`ingredient_brand_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
        """

        return query

    @staticmethod
    def create_table_recipe_usage_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `recipe_usage` (
                `recipe_usage_id` INTEGER NOT NULL PRIMARY KEY,
                `recipe_id` INTEGER NOT NULL,
                `datetime` TEXT NOT NULL,
                FOREIGN KEY (`recipe_id`)
                REFERENCES `recipes` (`recipe_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
        """

        return query

    @staticmethod
    def create_table_recipes_ingredients_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `recipes_ingredients` (
                `recipe_ingredients_id` INTEGER NOT NULL PRIMARY KEY,
                `recipe_id` INTEGER NOT NULL,
                `ingredient_id` INTEGER NOT NULL,
                FOREIGN KEY (`recipe_id`)
                REFERENCES `recipes` (`recipe_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (`ingredient_id`)
                REFERENCES `ingredients` (`ingredient_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
        """

        return query

    @staticmethod
    def create_table_recipes_tools_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `recipes_tools` (
                `recipe_tools_id` INTEGER NOT NULL PRIMARY KEY,
                `recipe_id` INTEGER NOT NULL,
                `tool_id` INTEGER NOT NULL,
                FOREIGN KEY (`recipe_id`)
                REFERENCES `recipes` (`recipe_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (`tool_id`)
                REFERENCES `tools` (`tool_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
        """

        return query

    @staticmethod
    def create_table_recipes_pictures_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `recipes_pictures` (
                `recipe_pictures_id` INTEGER NOT NULL PRIMARY KEY,
                `recipe_id` INTEGER NOT NULL,
                `picture_id` INTEGER NOT NULL,
                FOREIGN KEY (`recipe_id`)
                REFERENCES `recipes` (`recipe_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (`picture_id`)
                REFERENCES `pictures` (`picture_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
        """

        return query

    @staticmethod
    def create_table_recipes_instructions_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `recipes_instructions` (
                `recipe_instructions_id` INTEGER NOT NULL PRIMARY KEY,
                `recipe_id` INTEGER NOT NULL,
                `instruction_id` INTEGER NOT NULL,
                `instruction_number` INTEGER NOT NULL,
                FOREIGN KEY (`recipe_id`)
                REFERENCES `recipes` (`recipe_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (`instruction_id`)
                REFERENCES `instructions` (`instruction_id`)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
        """

        return query

    @staticmethod
    def initial_setup_queries() -> list[Query]:
        queries: list[Query] = [
            Queries.enable_foreign_keys_query(),

            Queries.create_table_recipe_groups_query(),
            Queries.create_table_recipes_query(),
            Queries.create_table_tools_query(),
            Queries.create_table_ingredient_types_query(),
            Queries.create_table_ingredient_brands_query(),
            Queries.create_table_nutrition_info_query(),
            Queries.create_table_pictures_query(),
            Queries.create_table_instructions_query(),

            Queries.create_table_ingredients_query(),
            Queries.create_table_recipe_usage_query(),
            Queries.create_table_recipes_ingredients_query(),
            Queries.create_table_recipes_tools_query(),
            Queries.create_table_recipes_pictures_query(),
            Queries.create_table_recipes_instructions_query()
        ]

        return queries

    @staticmethod
    def insert_recipe_group_query(group_name: str) -> Query:
        assert (isinstance(group_name, str))
        group_name = group_name.replace('"', "")

        query: Query = """
            INSERT INTO `recipe_groups`
            (
                `name`
            )
            VALUES
            (
                "{group_name}"
            );
        """.format(
            group_name = group_name
        )

        return query

    @staticmethod
    def insert_recipe_query(recipe_group_id: int, recipe_name: str) -> Query:
        assert (isinstance(recipe_group_id, int))
        assert (recipe_group_id > 0)
        assert (isinstance(recipe_name, str))
        recipe_name = recipe_name.replace('"', "")

        query: Query = """
            INSERT INTO `recipes`
            (
                `recipe_group_id`,
                `name`
            )
            VALUES
            (
                {recipe_group_id},
                "{recipe_name}"
            );
        """.format(
            recipe_group_id = recipe_group_id,
            recipe_name = recipe_name
        )

        return query

    @staticmethod
    def insert_tool_query(tool_name: str) -> Query:
        assert (isinstance(tool_name, str))
        tool_name = tool_name.replace('"', "")

        query: Query = """
            INSERT INTO `tools`
            (
                `name`
            )
            VALUES
            (
                "{tool_name}"
            );
        """.format(
            tool_name = tool_name
        )

        return query

    @staticmethod
    def insert_ingredient_type_query(ingredient_type: str) -> Query:
        assert (isinstance(ingredient_type, str))
        ingredient_type = ingredient_type.replace('"', "")

        query: Query = """
            INSERT INTO `ingredient_types`
            (
                `ingredient_type`
            )
            VALUES
            (
                "{ingredient_type}"
            );
        """.format(
            ingredient_type = ingredient_type
        )

        return query

    @staticmethod
    def insert_ingredient_brand_query(ingredient_brand: str) -> Query:
        assert (isinstance(ingredient_brand, str))
        ingredient_brand = ingredient_brand.replace('"', "")

        query: Query = """
            INSERT INTO `ingredient_brands`
            (
                `name`
            )
            VALUES
            (
                "{ingredient_brand}"
            );
        """.format(
            ingredient_brand = ingredient_brand
        )

        return query

    @staticmethod
    def insert_nutrition_info_query(
        litres_per_kilogram: float,
        kilocalories_per_kilogram: int,
        grams_of_fat_per_kilogram: float,
        grams_of_saturated_fat_per_kilogram: float,
        grams_of_trans_fat_per_kilogram: float,
        grams_of_carbohydrate_per_kilogram: float,
        grams_of_dietary_fibre_per_kilogram: float,
        grams_of_sugars_per_kilogram: float,
        grams_of_protein_per_kilogram: float,
        grams_of_cholesterol_per_kilogram: float,
        milligrams_of_sodium_per_kilogram: float,
        milligrams_of_potassium_per_kilogram: float,
        milligrams_of_calcium_per_kilogram: float,
        milligrams_of_iron_per_kilogram: float,
        has_gluten: bool,
        is_meat: bool,
        is_dairy: bool,
        is_animal_product: bool,
        is_nut: bool,
        is_soy: bool,
        grams_of_omega6_polyunsaturated_fat_per_kilogram: float | None = None,
        grams_of_omega3_polyunsaturated_fat_per_kilogram: float | None = None,
        grams_of_monounsaturated_fat_per_kilogram: float | None = None,
        grams_of_soluble_fibre_per_kilogram: float | None = None,
        grams_of_insoluble_fibre_per_kilogram: float | None = None,
        grams_of_sugar_alcohols_per_kilogram: float | None = None,
        grams_of_starch_per_kilogram: float | None = None,
        micrograms_of_vitamin_a_per_kilogram: float | None = None,
        milligrams_of_vitamin_c_per_kilogram: float | None = None,
        micrograms_of_vitamin_d_per_kilogram: float | None = None,
        milligrams_of_vitamin_e_per_kilogram: float | None = None,
        micrograms_of_vitamin_k_per_kilogram: float | None = None,
        milligrams_of_thiamine_per_kilogram: float | None = None,
        milligrams_of_riboflavin_per_kilogram: float | None = None,
        milligrams_of_niacin_per_kilogram: float | None = None,
        milligrams_of_vitamin_b6_per_kilogram: float | None = None,
        micrograms_of_folate_per_kilogram: float | None = None,
        micrograms_of_vitamin_b12_per_kilogram: float | None = None,
        micrograms_of_biotin_per_kilogram: float | None = None,
        milligrams_of_pantothenate_per_kilogram: float | None = None,
        milligrams_of_choline_per_kilogram: float | None = None,
        milligrams_of_phosphorous_per_kilogram: float | None = None,
        micrograms_of_iodide_per_kilograms: float | None = None,
        milligrams_of_magnesium_per_kilogram: float | None = None,
        milligrams_of_zinc_per_kilogram: float | None = None,
        micrograms_of_selenium_per_kilogram: float | None = None,
        milligrams_of_copper_per_kilogram: float | None = None,
        milligrams_of_manganese_per_kilogram: float | None = None,
        micrograms_of_chromium_per_kilogram: float | None = None,
        micrograms_of_molybdenum_per_kilogram: float | None = None,
        milligrams_of_chloride_per_kilogram: float | None = None
    ) -> Query:
        assert (isinstance(litres_per_kilogram, float))
        assert (isinstance(kilocalories_per_kilogram, int))
        assert (isinstance(grams_of_fat_per_kilogram, float))
        assert (isinstance(grams_of_saturated_fat_per_kilogram, float))
        assert (isinstance(grams_of_trans_fat_per_kilogram, float))
        assert (isinstance(grams_of_omega6_polyunsaturated_fat_per_kilogram, float) or grams_of_omega6_polyunsaturated_fat_per_kilogram is None)
        assert (isinstance(grams_of_omega3_polyunsaturated_fat_per_kilogram, float) or grams_of_omega3_polyunsaturated_fat_per_kilogram is None)
        assert (isinstance(grams_of_monounsaturated_fat_per_kilogram, float) or grams_of_monounsaturated_fat_per_kilogram is None)
        assert (isinstance(grams_of_carbohydrate_per_kilogram, float))
        assert (isinstance(grams_of_dietary_fibre_per_kilogram, float))
        assert (isinstance(grams_of_soluble_fibre_per_kilogram, float) or grams_of_soluble_fibre_per_kilogram is None)
        assert (isinstance(grams_of_insoluble_fibre_per_kilogram, float) or grams_of_insoluble_fibre_per_kilogram is None)
        assert (isinstance(grams_of_sugars_per_kilogram, float))
        assert (isinstance(grams_of_sugar_alcohols_per_kilogram, float) or grams_of_sugar_alcohols_per_kilogram is None)
        assert (isinstance(grams_of_starch_per_kilogram, float) or grams_of_starch_per_kilogram is None)
        assert (isinstance(grams_of_protein_per_kilogram, float))
        assert (isinstance(grams_of_cholesterol_per_kilogram, float))
        assert (isinstance(milligrams_of_sodium_per_kilogram, float))
        assert (isinstance(milligrams_of_potassium_per_kilogram, float))
        assert (isinstance(milligrams_of_calcium_per_kilogram, float))
        assert (isinstance(milligrams_of_iron_per_kilogram, float))
        assert (isinstance(micrograms_of_vitamin_a_per_kilogram, float) or micrograms_of_vitamin_a_per_kilogram is None)
        assert (isinstance(milligrams_of_vitamin_c_per_kilogram, float) or milligrams_of_vitamin_c_per_kilogram is None)
        assert (isinstance(micrograms_of_vitamin_d_per_kilogram, float) or micrograms_of_vitamin_d_per_kilogram is None)
        assert (isinstance(milligrams_of_vitamin_e_per_kilogram, float) or milligrams_of_vitamin_e_per_kilogram is None)
        assert (isinstance(micrograms_of_vitamin_k_per_kilogram, float) or micrograms_of_vitamin_k_per_kilogram is None)
        assert (isinstance(milligrams_of_thiamine_per_kilogram, float) or milligrams_of_thiamine_per_kilogram is None)
        assert (isinstance(milligrams_of_riboflavin_per_kilogram, float) or milligrams_of_riboflavin_per_kilogram is None)
        assert (isinstance(milligrams_of_niacin_per_kilogram, float) or milligrams_of_niacin_per_kilogram is None)
        assert (isinstance(milligrams_of_vitamin_b6_per_kilogram, float) or milligrams_of_vitamin_b6_per_kilogram is None)
        assert (isinstance(micrograms_of_folate_per_kilogram, float) or micrograms_of_folate_per_kilogram is None)
        assert (isinstance(micrograms_of_vitamin_b12_per_kilogram, float) or micrograms_of_vitamin_b12_per_kilogram is None)
        assert (isinstance(micrograms_of_biotin_per_kilogram, float) or micrograms_of_biotin_per_kilogram is None)
        assert (isinstance(milligrams_of_pantothenate_per_kilogram, float) or milligrams_of_pantothenate_per_kilogram is None)
        assert (isinstance(milligrams_of_choline_per_kilogram, float) or milligrams_of_choline_per_kilogram is None)
        assert (isinstance(milligrams_of_phosphorous_per_kilogram, float) or milligrams_of_phosphorous_per_kilogram is None)
        assert (isinstance(micrograms_of_iodide_per_kilograms, float) or micrograms_of_iodide_per_kilograms is None)
        assert (isinstance(milligrams_of_magnesium_per_kilogram, float) or milligrams_of_magnesium_per_kilogram is None)
        assert (isinstance(milligrams_of_zinc_per_kilogram, float) or milligrams_of_zinc_per_kilogram is None)
        assert (isinstance(micrograms_of_selenium_per_kilogram, float) or micrograms_of_selenium_per_kilogram is None)
        assert (isinstance(milligrams_of_copper_per_kilogram, float) or milligrams_of_copper_per_kilogram is None)
        assert (isinstance(milligrams_of_manganese_per_kilogram, float) or milligrams_of_manganese_per_kilogram is None)
        assert (isinstance(micrograms_of_chromium_per_kilogram, float) or micrograms_of_chromium_per_kilogram is None)
        assert (isinstance(micrograms_of_molybdenum_per_kilogram, float) or micrograms_of_molybdenum_per_kilogram is None)
        assert (isinstance(milligrams_of_chloride_per_kilogram, float) or milligrams_of_chloride_per_kilogram is None)
        assert (isinstance(has_gluten, bool))
        assert (isinstance(is_meat, bool))
        assert (isinstance(is_dairy, bool))
        assert (isinstance(is_animal_product, bool))
        assert (isinstance(is_nut, bool))
        assert (isinstance(is_soy, bool))
        # TODO could also assert that these are all positive numbers

        query: Query = """
            INSERT INTO `nutrition_info`
            (
                `l_per_kg`,
                `kilocalories_per_kg`,
                `g_fat_per_kg`,
                `g_saturated_fat_per_kg`,
                `g_trans_fat_per_kg`,
                `g_omega6_polyunsaturated_fat_per_kg`,
                `g_omega3_polyunsaturated_fat_per_kg`,
                `g_monounsaturated_fat_per_kg`,
                `g_carbohydrate_per_kg`,
                `g_dietary_fibre_per_kg`,
                `g_soluble_fibre_per_kg`,
                `g_insoluble_fibre_per_kg`,
                `g_sugars_per_kg`,
                `g_sugar_alcohols_per_kg`,
                `g_starch_per_kg`,
                `g_protein_per_kg`,
                `g_cholesterol_per_kg`,
                `mg_sodium_per_kg`,
                `mg_potassium_per_kg`,
                `mg_calcium_per_kg`,
                `mg_iron_per_kg`,
                `ug_vitamin_a_per_kg`,
                `mg_vitamin_c_per_kg`,
                `ug_vitamin_d_per_kg`,
                `mg_vitamin_e_per_kg`,
                `ug_vitamin_k_per_kg`,
                `mg_thiamine_per_kg`,
                `mg_riboflavin_per_kg`,
                `mg_niacin_per_kg`,
                `mg_vitamin_b6_per_kg`,
                `ug_folate_per_kg`,
                `ug_vitamin_b12_per_kg`,
                `ug_biotin_per_kg`,
                `mg_pantothenate_per_kg`,
                `mg_choline_per_kg`,
                `mg_phosphorous_per_kg`,
                `ug_iodide_per_kg`,
                `mg_magnesium_per_kg`,
                `mg_zinc_per_kg`,
                `ug_selenium_per_kg`,
                `mg_copper_per_kg`,
                `mg_manganese_per_kg`,
                `ug_chromium_per_kg`,
                `ug_molybdenum_per_kg`,
                `mg_chloride_per_kg`,
                `has_gluten`,
                `is_meat`,
                `is_dairy`,
                `is_animal_product`,
                `is_nut`,
                `is_soy`
            )
            VALUES
            (
                {litres_per_kilogram},
                {kilocalories_per_kilogram},
                {grams_of_fat_per_kilogram},
                {grams_of_saturated_fat_per_kilogram},
                {grams_of_trans_fat_per_kilogram},
                {grams_of_omega6_polyunsaturated_fat_per_kilogram},
                {grams_of_omega3_polyunsaturated_fat_per_kilogram},
                {grams_of_monounsaturated_fat_per_kilogram},
                {grams_of_carbohydrate_per_kilogram},
                {grams_of_dietary_fibre_per_kilogram},
                {grams_of_soluble_fibre_per_kilogram},
                {grams_of_insoluble_fibre_per_kilogram},
                {grams_of_sugars_per_kilogram},
                {grams_of_sugar_alcohols_per_kilogram},
                {grams_of_starch_per_kilogram},
                {grams_of_protein_per_kilogram},
                {grams_of_cholesterol_per_kilogram},
                {milligrams_of_sodium_per_kilogram},
                {milligrams_of_potassium_per_kilogram},
                {milligrams_of_calcium_per_kilogram},
                {milligrams_of_iron_per_kilogram},
                {micrograms_of_vitamin_a_per_kilogram},
                {milligrams_of_vitamin_c_per_kilogram},
                {micrograms_of_vitamin_d_per_kilogram},
                {milligrams_of_vitamin_e_per_kilogram},
                {micrograms_of_vitamin_k_per_kilogram},
                {milligrams_of_thiamine_per_kilogram},
                {milligrams_of_riboflavin_per_kilogram},
                {milligrams_of_niacin_per_kilogram},
                {milligrams_of_vitamin_b6_per_kilogram},
                {micrograms_of_folate_per_kilogram},
                {micrograms_of_vitamin_b12_per_kilogram},
                {micrograms_of_biotin_per_kilogram},
                {milligrams_of_pantothenate_per_kilogram},
                {milligrams_of_choline_per_kilogram},
                {milligrams_of_phosphorous_per_kilogram},
                {micrograms_of_iodide_per_kilograms},
                {milligrams_of_magnesium_per_kilogram},
                {milligrams_of_zinc_per_kilogram},
                {micrograms_of_selenium_per_kilogram},
                {milligrams_of_copper_per_kilogram},
                {milligrams_of_manganese_per_kilogram},
                {micrograms_of_chromium_per_kilogram},
                {micrograms_of_molybdenum_per_kilogram},
                {milligrams_of_chloride_per_kilogram},
                {has_gluten},
                {is_meat},
                {is_dairy},
                {is_animal_product},
                {is_nut},
                {is_soy}
            );
        """.format(
            litres_per_kilogram = litres_per_kilogram,
            kilocalories_per_kilogram = kilocalories_per_kilogram,
            grams_of_fat_per_kilogram = grams_of_fat_per_kilogram,
            grams_of_saturated_fat_per_kilogram = grams_of_saturated_fat_per_kilogram,
            grams_of_trans_fat_per_kilogram = grams_of_trans_fat_per_kilogram,
            grams_of_omega6_polyunsaturated_fat_per_kilogram = grams_of_omega6_polyunsaturated_fat_per_kilogram,
            grams_of_omega3_polyunsaturated_fat_per_kilogram = grams_of_omega3_polyunsaturated_fat_per_kilogram,
            grams_of_monounsaturated_fat_per_kilogram = grams_of_monounsaturated_fat_per_kilogram,
            grams_of_carbohydrate_per_kilogram = grams_of_carbohydrate_per_kilogram,
            grams_of_dietary_fibre_per_kilogram = grams_of_dietary_fibre_per_kilogram,
            grams_of_soluble_fibre_per_kilogram = grams_of_soluble_fibre_per_kilogram,
            grams_of_insoluble_fibre_per_kilogram = grams_of_insoluble_fibre_per_kilogram,
            grams_of_sugars_per_kilogram = grams_of_sugars_per_kilogram,
            grams_of_sugar_alcohols_per_kilogram = grams_of_sugar_alcohols_per_kilogram,
            grams_of_starch_per_kilogram = grams_of_starch_per_kilogram,
            grams_of_protein_per_kilogram = grams_of_protein_per_kilogram,
            grams_of_cholesterol_per_kilogram = grams_of_cholesterol_per_kilogram,
            milligrams_of_sodium_per_kilogram = milligrams_of_sodium_per_kilogram,
            milligrams_of_potassium_per_kilogram = milligrams_of_potassium_per_kilogram,
            milligrams_of_calcium_per_kilogram = milligrams_of_calcium_per_kilogram,
            milligrams_of_iron_per_kilogram = milligrams_of_iron_per_kilogram,
            micrograms_of_vitamin_a_per_kilogram = micrograms_of_vitamin_a_per_kilogram,
            milligrams_of_vitamin_c_per_kilogram = milligrams_of_vitamin_c_per_kilogram,
            micrograms_of_vitamin_d_per_kilogram = micrograms_of_vitamin_d_per_kilogram,
            milligrams_of_vitamin_e_per_kilogram = milligrams_of_vitamin_e_per_kilogram,
            micrograms_of_vitamin_k_per_kilogram = micrograms_of_vitamin_k_per_kilogram,
            milligrams_of_thiamine_per_kilogram = milligrams_of_thiamine_per_kilogram,
            milligrams_of_riboflavin_per_kilogram = milligrams_of_riboflavin_per_kilogram,
            milligrams_of_niacin_per_kilogram = milligrams_of_niacin_per_kilogram,
            milligrams_of_vitamin_b6_per_kilogram = milligrams_of_vitamin_b6_per_kilogram,
            micrograms_of_folate_per_kilogram = micrograms_of_folate_per_kilogram,
            micrograms_of_vitamin_b12_per_kilogram = micrograms_of_vitamin_b12_per_kilogram,
            micrograms_of_biotin_per_kilogram = micrograms_of_biotin_per_kilogram,
            milligrams_of_pantothenate_per_kilogram = milligrams_of_pantothenate_per_kilogram,
            milligrams_of_choline_per_kilogram = milligrams_of_choline_per_kilogram,
            milligrams_of_phosphorous_per_kilogram = milligrams_of_phosphorous_per_kilogram,
            micrograms_of_iodide_per_kilograms = micrograms_of_iodide_per_kilograms,
            milligrams_of_magnesium_per_kilogram = milligrams_of_magnesium_per_kilogram,
            milligrams_of_zinc_per_kilogram = milligrams_of_zinc_per_kilogram,
            micrograms_of_selenium_per_kilogram = micrograms_of_selenium_per_kilogram,
            milligrams_of_copper_per_kilogram = milligrams_of_copper_per_kilogram,
            milligrams_of_manganese_per_kilogram = milligrams_of_manganese_per_kilogram,
            micrograms_of_chromium_per_kilogram = micrograms_of_chromium_per_kilogram,
            micrograms_of_molybdenum_per_kilogram = micrograms_of_molybdenum_per_kilogram,
            milligrams_of_chloride_per_kilogram = milligrams_of_chloride_per_kilogram,
            has_gluten = 1 if has_gluten else 0,
            is_meat = 1 if is_meat else 0,
            is_dairy = 1 if is_dairy else 0,
            is_animal_product = 1 if is_animal_product else 0,
            is_nut = 1 if is_nut else 0,
            is_soy = 1 if is_soy else 0
        )

        return query

    @staticmethod
    def insert_picture_query() -> Query:

        query: Query = """
            INSERT INTO `pictures`
            (
                `picture`
            )
            VALUES
            (
                (?)
            );
        """

        return query

    @staticmethod
    def insert_instruction_query(instruction: str) -> Query:
        assert (isinstance(instruction, str))

        query: Query = """
            INSERT INTO `instructions`
            (
                `instruction`
            )
            VALUES
            (
                "{instruction}"
            );
        """.format(instruction = instruction)

        return query

    @staticmethod
    def insert_ingredient_query(ingredient_type_id: int, ingredient_brand_id: int, nutrition_info_id: int) -> Query:
        assert (isinstance(ingredient_type_id, int))
        assert (ingredient_type_id > 0)
        assert (isinstance(ingredient_brand_id, int))
        assert (ingredient_brand_id > 0)
        assert (isinstance(nutrition_info_id, int))
        assert (nutrition_info_id > 0)

        query: Query = """
            INSERT INTO `ingredients`
            (
                `ingredient_type_id`,
                `ingredient_brand_id`,
                `nutrition_info_id`
            )
            VALUES
            (
                {ingredient_type_id},
                {ingredient_brand_id},
                {nutrition_info_id}
            );
        """.format(
            ingredient_type_id = ingredient_type_id,
            ingredient_brand_id = ingredient_brand_id,
            nutrition_info_id = nutrition_info_id
        )

        return query

    @staticmethod
    def insert_recipe_usage_query(recipe_id: int, datetime_used: datetime.datetime) -> Query:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(datetime_used, datetime.datetime))

        query: Query = """
            INSERT INTO `recipe_usage`
            (
                `recipe_id`,
                `datetime`
            )
            VALUES
            (
                {recipe_id},
                "{datetime_used}"
            );
        """.format(
            recipe_id = recipe_id,
            datetime_used = datetime_used.strftime("%Y-%m-%d %H:%M:%S")
        )

        return query

    @staticmethod
    def insert_recipe_ingredient_query(recipe_id: int, ingredient_id: int) -> Query:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(ingredient_id, int))
        assert (ingredient_id > 0)

        query: Query = """
            INSERT INTO `recipes_ingredients`
            (
                `recipe_id`,
                `ingredient_id`
            )
            VALUES
            (
                {recipe_id},
                {ingredient_id}
            );
        """.format(
            recipe_id = recipe_id,
            ingredient_id = ingredient_id
        )

        return query

    @staticmethod
    def insert_recipe_tool_query(recipe_id: int, tool_id: int) -> Query:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(tool_id, int))
        assert (tool_id > 0)

        query: Query = """
            INSERT INTO `recipes_tools`
            (
                `recipe_id`,
                `tool_id`
            )
            VALUES
            (
                {recipe_id},
                {tool_id}
            );
        """.format(
            recipe_id = recipe_id,
            tool_id = tool_id
        )

        return query

    @staticmethod
    def insert_recipe_picture_query(recipe_id: int, picture_id: int) -> Query:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(picture_id, int))
        assert (picture_id > 0)

        query: Query = """
            INSERT INTO `recipes_pictures`
            (
                `recipe_id`,
                `picture_id`
            )
            VALUES
            (
                {recipe_id},
                {picture_id}
            );
        """.format(
            recipe_id = recipe_id,
            picture_id = picture_id
        )

        return query

    @staticmethod
    def insert_recipe_instruction(recipe_id: int, instruction_id: int, instruction_number: int) -> Query:
        assert (isinstance(recipe_id, int))
        assert (recipe_id > 0)
        assert (isinstance(instruction_id, int))
        assert (instruction_id > 0)
        assert (isinstance(instruction_number, int))
        assert (instruction_number > 0)

        query: Query = """
            INSERT INTO `recipes_instructions`
            (
                `recipe_id`,
                `instruction_id`,
                `instruction_number`
            )
            VALUES
            (
                {recipe_id},
                {instruction_id},
                {instruction_number}
            );
        """.format(
            recipe_id = recipe_id,
            instruction_id = instruction_id,
            instruction_number = instruction_number
        )

        return query

    @staticmethod
    def get_recipe_groups_query() -> Query:
        query: Query =  """
            SELECT
                `recipe_group_id`,
                `name`
            FROM
                `recipe_groups`;
        """

        return query

    @staticmethod
    def get_recipes_query(recipe_group_id: int | None = None) -> Query:
        assert (isinstance(recipe_group_id, int) or recipe_group_id is None)
        if (isinstance(recipe_group_id, int)):
            assert (recipe_group_id > 0)
        query: Query = """
            SELECT
                `recipe_id`,
                `recipe_group_id`,
                `name`,
                `required_time_minutes`
            FROM
                `recipes`
            {where_recipe_group_id};
        """
        where_recipe_group_id: Query = ""
        if (recipe_group_id is not None):
            where_recipe_group_id = """
                WHERE
                    `recipe_group_id` = {recipe_group_id}
            """.format(recipe_group_id = recipe_group_id)
        query = query.format(where_recipe_group_id = where_recipe_group_id)

        return query

    @staticmethod
    def get_tools_query(recipe_id: int | None = None) -> Query:
        assert (isinstance(recipe_id, int) or recipe_id is None)
        if (isinstance(recipe_id, int)):
            assert (recipe_id > 0)
        query: Query = """
            SELECT
                `tool_id`,
                `name`
            FROM
                `tools`
            {where_recipe_id};
        """
        where_recipe_id: Query = ""
        if (recipe_id is not None):
            where_recipe_id = """
                JOIN
                    `recipes_tools`
                ON
                    `recipes_tools`.`tool_id` = `tools`.`tool_id`
                WHERE
                    `recipe_id` = {recipe_id}
            """.format(
                recipe_id = recipe_id
            )
        query = query.format(
            where_recipe_id = where_recipe_id
        )

        return query

    @staticmethod
    def get_pictures_query(recipe_id: int | None = None) -> Query:
        assert (isinstance(recipe_id, int) or recipe_id is None)
        if (isinstance(recipe_id, int)):
            assert (recipe_id > 0)
        query: Query = """
            SELECT
                `picture_id`,
                `picture`
            FROM
                `pictures`
            {where_recipe_id};
        """
        where_recipe_id: Query = ""
        if (recipe_id is not None):
            where_recipe_id = """
                JOIN
                    `recipes_pictures`
                ON
                    `recipes_pictures`.`picture_id` = `pictures`.`picture_id`
                WHERE
                    `recipe_id` = {recipe_id}
            """.format(
                recipe_id = recipe_id
            )
        query = query.format(
            where_recipe_id = where_recipe_id
        )

        return query

    @staticmethod
    def get_instructions_query(recipe_id: int | None = None) -> Query:
        assert (isinstance(recipe_id, int) or recipe_id is None)
        if (isinstance(recipe_id, int)):
            assert (recipe_id > 0)
        query: Query = """
            SELECT
                `instructions`.`instruction_id`,
                `instruction`,
                `instruction_number`
            FROM
                `instructions`
            JOIN
                `recipes_instructions`
            ON
                `recipe_instructions`.`instruction_id` = `instructions`.`instruction_id`
            {where_recipe_id};
        """
        where_recipe_id: Query = ""
        if (recipe_id is not None):
            where_recipe_id = """
                WHERE
                    `recipe_id` = {recipe_id}
            """.format(
                recipe_id = recipe_id
            )
        query = query.format(
            where_recipe_id = where_recipe_id
        )

        return query

    @staticmethod
    def get_ingredients_query(recipe_id: int | None = None) -> Query:
        assert (isinstance(recipe_id, int) or recipe_id is None)
        if (isinstance(recipe_id, int)):
            assert (recipe_id > 0)
        query: Query = """
            SELECT
                `ingredient_id`,
                `ingredient_type_id`,
                `ingredient_type`,
                `ingredient_brand_id`,
                `ingredient_brand`,
                `nutrition_info_id`,
                `nutrition_info`.*
            FROM
                `ingredients`
            JOIN
                `ingredient_types`
            ON
                `ingredient_types`.`ingredient_type_id` = `ingredients`.`ingredient_type_id`
            JOIN
                `ingredient_brands`
            ON
                `ingredient_brands`.`ingredient_brand_id` = `ingredients`.`ingredient_brand_id`
            JOIN
                `nutrition_info`
            ON
                `nutrition_info`.`nutrition_info_id` = `ingredients`.`nutrition_info_id`
            {where_recipe_id};
        """
        where_recipe_id: Query = ""
        if (recipe_id is not None):
            where_recipe_id = """
                JOIN
                    `recipes_ingredients`
                ON
                    `recipes_ingredients`.`ingredient_id` = `ingredients`.`ingredient_id`
                WHERE
                    `recipe_id` = {recipe_id}
            """.format(
                recipe_id = recipe_id
            )
        query = query.format(
            where_recipe_id = where_recipe_id
        )

        return query

    @staticmethod
    def get_recipe_usage_query(recipe_id: int | None = None) -> Query:
        assert (isinstance(recipe_id, int) or recipe_id is None)
        if (isinstance(recipe_id, int)):
            assert (recipe_id > 0)
        query: Query = """
            SELECT
                `recipe_usage_id`,
                `recipe_id`,
                `datetime`
            FROM
                `recipe_usage`
            {where_recipe_id};
        """
        where_recipe_id: Query = ""
        if (recipe_id is not None):
            where_recipe_id = """
                WHERE
                    `recipe_id` = {recipe_id}
            """.format(
                recipe_id = recipe_id
            )
        query = query.format(
            where_recipe_id = where_recipe_id
        )
        return query
