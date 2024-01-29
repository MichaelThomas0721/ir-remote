from typing import Union

from fastapi import FastAPI

from get_signal import recordSequence

app = FastAPI()


@app.get("/")
async def read_root():
    sequence = await recordSequence()
    return {"test": sequence}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}