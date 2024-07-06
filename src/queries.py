
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
                `recipe_group_id` INT NOT NULL PRIMARY KEY,
                `group_name` TEXT NOT NULL UNIQUE
            );
        """

        return query

    @staticmethod
    def create_table_recipes_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `recipes` (
                `recipe_id` INT NOT NULL PRIMARY KEY,
                `recipe_group_id` INT NOT NULL,
                `name` TEXT NOT NULL UNIQUE,
                `required_time_minutes` INT NULL,
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
                `tool_id` INT NOT NULL PRIMARY KEY,
                `name` TEXT NOT NULL UNIQUE
            );
        """

        return query

    @staticmethod
    def create_table_ingredient_types_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `ingredient_types` (
                `ingredient_type_id` INT NOT NULL PRIMARY KEY,
                `ingredient_type` TEXT NOT NULL UNIQUE
            );
        """

        return query

    @staticmethod
    def create_table_ingredient_brands_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `ingredient_brands` (
                `ingredient_brand_id` INT NOT NULL PRIMARY KEY,
                `brand_name` TEXT NOT NULL UNIQUE
            );
        """

        return query

    @staticmethod
    def create_table_nutrition_info_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `nutrition_info` (
                `nutrition_info_id` INT NOT NULL PRIMARY KEY,
                `l_per_kg` REAL NOT NULL,
                `kilocalories_per_kg` INT NOT NULL,
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
                `has_gluten` INT NOT NULL CHECK (has_gluten IN (0, 1)),
                `is_meat` INT NOT NULL CHECK (is_meat IN (0, 1)),
                `is_dairy` INT NOT NULL CHECK (is_dairy IN (0, 1)),
                `is_animal_product` INT NOT NULL CHECK (is_animal_product IN (0, 1)),
                `is_nut` INT NOT NULL CHECK (is_nut IN (0, 1)),
                `is_soy` INT NOT NULL CHECK (is_soy IN (0, 1))
            );
        """

        return query

    @staticmethod
    def create_table_pictures_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `pictures` (
                `picture_id` INT NOT NULL PRIMARY KEY,
                `picture` BLOB NOT NULL
            );
        """

        return query

    @staticmethod
    def create_table_instructions_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `instructions` (
                `instruction_id` INT NOT NULL PRIMARY KEY,
                `instruction` TEXT NOT NULL
            );
        """

        return query

    @staticmethod
    def create_table_ingredients_query() -> Query:
        query: Query = """
            CREATE TABLE IF NOT EXISTS `ingredients` (
                `ingredient_id` INT NOT NULL PRIMARY KEY,
                `ingredient_type_id` INT NOT NULL,
                `ingredient_brand_id` INT NOT NULL,
                `nutrition_info_id` INT NOT NULL,
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
                `recipe_usage_id` INT NOT NULL PRIMARY KEY,
                `recipe_id` INT NOT NULL,
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
                `recipe_ingredients_id` INT NOT NULL PRIMARY KEY,
                `recipe_id` INT NOT NULL,
                `ingredient_id` INT NOT NULL,
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
                `recipe_tools_id` INT NOT NULL PRIMARY KEY,
                `recipe_id` INT NOT NULL,
                `tool_id` INT NOT NULL,
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
                `recipe_pictures_id` INT NOT NULL PRIMARY KEY,
                `recipe_id` INT NOT NULL,
                `picture_id` INT NOT NULL,
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
                `recipe_instructions_id` INT NOT NULL PRIMARY KEY,
                `recipe_id` INT NOT NULL,
                `instruction_id` INT NOT NULL,
                `instruction_number` INT NOT NULL,
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
