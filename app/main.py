from fastapi import FastAPI

from app.database import Base, engine
from app.routers import products
from app.routers import approvals
from app.routers import slack

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
app.include_router(approvals.router)
app.include_router(slack.router)