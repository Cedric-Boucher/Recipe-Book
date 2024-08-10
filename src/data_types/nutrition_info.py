class Nutrition_Info():
    def __init__(
        self,
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
        micrograms_of_iodide_per_kilogram: float | None = None,
        milligrams_of_magnesium_per_kilogram: float | None = None,
        milligrams_of_zinc_per_kilogram: float | None = None,
        micrograms_of_selenium_per_kilogram: float | None = None,
        milligrams_of_copper_per_kilogram: float | None = None,
        milligrams_of_manganese_per_kilogram: float | None = None,
        micrograms_of_chromium_per_kilogram: float | None = None,
        micrograms_of_molybdenum_per_kilogram: float | None = None,
        milligrams_of_chloride_per_kilogram: float | None = None
    ) -> None:
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
        assert (isinstance(micrograms_of_iodide_per_kilogram, float) or micrograms_of_iodide_per_kilogram is None)
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

        self.__litres_per_kilogram: float = litres_per_kilogram
        self.__kilocalories_per_kilogram: int = kilocalories_per_kilogram
        self.__grams_of_fat_per_kilogram: float = grams_of_fat_per_kilogram
        self.__grams_of_saturated_fat_per_kilogram: float = grams_of_saturated_fat_per_kilogram
        self.__grams_of_trans_fat_per_kilogram: float = grams_of_trans_fat_per_kilogram
        self.__grams_of_carbohydrate_per_kilogram: float = grams_of_carbohydrate_per_kilogram
        self.__grams_of_dietary_fibre_per_kilogram: float = grams_of_dietary_fibre_per_kilogram
        self.__grams_of_sugars_per_kilogram: float = grams_of_sugars_per_kilogram
        self.__grams_of_protein_per_kilogram: float = grams_of_protein_per_kilogram
        self.__grams_of_cholesterol_per_kilogram: float = grams_of_cholesterol_per_kilogram
        self.__milligrams_of_sodium_per_kilogram: float = milligrams_of_sodium_per_kilogram
        self.__milligrams_of_potassium_per_kilogram: float = milligrams_of_potassium_per_kilogram
        self.__milligrams_of_calcium_per_kilogram: float = milligrams_of_calcium_per_kilogram
        self.__milligrams_of_iron_per_kilogram: float = milligrams_of_iron_per_kilogram
        self.__has_gluten: bool = has_gluten
        self.__is_meat: bool = is_meat
        self.__is_dairy: bool = is_dairy
        self.__is_animal_product: bool =is_animal_product 
        self.__is_nut: bool = is_nut
        self.__is_soy: bool = is_soy
        self.__grams_of_omega6_polyunsaturated_fat_per_kilogram: float | None = grams_of_omega6_polyunsaturated_fat_per_kilogram
        self.__grams_of_omega3_polyunsaturated_fat_per_kilogram: float | None = grams_of_omega3_polyunsaturated_fat_per_kilogram
        self.__grams_of_monounsaturated_fat_per_kilogram: float | None = grams_of_monounsaturated_fat_per_kilogram
        self.__grams_of_soluble_fibre_per_kilogram: float | None = grams_of_soluble_fibre_per_kilogram
        self.__grams_of_insoluble_fibre_per_kilogram: float | None = grams_of_insoluble_fibre_per_kilogram
        self.__grams_of_sugar_alcohols_per_kilogram: float | None = grams_of_sugar_alcohols_per_kilogram
        self.__grams_of_starch_per_kilogram: float | None = grams_of_starch_per_kilogram
        self.__micrograms_of_vitamin_a_per_kilogram: float | None = micrograms_of_vitamin_a_per_kilogram
        self.__milligrams_of_vitamin_c_per_kilogram: float | None = milligrams_of_vitamin_c_per_kilogram
        self.__micrograms_of_vitamin_d_per_kilogram: float | None = micrograms_of_vitamin_d_per_kilogram
        self.__milligrams_of_vitamin_e_per_kilogram: float | None = milligrams_of_vitamin_e_per_kilogram
        self.__micrograms_of_vitamin_k_per_kilogram: float | None = micrograms_of_vitamin_k_per_kilogram
        self.__milligrams_of_thiamine_per_kilogram: float | None = milligrams_of_thiamine_per_kilogram
        self.__milligrams_of_riboflavin_per_kilogram: float | None = milligrams_of_riboflavin_per_kilogram
        self.__milligrams_of_niacin_per_kilogram: float | None = milligrams_of_niacin_per_kilogram
        self.__milligrams_of_vitamin_b6_per_kilogram: float | None = milligrams_of_vitamin_b6_per_kilogram
        self.__micrograms_of_folate_per_kilogram: float | None = micrograms_of_folate_per_kilogram
        self.__micrograms_of_vitamin_b12_per_kilogram: float | None = micrograms_of_vitamin_b12_per_kilogram
        self.__micrograms_of_biotin_per_kilogram: float | None = micrograms_of_biotin_per_kilogram
        self.__milligrams_of_pantothenate_per_kilogram: float | None = milligrams_of_pantothenate_per_kilogram
        self.__milligrams_of_choline_per_kilogram: float | None = milligrams_of_choline_per_kilogram
        self.__milligrams_of_phosphorous_per_kilogram: float | None = milligrams_of_phosphorous_per_kilogram
        self.__micrograms_of_iodide_per_kilogram: float | None = micrograms_of_iodide_per_kilogram
        self.__milligrams_of_magnesium_per_kilogram: float | None = milligrams_of_magnesium_per_kilogram
        self.__milligrams_of_zinc_per_kilogram: float | None = milligrams_of_zinc_per_kilogram
        self.__micrograms_of_selenium_per_kilogram: float | None = micrograms_of_selenium_per_kilogram
        self.__milligrams_of_copper_per_kilogram: float | None = milligrams_of_copper_per_kilogram
        self.__milligrams_of_manganese_per_kilogram: float | None = milligrams_of_manganese_per_kilogram
        self.__micrograms_of_chromium_per_kilogram: float | None = micrograms_of_chromium_per_kilogram
        self.__micrograms_of_molybdenum_per_kilogram: float | None = micrograms_of_molybdenum_per_kilogram
        self.__milligrams_of_chloride_per_kilogram: float | None = milligrams_of_chloride_per_kilogram

    @property
    def litres_per_kilogram(self) -> float:
        return self.__litres_per_kilogram

    @property
    def kilocalories_per_kilogram(self) -> int:
        return self.__kilocalories_per_kilogram

    @property
    def grams_of_fat_per_kilogram(self) -> float:
        return self.__grams_of_fat_per_kilogram

    @property
    def grams_of_saturated_fat_per_kilogram(self) -> float:
        return self.__grams_of_saturated_fat_per_kilogram

    @property
    def grams_of_trans_fat_per_kilogram(self) -> float:
        return self.__grams_of_trans_fat_per_kilogram

    @property
    def grams_of_carbohydrate_per_kilogram(self) -> float:
        return self.__grams_of_carbohydrate_per_kilogram

    @property
    def grams_of_dietary_fibre_per_kilogram(self) -> float:
        return self.__grams_of_dietary_fibre_per_kilogram

    @property
    def grams_of_sugars_per_kilogram(self) -> float:
        return self.__grams_of_sugars_per_kilogram

    @property
    def grams_of_protein_per_kilogram(self) -> float:
        return self.__grams_of_protein_per_kilogram

    @property
    def grams_of_cholesterol_per_kilogram(self) -> float:
        return self.__grams_of_cholesterol_per_kilogram

    @property
    def milligrams_of_sodium_per_kilogram(self) -> float:
        return self.__milligrams_of_sodium_per_kilogram

    @property
    def milligrams_of_potassium_per_kilogram(self) -> float:
        return self.__milligrams_of_potassium_per_kilogram

    @property
    def milligrams_of_calcium_per_kilogram(self) -> float:
        return self.__milligrams_of_calcium_per_kilogram

    @property
    def milligrams_of_iron_per_kilogram(self) -> float:
        return self.__milligrams_of_iron_per_kilogram

    @property
    def has_gluten(self) -> bool:
        return self.__has_gluten

    @property
    def is_meat(self) -> bool:
        return self.__is_meat

    @property
    def is_dairy(self) -> bool:
        return self.__is_dairy

    @property
    def is_animal_product(self) -> bool:
        return self.__is_animal_product

    @property
    def is_nut(self) -> bool:
        return self.__is_nut

    @property
    def is_soy(self) -> bool:
        return self.__is_soy

    @property
    def grams_of_omega6_polyunsaturated_fat_per_kilogram(self) -> float | None:
        return self.__grams_of_omega6_polyunsaturated_fat_per_kilogram

    @property
    def grams_of_omega3_polyunsaturated_fat_per_kilogram(self) -> float | None:
        return self.__grams_of_omega3_polyunsaturated_fat_per_kilogram

    @property
    def grams_of_monounsaturated_fat_per_kilogram(self) -> float | None:
        return self.__grams_of_monounsaturated_fat_per_kilogram

    @property
    def grams_of_soluble_fibre_per_kilogram(self) -> float | None:
        return self.__grams_of_soluble_fibre_per_kilogram

    @property
    def grams_of_insoluble_fibre_per_kilogram(self) -> float | None:
        return self.__grams_of_insoluble_fibre_per_kilogram

    @property
    def grams_of_sugar_alcohols_per_kilogram(self) -> float | None:
        return self.__grams_of_sugar_alcohols_per_kilogram

    @property
    def grams_of_starch_per_kilogram(self) -> float | None:
        return self.__grams_of_starch_per_kilogram

    @property
    def micrograms_of_vitamin_a_per_kilogram(self) -> float | None:
        return self.__micrograms_of_vitamin_a_per_kilogram

    @property
    def milligrams_of_vitamin_c_per_kilogram(self) -> float | None:
        return self.__milligrams_of_vitamin_c_per_kilogram

    @property
    def micrograms_of_vitamin_d_per_kilogram(self) -> float | None:
        return self.__micrograms_of_vitamin_d_per_kilogram

    @property
    def milligrams_of_vitamin_e_per_kilogram(self) -> float | None:
        return self.__milligrams_of_vitamin_e_per_kilogram

    @property
    def micrograms_of_vitamin_k_per_kilogram(self) -> float | None:
        return self.__micrograms_of_vitamin_k_per_kilogram

    @property
    def milligrams_of_thiamine_per_kilogram(self) -> float | None:
        return self.__milligrams_of_thiamine_per_kilogram

    @property
    def milligrams_of_riboflavin_per_kilogram(self) -> float | None:
        return self.__milligrams_of_riboflavin_per_kilogram

    @property
    def milligrams_of_niacin_per_kilogram(self) -> float | None:
        return self.__milligrams_of_niacin_per_kilogram

    @property
    def milligrams_of_vitamin_b6_per_kilogram(self) -> float | None:
        return self.__milligrams_of_vitamin_b6_per_kilogram

    @property
    def micrograms_of_folate_per_kilogram(self) -> float | None:
        return self.__micrograms_of_folate_per_kilogram

    @property
    def micrograms_of_vitamin_b12_per_kilogram(self) -> float | None:
        return self.__micrograms_of_vitamin_b12_per_kilogram

    @property
    def micrograms_of_biotin_per_kilogram(self) -> float | None:
        return self.__micrograms_of_biotin_per_kilogram

    @property
    def milligrams_of_pantothenate_per_kilogram(self) -> float | None:
        return self.__milligrams_of_pantothenate_per_kilogram

    @property
    def milligrams_of_choline_per_kilogram(self) -> float | None:
        return self.__milligrams_of_choline_per_kilogram

    @property
    def milligrams_of_phosphorous_per_kilogram(self) -> float | None:
        return self.__milligrams_of_phosphorous_per_kilogram

    @property
    def micrograms_of_iodide_per_kilogram(self) -> float | None:
        return self.__micrograms_of_iodide_per_kilogram

    @property
    def milligrams_of_magnesium_per_kilogram(self) -> float | None:
        return self.__milligrams_of_magnesium_per_kilogram

    @property
    def milligrams_of_zinc_per_kilogram(self) -> float | None:
        return self.__milligrams_of_zinc_per_kilogram

    @property
    def micrograms_of_selenium_per_kilogram(self) -> float | None:
        return self.__micrograms_of_selenium_per_kilogram

    @property
    def milligrams_of_copper_per_kilogram(self) -> float | None:
        return self.__milligrams_of_copper_per_kilogram

    @property
    def milligrams_of_manganese_per_kilogram(self) -> float | None:
        return self.__milligrams_of_manganese_per_kilogram

    @property
    def micrograms_of_chromium_per_kilogram(self) -> float | None:
        return self.__micrograms_of_chromium_per_kilogram

    @property
    def micrograms_of_molybdenum_per_kilogram(self) -> float | None:
        return self.__micrograms_of_molybdenum_per_kilogram

    @property
    def milligrams_of_chloride_per_kilogram(self) -> float | None:
        return self.__milligrams_of_chloride_per_kilogram

    def __str__(self) -> str:
        output: str = "Nutrition Info:\n"
        output += "\tLitres Per Kilogram: {}\n".format(self.litres_per_kilogram)
        output += "\tKilocalories Per Kilogram: {}\n".format(self.kilocalories_per_kilogram)
        output += "\tGrams of Fat Per Kilogram: {}\n".format(self.grams_of_fat_per_kilogram)
        output += "\tGrams of Saturated Fat Per Kilogram: {}\n".format(self.grams_of_saturated_fat_per_kilogram)
        output += "\tGrams of Trans Fat Per Kilogram: {}\n".format(self.grams_of_trans_fat_per_kilogram)
        output += "\tGrams of Carbohydrate Per Kilogram: {}\n".format(self.grams_of_carbohydrate_per_kilogram)
        output += "\tGrams of Dietary Fibre Per Kilogram: {}\n".format(self.grams_of_dietary_fibre_per_kilogram)
        output += "\tGrams of Sugars Per Kilogram: {}\n".format(self.grams_of_sugars_per_kilogram)
        output += "\tGrams of Protein Per Kilogram: {}\n".format(self.grams_of_protein_per_kilogram)
        output += "\tGrams of Cholesterol Per Kilogram: {}\n".format(self.grams_of_cholesterol_per_kilogram)
        output += "\tMilligrams of Sodium Per Kilogram: {}\n".format(self.milligrams_of_sodium_per_kilogram)
        output += "\tMilligrams of Potassium Per Kilogram: {}\n".format(self.milligrams_of_potassium_per_kilogram)
        output += "\tMilligrams of Calcium Per Kilogram: {}\n".format(self.milligrams_of_calcium_per_kilogram)
        output += "\tMilligrams of Iron Per Kilogram: {}\n".format(self.milligrams_of_iron_per_kilogram)
        output += "\tContains Gluten: {}\n".format(self.has_gluten)
        output += "\tIs Meat: {}\n".format(self.is_meat)
        output += "\tIs Dairy: {}\n".format(self.is_dairy)
        output += "\tIs Animal Product: {}\n".format(self.is_animal_product)
        output += "\tIs Nut: {}\n".format(self.is_nut)
        output += "\tIs Soy: {}\n".format(self.is_soy)
        output += "\tGrams of Omega-6 Polyunsaturated Fat Per Kilogram: {}\n".format(self.grams_of_omega6_polyunsaturated_fat_per_kilogram)
        output += "\tGrams of Omega-3 Polyunsaturated Fat Per Kilogram: {}\n".format(self.grams_of_omega3_polyunsaturated_fat_per_kilogram)
        output += "\tGrams of Monounsaturated Fat Per Kilogram: {}\n".format(self.grams_of_monounsaturated_fat_per_kilogram)
        output += "\tGrams of Soluble Fibre Per Kilogram: {}\n".format(self.grams_of_soluble_fibre_per_kilogram)
        output += "\tGrams of Insoluble Fibre Per Kilogram: {}\n".format(self.grams_of_insoluble_fibre_per_kilogram)
        output += "\tGrams of Sugar Alcohols Per Kilogram: {}\n".format(self.grams_of_sugar_alcohols_per_kilogram)
        output += "\tGrams of Starch Per Kilogram: {}\n".format(self.grams_of_starch_per_kilogram)
        output += "\tMicrograms of Vitamin A Per Kilogram: {}\n".format(self.micrograms_of_vitamin_a_per_kilogram)
        output += "\tMilligrams of Vitamin C Per Kilogram: {}\n".format(self.milligrams_of_vitamin_c_per_kilogram)
        output += "\tMicrograms of Vitamin D Per Kilogram: {}\n".format(self.micrograms_of_vitamin_d_per_kilogram)
        output += "\tMilligrams of Vitamin E Per Kilogram: {}\n".format(self.milligrams_of_vitamin_e_per_kilogram)
        output += "\tMicrograms of Vitamin K Per Kilogram: {}\n".format(self.micrograms_of_vitamin_k_per_kilogram)
        output += "\tMilligrams of Thiamine Per Kilogram: {}\n".format(self.milligrams_of_thiamine_per_kilogram)
        output += "\tMilligrams of Riboflavin Per Kilogram: {}\n".format(self.milligrams_of_riboflavin_per_kilogram)
        output += "\tMilligrams of Niacin Per Kilogram: {}\n".format(self.milligrams_of_niacin_per_kilogram)
        output += "\tMilligrams of Vitamin B6 Per Kilogram: {}\n".format(self.milligrams_of_vitamin_b6_per_kilogram)
        output += "\tMicrograms of Folate Per Kilogram: {}\n".format(self.micrograms_of_folate_per_kilogram)
        output += "\tMicrograms of Vitamin B12 Per Kilogram: {}\n".format(self.micrograms_of_vitamin_b12_per_kilogram)
        output += "\tMicrograms of Biotin Per Kilogram: {}\n".format(self.micrograms_of_biotin_per_kilogram)
        output += "\tMilligrams of Pantothenate Per Kilogram: {}\n".format(self.milligrams_of_pantothenate_per_kilogram)
        output += "\tMilligrams of Choline Per Kilogram: {}\n".format(self.milligrams_of_choline_per_kilogram)
        output += "\tMilligrams of Phosphorous Per Kilogram: {}\n".format(self.milligrams_of_phosphorous_per_kilogram)
        output += "\tMicrograms of Iodide Per Kilograms: {}\n".format(self.micrograms_of_iodide_per_kilogram)
        output += "\tMilligrams of Magnesium Per Kilogram: {}\n".format(self.milligrams_of_magnesium_per_kilogram)
        output += "\tMilligrams of Zinc Per Kilogram: {}\n".format(self.milligrams_of_zinc_per_kilogram)
        output += "\tMicrograms of Selenium Per Kilogram: {}\n".format(self.micrograms_of_selenium_per_kilogram)
        output += "\tMilligrams of Copper Per Kilogram: {}\n".format(self.milligrams_of_copper_per_kilogram)
        output += "\tMilligrams of Manganese Per Kilogram: {}\n".format(self.milligrams_of_manganese_per_kilogram)
        output += "\tMicrograms of Chromium Per Kilogram: {}\n".format(self.micrograms_of_chromium_per_kilogram)
        output += "\tMicrograms of Molybdenum Per Kilogram: {}\n".format(self.micrograms_of_molybdenum_per_kilogram)
        output += "\tMilligrams of Chloride Per Kilogram: {}\n".format(self.milligrams_of_chloride_per_kilogram)

        return output
