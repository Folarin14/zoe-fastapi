from fastapi import FastAPI
# from .repository import models
# from .repository.database import engine
from zoe.routers import finance_data

app = FastAPI()

# models.Base.metadata.create_all(engine)


@app.get('/')
def index():
    return "Test Home Page - Should be an HTML"


# app.include_router(users.router)
app.include_router(finance_data.router)
