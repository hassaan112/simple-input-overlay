import pystray
from PIL import Image


def create_icon():
    from helper import on_closing
    image = Image.open("assets/keys.ico")
    icon = pystray.Icon("InpOverlay", image, "Hassaan's Input Overlay", menu=pystray.Menu(
        # pystray.MenuItem("Settings", lambda: open_settings(root)),
        pystray.MenuItem("Exit", lambda: on_closing(icon))
    ))

    return icon

def open_settings(root):
    pass