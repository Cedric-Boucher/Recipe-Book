from nutrition_info import Nutrition_Info
from ingredient_brand import Ingredient_Brand
from ingredient_type import Ingredient_Type

class Ingredient():
    def __init__(
        self,
        ingredient_type: Ingredient_Type,
        ingredient_brand: Ingredient_Brand,
        nutrition_info: Nutrition_Info
    ) -> None:
        assert (isinstance(ingredient_type, Ingredient_Type))
        assert (len(ingredient_type) > 0)
        assert (isinstance(ingredient_brand, Ingredient_Brand))
        assert (len(ingredient_brand) > 0)
        assert (isinstance(nutrition_info, Nutrition_Info))

        self.__ingredient_type: Ingredient_Type = ingredient_type
        self.__ingredient_brand: Ingredient_Brand = ingredient_brand
        self.__nutrition_info: Nutrition_Info = nutrition_info

    @property
    def ingredient_type(self) -> Ingredient_Type:
        return self.__ingredient_type

    @property
    def ingredient_brand(self) -> Ingredient_Brand:
        return self.__ingredient_brand

    @property
    def nutrition_info(self) -> Nutrition_Info:
        return self.__nutrition_info
