from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/home")
async def root():
    return {"message": "Home Page"}

@app.get("/about")
async def root():
    return {"message": "about what..."}