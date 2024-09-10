from fastapi import FastAPI 
app = FastAPI()
app.title = "Mi Aplicacion En FastAPI"
@app.get('/')
def message():
    return "Hello World"