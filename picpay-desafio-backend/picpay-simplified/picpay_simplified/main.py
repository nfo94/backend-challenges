from fastapi import FastAPI
from api.routes import healthcheck, transactions, users

app = FastAPI()

app.include_router(healthcheck.router)
app.include_router(users.router)
app.include_router(transactions.router)
