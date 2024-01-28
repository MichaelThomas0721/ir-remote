from piir.io import receive
from piir.decode import decode
from piir.prettify import prettify
import json

keys = {}

while True:
    data = decode(receive(8))
    if data:
        break
keys['keyname'] = data
print(json.dumps(prettify(keys), indent=2))