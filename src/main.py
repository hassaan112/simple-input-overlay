from stray import create_icon
from key_handling import set_overlay_keys, update_keys
from keys import Key
# import queue
import helper

root = helper.root_setup()
keys: dict[str, Key] = set_overlay_keys(root)
stray_icon = create_icon()
# event_queue = queue.Queue()

def main():
    stray_icon.run_detached()
    # for key in list(keys.values()):
    #     keyboard.on_press_key(key.text, lambda e: )


    while helper.running:
        update_keys(keys=keys)
        # try:
        #     event = event_queue.get_nowait()
        #     event.key_pressed()
        # except queue.Empty:
        #     pass
        root.update()
        root.update_idletasks()

main()