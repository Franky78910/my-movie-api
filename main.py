from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"
movies_list = [
    {
        "id": 1, 
        "title": "Deap POOL",
        "overview": "Comica Infantil",
        "year": 2024,
        "rating": 100.0
    },
    {
        "id": 2,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    },
    {
        "id": 3,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    },
    {
        "id": 4,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    },
    {
        "id": 5,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    },
    {
        "id": 6,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    },
    {
        "id": 7,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    },
    {
        "id": 8,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    },
    {
        "id": 9,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    },
    {
        "id": 10,
        "title": "Batman",
        "overview": "Comica",
        "year": 2011,
        "rating": 200.0
    }
    
]
@app.get('/', tags=["Home"])
def message():
    return HTMLResponse ('<h1> Hello world </h1>')
@app.get('/movies', tags=["Movies"])
def get_movies():
    return movies_list

@app.get('/movies/{id}' , tags=["Movies"])
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []    