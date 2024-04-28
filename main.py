from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'Data':{'Name': 'Arqam'}};

@app.get("/about")
def about():
    return {'About Us'}
