from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello World"}

@app.get("/greet")
def greet():
    return {"Message": "Hello Vivek!"}