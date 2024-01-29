from typing import Union

from fastapi import FastAPI

from get_signal import recordSequence

app = FastAPI()

sequence = []

async def setup():
    while True:
        sequence = await recordSequence()


@app.get("/")
async def read_root():
    sequence = await recordSequence()
    return {"test": sequence}

setup()
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}