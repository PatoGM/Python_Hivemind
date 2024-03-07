from fastapi import FastAPI
from global_variables import GLOBAL_VARIABLES

app = FastAPI()

@app.get("/")
async def display_status():
    print("got status")
    return GLOBAL_VARIABLES

@app.post("/webhook")
async def webhook_echo():
    print("got webhook")