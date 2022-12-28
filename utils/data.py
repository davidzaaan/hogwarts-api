from pandas import DataFrame, read_csv
import numpy as np


def movies_data() -> dict:
    """
        #### Function that loads the movies DataFrame and format it
    """
    # DF loading...
    # Movies DataFrame and cleaning
    MOVIES_DF: DataFrame = read_csv("data/movies.csv", converters={
        "Budget": str.strip,
        "Box Office": str.strip
        })
    # Switching the index to start in 1
    MOVIES_DF.index = np.arange(1, len(MOVIES_DF) + 1)

    return MOVIES_DF.to_dict(orient='index')


def get_characters_dataframe() -> DataFrame:
    """
        #### Function that loads and returns the characters DataFrame
    """
    # Characters DataFrame and Cleaning
    characters_df = read_csv("data/characters.csv", converters={"Descr": str.strip})
    characters_df.fillna(value={
        "Gender": "Unknown", 
        "Descr": "This character does not have a description"
        },
        inplace=True
    )
    # Switching the index to start in 1
    characters_df.index = np.arange(1, len(characters_df) + 1)

    return characters_df

# Loading the DataFrame globally to use across functions that requires it
CHARACTERS_DF = get_characters_dataframe()


def characters_data() -> dict:
    """
        Function that formats the characters DataFrame into the form of a Python list of dictionaries

        ### Example
        ```
        [{
            "Name": "Harry Potter",
            "Link": "https://www.hp-lexicon.org/character/potter-family/harry-potter/",
            "Descr": "This is a description",
            "Gender": "Any",
            "Species/Race": "Any",
            ...
        },
        {
            ...
        }]
        ```
    """
    return CHARACTERS_DF.to_dict(orient='records')


def get_characters_listname() -> list:
    """
        #### Function that returns the `Name` column in the characters DataFrame in the form of a Python's list
    """
    return CHARACTERS_DF["Name"].to_list()


def places_data() -> dict:
    """
        #### Function that loads, format and returns the places DataFrame
    """
    # Places DataFrame and cleaning
    places_df: DataFrame = read_csv("data/places.csv")
    # Switching the index to start in 1
    places_df.index = np.arange(1, len(places_df) + 1)

    return places_df.to_dict(orient='index')


def spells_data() -> dict:
    """
        #### Function that loads, format and returns the spells DataFrame
    """
    # Spells DataFrame and cleaning
    spells_df: DataFrame = read_csv("data/spells.csv")
    spells_df.fillna(value={"Light": "Undetermined"}, inplace=True)
    # Switching the index to start in 1
    spells_df.index = np.arange(1, len(spells_df) + 1)

    return spells_df.to_dict(orient='index')


def get_character(name: str, list_of_names: list) -> str | None:
        """
            Function that returns a JSON object with the character `name` given

            ### Params
                `name[str]`: The name of the character to look for\n
                `list_of_names[list]`: The list of all the names existing in the characters DataFrame 
        """
        name = name.strip().title()
        if name in list_of_names:
            character: dict = CHARACTERS_DF.loc[CHARACTERS_DF["Name"] == name]
            return character.to_dict(orient='records')[0]
        
        return None


# Keep in mind
def filter_names(name: str, list_of_names: list) -> list:
    """
        ## Logic pending for this function...
    """
    names_filtered: list = list(filter(lambda char_name: char_name.lower().startswith(name[0]), list_of_names))
    return names_filtered