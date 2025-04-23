import json
from keys import Key


def set_overlay_keys(root):
    keys = {}
    try:
        with open("data/selectedkeys.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: data.json not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in data.json.")

    
    for key in data["keys"]:
        keys[key["key"]] = Key(root, key["key"], int(key["column"]), int(key["row"]), int(key["column-span"]), int(key["row-span"]), int(key["width"]), int(key["height"]))
    
    return keys

def update_keys(keys):
    for key in list(keys.values()):
        key.check_pressed()