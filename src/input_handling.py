import json
from input_display import InputDisplay
import keyboard, mouse

class InputHandler():
    def __init__(self, inputs, has_keys, has_mouse_buttons):
        # A set to track pressed inputs
        self.held_inputs = set()
        self.pressed = []
        self.released = []
        self.inputs = inputs
        # Hook the keyboard to listen for key events
        if has_keys:
            keyboard.hook(self.on_key_event)
        if has_mouse_buttons:
            mouse.hook(self.on_mouse_event)
    
    # Callback function that listens for key events
    def on_key_event(self, event):
        if event.name in self.inputs: # Check if the pressed/released key should be checked for
            if event.event_type == keyboard.KEY_DOWN:
                self.held_inputs.add(event.name)  # Add the key to the set when pressed
                self.pressed.append(event.name)
            elif event.event_type == keyboard.KEY_UP:
                self.held_inputs.discard(event.name)  # Remove the key from the set when released
                self.released.append(event.name)
        
    def on_mouse_event(self, event):
        if isinstance(event, mouse.ButtonEvent):
            if event.button in self.inputs: # Check if the pressed/released button should be checked for
                if event.event_type == 'down':
                    self.held_inputs.add(event.button)
                    self.pressed.append(event.button)
                elif event.event_type == 'up':
                    self.held_inputs.discard(event.button)  # Remove the key from the set when released
                    self.released.append(event.button)
                elif event.event_type == 'double':
                    self.held_inputs.add(event.button)
                    self.pressed.append(event.button)
    
def set_overlay_inputs(root):
    inputs = {}
    try:
        with open("data/selected_inputs.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: data.json not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in data.json.")

    
    for input in data["keys"]:
        inputs[input["input"]] = InputDisplay(root, input["name"], int(input["column"]), int(input["row"]), int(input["column-span"]), int(input["row-span"]), int(input["width"]), int(input["height"]))

    for input in data["mouse-buttons"]:
        inputs[input["input"]] = InputDisplay(root, input["name"], int(input["column"]), int(input["row"]), int(input["column-span"]), int(input["row-span"]), int(input["width"]), int(input["height"]))

    return inputs, len(data["keys"]), len(data["mouse-buttons"])
