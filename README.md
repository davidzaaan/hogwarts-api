# Hogwarts API
Welcome to my Hogwarts API. This API is inspired on the Harry Potter's books.
Ready to create awesome apps with Hogwarts most loved characters and its mysteries?
### *Dissendium!* 🌠

### Contents
- [Getting started](#getting-started)
- [Installation](#installation-steps)
- [Run server](#running-the-server)
- [Routes](#routes-and-data-access)
- [Authors](#authors)
- [Credits](#credits)

## Getting started
Up next I will provide you the instructions step-by-step to run this API on your local machine.

### Prerequisites
- `pip` version `>=22.3.1`
- `Python` version `>=3.10`

## Installation steps

**Note**: Be sure to create a new folder where you wish to have a copy of this repository.

First you have to clone this Git repository on your local machine within the folder you chose to install it with the following command:

`git clone https://github.com/davidzaaan/hogwarts-api.git`

In this case the cloning example will be using the HTTPS method but you can use the method of your preference.



This should leave you a folder with the following structure:
```
hogwarts-api/
    data/
    utils/
    harry.py
    .gitignore
    requirements.txt
    README.md
```

**Note:** It is recommended to create a Python virtual environment within the cloned repository folder in order to install all the required packages for this project. If you don't know what a virtual environment is and how to activate one. Up next I leave you a YouTube video that can help.

[Python Tutorial: VENV (Windows) - How to Use Virtual Environments with the Built-In venv Module](https://www.youtube.com/watch?v=APOPm01BVrk) - *by Corey Schafer*

---

**Note:** For this tutorial purposes we will call the new environment `env` but you can name it as you will.

**Note:** For this tutorial purposes the default command line that I'll be using is `Git Bash`

To activate your virtual environment run the following command on your preferred terminal:

```
username MINGW64 ~/OneDrive/Desktop/hogwarts-api (main)
$ virtualenv env
```

Once you have installed and activated successfully your environment you should have a folder structure like the following.

```
klener/
    env/
    data/
    utils/
    harry.py
    .gitignore
    README.md
    requirements.txt
```

And your terminal now should look like this with the activated environment

```
(env)
username MINGW64 ~/OneDrive/Desktop/hogwarts-api (main)
$ 
```

Now, install the packages with the command on your terminal

```
(env)
username MINGW64 ~/OneDrive/Desktop/hogwarts-api (main)
$ pip install -r requirements.txt
```

**Note**: `pip` installing commands can vary according to your Operative System and Python version. Be sure to have your `pip` and Python version up to date.


## Running the server

Because of this project works on a server we will use `uvicorn` for this purpose. The `FastAPI`'s main server.

Within the same folder you made the installation open a new terminal of your preference and run the following command

```
(env)
username MINGW64 ~/OneDrive/Desktop/hogwarts-api (main)
$ uvicorn harry:app --reload
```

The previous command should start a server and your command line should look like this

```
INFO:     Will watch for changes in these directories: ['C:\\Users\\<YOUR_USERNAME>\\Desktop\\hogwarts-api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1728] using WatchFiles
INFO:     Started server process [8116]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

That's it. You have your local version of **Hogwarts API** all set. Now, let's dive a little bit in the routes and how you can access the data.

# Routes and data access

## Characters

This route will return you an array of `JSON` objects or Python dictionaries `dict` containing all main data about Hogwarts characters.

### Routes

`/characters/` -> Return all characters

If any `Query` param is given, it will return the data related with the `name` of the character

*Example*

`/characters?name=harry potter` -> This will return the data related to **Harry Potter**

### Constraints with the `name` parameter

`name` is of type `str`

`name` length must be greater or equal to 3

`name` length must be less than or equal to 50

**Note:** The character lookup algorithm is greedy, so if you type for example:

`/characters?name=harry` It will return the data of **Harry Potter** anyways

as well as...

`/characters?name=har`

and...

`/characters?name=harry p`

or if the complete name is given

`/characters?name=harry potter`

### Return codes:
`200` Request was successful and it retrieved all the data

`404` No characters were found with the `Query` param `name` given

`409` It will return this code if the `Query` param with the `name` given has more than one match

## Spells

This route will return you a `JSON` object or Python dictionary `dict` containing all main data about all the spells casted in both movies and books in the form of Python dictionaries `dict`.

### Routes

`/spells/` -> Will return a dictionary will all the spells data

`/spells/{spell_id}` -> Will return the specific data from a certain spell such as its *Incantation* and type of spell.

### Constraints with the `spell_id` parameter

`spell_id` must be a positive integer `int`

### Return codes:
`200` Request was successful and it retrieved certain either spell data or all the spells

`404` No spells were found with the `Path` param `spell_id` given

## Places

This route will return you a `JSON` object or Python dictionary `dict` containing all main data about all the places where the story developed in the form of Python dictionaries `dict`.

### Routes

`/places/` -> Will return a dictionary will all the places data.

`/places/{place_id}` -> Will return the specific data from a certain place.

### Constraints with the `place_id` parameter

`place_id` must be a positive integer `int`

### Return codes:
`200` Request was successful and it retrieved certain either place data or all the places

`404` No places were found with the `Path` param `place_id` given

## Movies

This route will return you a `JSON` object or Python dictionary `dict` containing all main data about all **Harry Potter's** movies in the form of Python dictionaries `dict`.

### Routes

`/movies/` -> Will return a dictionary will all the movies data.

`/movies/{movie_id}` -> Will return the specific data from a certain movie.

### Constraints with the `place_id` parameter

`movie_id` must be a positive integer `int`

### Return codes:
`200` Request was successful and it retrieved either certain movie data or all the movies data

`404` No movies were found with the `Path` param `movie_id` given

## Authors

  **David Monroy** - *Project creator and developer* -
    [davidzaaan](https://github.com/davidzaaan)

## Credits
Special thanks to all the people who gathered the data that made this possible.

- *MARYNA ANTONEVYCH:* [https://www.kaggle.com/maricinnamon]
- *JOSÈ ROBERTO CANUTO:* [https://www.kaggle.com/zez000]
- *ELECTROCLASHH:* [https://www.kaggle.com/electroclashh]
- *Gulsah Demiryurek:* [https://www.kaggle.com/gulsahdemiryurek]