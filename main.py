from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def api_call():
    return "Hello World!"