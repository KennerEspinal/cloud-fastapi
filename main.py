from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Hello World!"])
def hello():
    return {"Hello": "World"}