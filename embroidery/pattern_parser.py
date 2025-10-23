from enum import StrEnum

import pandas as pd
from PIL import Image
from google import genai


class ColorsTable(StrEnum):
    CODE = "code"
    ID = "id"
    DESCRIPTION = "description"
    SKEIN_COUNT = "skeins"


class Models(StrEnum):
    GEMENI2_5 = "gemini-2.5-flash"


class PatternParser:
    def __init__(self):
        self.genai = genai.Client()

    def get_color_requirements(self, images: list[Image.Image]) -> pd.DataFrame | None:
        prompt = f"""
            Extract the data from this table and return it as comma-separated values. 
            Include the code number as '{ColorsTable.CODE.value}', color number as 
            '{ColorsTable.ID.value}', a description of the color as 
            '{ColorsTable.DESCRIPTION.value}', and the number of skeins required as 
            '{ColorsTable.SKEIN_COUNT.value}'. Make sure to keep the relationship 
            stable. Do not include any Python code, explanations, or dataframe creation.
            Just return the raw data with de-duplicated headers.
        """

        response = self.genai.models.generate_content(
            model=Models.GEMENI2_5, contents=[prompt, images]
        )

        try:
            colors_df = pd.read_csv(response.text)
            return colors_df
        except Exception as e:
            print(e)
