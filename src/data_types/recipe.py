from ingredient import Ingredient
import datetime

class Recipe():
    def __init__(
        self,
        recipe_name: str,
        recipe_group_name: str,
        ingredients: list[Ingredient],
        instructions: list[str],
        tools: list[str],
        pictures: list[bytes],
        recipe_usage_datetimes: list[datetime.datetime],

    ) -> None:
        assert (isinstance(recipe_name, str))
        assert (isinstance(recipe_group_name, str))
        assert (isinstance(ingredients, list))
        for ingredient in ingredients:
            assert (isinstance(ingredient, Ingredient))
        assert (isinstance(instructions, list))
        for instruction in instructions:
            assert (isinstance(instruction, str))
        assert (isinstance(tools, list))
        for tool in tools:
            assert (isinstance(tool, str))
        assert (isinstance(pictures, list))
        for picture in pictures:
            assert (isinstance(picture, bytes))
        assert (isinstance(recipe_usage_datetimes, list))
        for recipe_usage_datetime in recipe_usage_datetimes:
            assert (isinstance(recipe_usage_datetime, datetime.datetime))

        self.__recipe_name: str = recipe_name
        self.__recipe_group_name: str = recipe_group_name
        self.__ingredients: list[Ingredient] = ingredients
        self.__instructions: list[str] = instructions
        self.__tools: list[str] = tools
        self.__pictures: list[bytes] = pictures
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
    def instructions(self) -> list[str]:
        return self.__instructions

    @property
    def tools(self) -> list[str]:
        return self.__tools

    @property
    def pictures(self) -> list[bytes]:
        return self.__pictures

    @property
    def recipe_usage_datetimes(self) -> list[datetime.datetime]:
        return self.__recipe_usage_datetimes
