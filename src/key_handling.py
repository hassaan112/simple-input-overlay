import json
from keys import Key
import keyboard

class InputHandler():
    def __init__(self, keys):
        # A set to track pressed keys
        self.held_keys = set()
        self.pressed = []
        self.released = []
        self.keys = keys
        # Hook the keyboard to listen for key events
        keyboard.hook(self.on_key_event)
    
    # Callback function that listens for key events
    def on_key_event(self, event):
        if event.event_type == keyboard.KEY_DOWN and event.name.upper() in self.keys:
            self.held_keys.add(event.name.upper())  # Add the key to the set when pressed
            self.pressed.append(event.name.upper())
        elif event.event_type == keyboard.KEY_UP and event.name.upper() in self.keys:
            self.held_keys.discard(event.name.upper())  # Remove the key from the set when released
            self.released.append(event.name.upper())

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
