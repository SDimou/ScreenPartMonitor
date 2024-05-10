import pyautogui
import time

print("Press Ctrl-C to quit.")

try:
    while True:
        # Get and print the x, y coordinates of the mouse cursor.
        x, y = pyautogui.position()
        position_str = f'X: {x} Y: {y}'
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\nDone.')
