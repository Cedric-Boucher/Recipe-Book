# should validate all recipe json files to ensure:
# 1. structure is valid and contains all required fields
# 2. structure does not contain unrecognized fields
# 3. all field values are valid (of the correct type, make sense, etc)
# 4. all units are valid and recognized
# 5. picture file names are valid and point to existing pictures in Pictures folder

# create enums for Python for things that should be enums

# it's not well defined when ingredient names shouldbe singular or plural, ingredients should be enums too (names that only exist in one place)

import sqlite3
from typing import Any

class Database:
    def __init__(self, filename: str):
        self.__filename: str = filename
        self.__connection: None | sqlite3.Connection = None
        self.__cursor: None | sqlite3.Cursor = None

    def connect(self) -> None:
        try:
            self.__connection = sqlite3.connect(self.__filename)
            print("sqlite3 version: {}".format(sqlite3.sqlite_version))
        except sqlite3.Error as e:
            print(e)

        if self.__connection is not None:
            try:
                self.__cursor = self.__connection.cursor()
            except sqlite3.Error as e:
                print(e)

    def run_query(self, query: str) -> list[Any]:
        assert (self.__cursor is not None)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def disconnect(self) -> None:
        if self.__cursor is not None:
            self.__cursor.close()
        if self.__connection is not None:
            self.__connection.close()

if __name__ == "__main__":
    initial_setup_queries: list[str] = [
        """
        PRAGMA foreign_keys = ON;
        """,
        """
        CREATE TABLE IF NOT EXISTS `recipes` (
            `recipe_id` INT NOT NULL PRIMARY KEY,
            `name` TEXT NOT NULL UNIQUE
        );
        """,
        """
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
        """,
        """
        CREATE TABLE IF NOT EXISTS `ingredients` (
            `ingredient_id` INT NOT NULL PRIMARY KEY,
            `name` TEXT NOT NULL UNIQUE,
            `nutrition_info_id` INT NOT NULL,
            FOREIGN KEY (`nutrition_info_id`)
            REFERENCES `nutrition_info` (`nutrition_info_id`)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
        """,
        """
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
        """,
        """
        CREATE TABLE IF NOT EXISTS `tools` (
            `tool_id` INT NOT NULL PRIMARY KEY,
            `name` TEXT NOT NULL UNIQUE
        );
        """,
        """
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
        """,
        """
        CREATE TABLE IF NOT EXISTS `pictures` (
            `picture_id` INT NOT NULL PRIMARY KEY,
            `picture` BLOB NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS `nutrition_info` (
            `nutrition_info_id` INT NOT NULL PRIMARY KEY,
            `amount_grams` INT NOT NULL,
            `calories` INT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS `recipes_instructions` (
            `recipe_instructions_id` INT NOT NULL PRIMARY KEY,
            `recipe_id` INT NOT NULL,
            `instruction_id` INT NOT NULL,
            FOREIGN KEY (`recipe_id`)
            REFERENCES `recipes` (`recipe_id`)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            FOREIGN KEY (`instruction_id`)
            REFERENCES `instructions` (`instruction_id`)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS `instructions` (
            `instruction_id` INT NOT NULL PRIMARY KEY,
            `instruction` TEXT NOT NULL
        );
        """
    ]

    STORE_IN_MEMORY: bool = False

    if STORE_IN_MEMORY:
        database: Database = Database(":memory:")
    else:
        database: Database = Database("recipe_book.sqlite3")
    database.connect()
    for initial_setup_query in initial_setup_queries:
        print(initial_setup_query)
        print(database.run_query(initial_setup_query))
    database.disconnect()
