from data_types.ingredient import Ingredient
from data_types.instruction import Instruction
from data_types.tool import Tool
from data_types.picture import Picture
import datetime

class Recipe():
    def __init__(
        self,
        recipe_name: str,
        recipe_group_name: str,
        ingredients: list[Ingredient],
        instructions: list[Instruction],
        tools: list[Tool],
        pictures: list[Picture],
        required_time_minutes: int | None,
        recipe_usage_datetimes: list[datetime.datetime]
    ) -> None:
        assert (isinstance(recipe_name, str))
        assert (isinstance(recipe_group_name, str))
        assert (isinstance(ingredients, list))
        for ingredient in ingredients:
            assert (isinstance(ingredient, Ingredient))
        assert (isinstance(instructions, list))
        for instruction in instructions:
            assert (isinstance(instruction, Instruction))
        assert (isinstance(tools, list))
        for tool in tools:
            assert (isinstance(tool, Tool))
        assert (isinstance(pictures, list))
        for picture in pictures:
            assert (isinstance(picture, Picture))
        assert (isinstance(required_time_minutes, int) or required_time_minutes is None)
        assert (isinstance(recipe_usage_datetimes, list))
        for recipe_usage_datetime in recipe_usage_datetimes:
            assert (isinstance(recipe_usage_datetime, datetime.datetime))

        self.__recipe_name: str = recipe_name
        self.__recipe_group_name: str = recipe_group_name
        self.__ingredients: list[Ingredient] = ingredients
        self.__instructions: list[Instruction] = instructions
        self.__tools: list[Tool] = tools
        self.__pictures: list[Picture] = pictures
        self.__required_time_minutes: int | None = required_time_minutes
        self.__recipe_usage_datetimes: list[datetime.datetime] = recipe_usage_datetimes

    @property
    def recipe_name(self) -> str:
        return self.__recipe_name

    @property
    def recipe_group_name(self) -> str:
        return self.__recipe_group_name

    @property
    def ingredients(self) -> list[Ingredient]:
        return self.__ingredients

    @property
    def instructions(self) -> list[Instruction]:
        return self.__instructions

    @property
    def tools(self) -> list[Tool]:
        return self.__tools

    @property
    def pictures(self) -> list[Picture]:
        return self.__pictures

    @property
    def required_time_minutes(self) -> int | None:
        return self.__required_time_minutes

    @property
    def recipe_usage_datetimes(self) -> list[datetime.datetime]:
        return self.__recipe_usage_datetimes

    def __str__(self) -> str:
        output: str = "Recipe:\n"
        output += "\tRecipe Name: {}\n".format(self.recipe_name)
        output += "\tRecipe Group Name: {}\n".format(self.recipe_group_name)
        output += "\tRequired Time Minutes: {}\n".format(self.required_time_minutes)
        output += "\tRecipe Usage Datetimes:\n"
        for usage_datetime in self.recipe_usage_datetimes:
            output += "\t\t{recipe_usage_datetime}\n".format(recipe_usage_datetime = usage_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        output += "\tPicture Count: {}\n".format(len(self.pictures))
        output += "\tTools:\n"
        for tool in self.tools:
            output += "\t\t{tool}\n".format(tool = tool)
        output += "\tInstructions:\n"
        for instruction in self.instructions:
            output += "\t\t{instruction}\n".format(instruction = instruction)
        output += "\tIngredients:\n"
        for ingredient in self.ingredients:
            ingredient_str: list[str] = str(ingredient).splitlines()
            for line in ingredient_str:
                output += "\t\t{line}\n".format(line = line)        

        return output
