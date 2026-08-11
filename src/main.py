from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
app = FastAPI()

@app.get("/")
def home():
    return {
        "Hello" : "World"
    }

# __________________________________________________________________________

@app.get("/brazilutc")
def utc():
    now = datetime.now(ZoneInfo("America/Sao_Paulo"))
    return {
        "horario" : now.strftime("%H:%M:%S"),
        "data" : now.strftime("%Y/%m/%d")
    }

# __________________________________________________________________________