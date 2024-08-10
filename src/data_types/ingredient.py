from data_types.nutrition_info import Nutrition_Info
from data_types.ingredient_brand import Ingredient_Brand
from data_types.ingredient_type import Ingredient_Type

class Ingredient():
    def __init__(
        self,
        ingredient_type: Ingredient_Type,
        ingredient_brand: Ingredient_Brand,
        nutrition_info: Nutrition_Info,
        amount_grams: int
    ) -> None:
        assert (isinstance(ingredient_type, Ingredient_Type))
        assert (len(ingredient_type) > 0)
        assert (isinstance(ingredient_brand, Ingredient_Brand))
        assert (len(ingredient_brand) > 0)
        assert (isinstance(nutrition_info, Nutrition_Info))
        assert (isinstance(amount_grams, int))
        assert (amount_grams > 0)

        self.__ingredient_type: Ingredient_Type = ingredient_type
        self.__ingredient_brand: Ingredient_Brand = ingredient_brand
        self.__nutrition_info: Nutrition_Info = nutrition_info
        self.__amount_grams: int = amount_grams

    @property
    def ingredient_type(self) -> Ingredient_Type:
        return self.__ingredient_type

    @property
    def ingredient_brand(self) -> Ingredient_Brand:
        return self.__ingredient_brand

    @property
    def nutrition_info(self) -> Nutrition_Info:
        return self.__nutrition_info

    @property
    def amount_grams(self) -> int:
        return self.__amount_grams

    def __str__(self) -> str:
        output: str = "Ingredient:\n"
        output += "\tIngredient Type: {}\n".format(self.ingredient_type)
        output += "\tIngredient Brand: {}\n".format(self.ingredient_brand)
        output += "\tAmount Grams: {}\n".format(self.amount_grams)
        nutrition_info_str: list[str] = str(self.nutrition_info).splitlines()
        for line in nutrition_info_str:
            output += "\t{line}\n".format(line = line)

        return output
