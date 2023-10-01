import pyautogui
import time
import keyboard


def click_on_color(r, g, b):
    """
    Continuously checks the color of the pixel under the mouse cursor and clicks on it if it matches the specified RGB
    values. The function can be stopped by pressing the 'q' key.

    :param r: The red component of the RGB color to look for.
    :param g: The green component of the RGB color to look for.
    :param b: The blue component of the RGB color to look for.
    """
    while True:
        x, y = pyautogui.position()
        color = pyautogui.pixel(x, y)
        if color == (r, g, b):
            pyautogui.click(x, y)
        if keyboard.is_pressed('q'):
            break
        time.sleep(0.1)


click_on_color(75, 219, 106)
