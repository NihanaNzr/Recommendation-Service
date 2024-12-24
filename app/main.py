from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Recommendation Service", version="1.0")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recommendation Service"}
