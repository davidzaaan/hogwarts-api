from pandas import DataFrame, read_csv
import numpy as np
import re


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
    # Characters DataFrame and Cleaning
    global CHARACTERS_DF
    CHARACTERS_DF = read_csv("data/characters.csv", converters={"Descr": str.strip, "Name": str.title})

    # Switching the index to start in 1
    CHARACTERS_DF.index = np.arange(1, len(CHARACTERS_DF) + 1)

    CHARACTERS_DF.fillna(value={
        "Gender": "Unknown", 
        "Descr": "This character does not have a description"
        },
        inplace=True
    )

    return CHARACTERS_DF.to_dict(orient='records')


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


def get_character(name: str) -> dict | None | bool:
        """
            Function that returns a JSON object with the character `name` given

            ### Params
                `name[str]`: The name of the character to look for\n
            
            ### Return
                `dict`: Will return a JSON (or Python dictionary) if a character was found
                `None`: Will return `None` if no character was found
                `False`: Will return `False` if there is more than one character with the name given
        """
        name: str = name.strip().title()
        names_filtered: str = filter_names(name)

        # names lookup
        name_regex = re.findall(r"{}[A-Za-z-']*\s?[A-Za-z-']*\s?[A-Za-z-']*\s?[A-Za-z-']*".format(name), names_filtered, re.I)

        if name_regex:
            if not len(name_regex) > 1:
                # get the character from the DataFrame
                character = CHARACTERS_DF.loc[CHARACTERS_DF["Name"] == name_regex[0]]

                # orient='records' returns a list, so access the only ocurrence
                return character.to_dict(orient='records')[0]
            
            return False
        
        return None


def filter_names(name: str) -> str:
    """
        Function that will return only names that match with the first 3 letters of the name given
        in the form of a string of comma separated names

        ### Params
            `name[str]`: Name to evaluate and filter
    """

    # filter names from the characters DataFramewho match with the first 3 letters with the name given
    names_filter: list = CHARACTERS_DF["Name"].str.startswith(name[:3], na=False)

    # return comma separated names to evaluate with regex
    return ",".join(CHARACTERS_DF.loc[names_filter, "Name"].to_list())