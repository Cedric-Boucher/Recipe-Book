from nutrition_info import Nutrition_Info

class Ingredient():
    def __init__(
        self,
        ingredient_type: str,
        ingredient_brand: str,
        nutrition_info: Nutrition_Info
    ) -> None:
        assert (isinstance(ingredient_type, str))
        assert (len(ingredient_type) > 0)
        assert (isinstance(ingredient_brand, str))
        assert (len(ingredient_brand) > 0)
        assert (isinstance(nutrition_info, Nutrition_Info))

        self.__ingredient_type: str = ingredient_type
        self.__ingredient_brand: str = ingredient_brand
        self.__nutrition_info: Nutrition_Info = nutrition_info

    @property
    def ingredient_type(self) -> str:
        return self.__ingredient_type

    @property
    def ingredient_brand(self) -> str:
        return self.__ingredient_brand

    @property
    def nutrition_info(self) -> Nutrition_Info:
        return self.__nutrition_info
