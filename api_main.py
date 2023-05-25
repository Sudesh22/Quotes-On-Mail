import linecache, random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"home": "Route works"}

@app.get("/quote")
def newQuote():
    with open("Quotes.csv") as fp:
        No_of_Lines = len(fp.readlines())

    quote_list = linecache.getline("Quotes.csv", random.randint(0, No_of_Lines), module_globals=None).strip("\n").split(";")

    quote = quote_list[0]
    author = quote_list[1]
    genre = quote_list[2]

    return {"quote": quote, "author": author, "genre": genre}