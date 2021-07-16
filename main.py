from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Hi BePet"


@app.get('/welcome/{name}')
def get_welcome(name):
    return {"message":f"Hola {name}"}