from fastapi import FastAPI, HTTPException, status, Query, Path

app = FastAPI()

CACHE: dict = {}


@app.get("/")
async def index():
    """
        #### Function that lists all the available routes and their usage
    """
    return CACHE


@app.get("/movies/")
async def movies_all():
    """
        #### Function that returns all movies data
    """
    if not "movies" in CACHE:
        from utils.data import movies_data
        CACHE["movies"] = movies_data()
        
    return CACHE["movies"]



@app.get("/movies/{movie_id}")
async def get_movie_by_id(
        movie_id: int = Path(
            title="Movie ID",
            description="The ID of the movie to retrieve data from",
            ge=0
        )
    ):
    """
        Function that returns JSON object based on the `movie_id` given

        ### Params
            `movie_id[int]`: Movie ID to get the data from
    """
    if not "movies" in CACHE:
        from utils.data import movies_data
        CACHE["movies"] = movies_data()

    try:
        return {"movie": CACHE["movies"][movie_id]}
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie with given ID does not exist")


@app.get("/characters/")
async def characters_all(
        character_name: str | None = Query(
            default=None,
            min_length=3,
            max_length=50,
            alias="name",
            regex="\w+"
        )
    ):
    """
        Function that returns all characters and their data

        ### Params
            `character_name[str | None]` Query param with the name of the character to retrieve data from
        
        ### Return
            `/characters/` will return Array of JSON objects with all the characters if no Query param is given \n
            `/characters?name=[str]` will JSON object with the character data
    """
    if not "characters" in CACHE:
        from utils.data import characters_data
        CACHE["characters"] = characters_data()

    if character_name:
        from utils.data import get_character
        character = get_character(character_name)
        
        if character is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character was not found")
        elif character is False:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Too many characters with the name given, can you be more specific?")


        return character

    return CACHE["characters"]


@app.get("/places/")
async def places_all():
    """
        #### Function that returns all places data
    """
    if not "places" in CACHE:
        from utils.data import places_data
        CACHE["places"] = places_data()

    return CACHE["places"]


@app.get("/places/{place_id}")
async def get_place_by_id(
        place_id: int  = Path(
            title="Place ID",
            description="The ID of the place to retrieve data from",
            ge=0
        )
    ):
    """
        Function that returns a JSON object based on the `place_id` given

        ### Params
            `place_id[int]`: Movie ID to get the data from
    """
    if not "places" in CACHE:
        from utils.data import places_data
        CACHE["places"] = places_data()

    try:
        return {"place": CACHE["places"][place_id]}
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Place with given ID does not exist")


@app.get("/spells/")
async def spells_all():
    """
        #### Function that returns all spells data
    """
    if not "spells" in CACHE:
        from utils.data import spells_data
        CACHE["spells"] = spells_data()

    return CACHE["spells"]


@app.get("/spells/{spell_id}")
async def get_spell_by_id(
        spell_id: int = Path(
            title="Spell ID",
            description="The ID of the spell to retrieve data from",
            ge=0
        )
    ):
    """
        Function that returns a JSON object based on the `spell_id`
        
        ### Params
            `spell_id[int]`: Spell ID to get the data from
    """
    if not "spells" in CACHE:
        from utils.data import spells_data
        CACHE["spells"] = spells_data()

    try:
        return {"spell": CACHE["spells"][spell_id]}
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Spell with given ID does not exist")