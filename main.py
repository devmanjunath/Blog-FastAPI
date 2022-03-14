from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"Manjunath PV"}}

@app.get("/about")
def about():
    return {"data":{"about":"Project created in 2022"}}