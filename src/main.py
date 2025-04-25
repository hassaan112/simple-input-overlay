from stray import create_icon
from key_handling import InputHandler
from key_handling import set_overlay_keys
from keys import Key
# import queue
import helper

stray_icon = create_icon()
root = helper.root_setup(stray_icon)
keys: dict[str, Key] = set_overlay_keys(root)
inp = InputHandler(keys=keys)
# event_queue = queue.Queue()

def overlay_update():
    if inp.pressed:
        for key in inp.pressed:
            keys[key].pressed()
        inp.pressed = []
    
    if inp.released:
        for key in inp.released:
            keys[key].released()
        inp.released = []
    if inp.held_keys:
        current_keys = list(inp.held_keys)
        for key in current_keys:
            keys[key].held()


def main():
    stray_icon.run_detached()
    # for key in list(keys.values()):
    #     keyboard.on_press_key(key.text, lambda e: )


    while helper.running:
        overlay_update()
        

        # current_keys = list(inp.pressed_keys)
        # for key in current_keys:
        #     keys[key].held()
        # update_keys(keys=keys)
        # try:
        #     event = event_queue.get_nowait()
        #     event.key_pressed()
        # except queue.Empty:
        #     pass
        root.lift()
        root.update()
        root.update_idletasks()

main()