#run this with the command uvicorn unitec_class:app
from fastapi import FastAPI

app = FastAPI(docs_url="/")

@app.get("/hello")
def blah():
    return "this is an api"