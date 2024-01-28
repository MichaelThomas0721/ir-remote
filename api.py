from typing import Union

from fastapi import FastAPI

from get_signal import getSequence

app = FastAPI()


@app.get("/")
def read_root():
    return {"test": getSequence}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}