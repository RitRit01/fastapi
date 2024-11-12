from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
async def hello():
    return {"message": "Hello world"}
