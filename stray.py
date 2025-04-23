import pystray
from PIL import Image


def create_icon():
    image = Image.open("assets/keys.ico")
    icon = pystray.Icon("InpOverlay", image, "Hassaan's Input Overlay", menu=pystray.Menu(
        pystray.MenuItem("Exit", lambda: icon.stop())
    ))

    return icon