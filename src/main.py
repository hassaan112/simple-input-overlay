from stray import create_icon
from input_handling import InputHandler
from input_handling import set_overlay_inputs
from input_display import InputDisplay
import helper, keyboard


stray_icon = create_icon()
root = helper.root_setup(stray_icon)
inputs, has_keys, has_mouse_buttons = set_overlay_inputs(root)
input_handler = InputHandler(inputs, has_keys, has_mouse_buttons)

def overlay_update():
    if input_handler.pressed:
        for input in input_handler.pressed:
            inputs[input].pressed()
        input_handler.pressed = []    

    if input_handler.released:
        for input in input_handler.released:
            inputs[input].released()
        input_handler.released = []

    if input_handler.held_inputs:
        current_inputs = list(input_handler.held_inputs)
        for input in current_inputs:
            inputs[input].held()


def main():
    stray_icon.run_detached()
    while helper.running:
        # if keyboard.is_pressed("L"):
        #     root.withdraw()
        overlay_update()
        root.lift()
        root.update()
        root.update_idletasks()

main()