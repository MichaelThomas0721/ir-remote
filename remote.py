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

# Convert the data to a pretty-printed JSON string
json_data = json.dumps(prettify(keys), indent=2)

# Print the data to the console
print(json_data)

# Write the data to a text file
with open('decoded_ir_signal.txt', 'w') as file:
    file.write(json_data)