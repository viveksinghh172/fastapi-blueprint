from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello World"}

@app.get("/greet")
def greet():
    return {"Message": "Hello Vivek!"}

@app.get("/greet/{name}")
def greet_name(name:str, age: int):
    return {"message": f"Hello {name} and you are {age} years old"}