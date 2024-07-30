from nutrition_info import Nutrition_Info
from ingredient_brand import Ingredient_Brand
from ingredient_type import Ingredient_Type

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
