import cv2
import numpy as np
import pyautogui
import tkinter as tk
from tkinter import messagebox
import os
import ctypes

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import pystray
from PIL import Image
import threading
import time
import variables as var

# Path to the MP3 file to play
mp3_file_path = var.mp3_file_path

overlay_root = None
overlay_visible = False

# Create a hidden main window for Tkinter operations
main_thread_tk = tk.Tk()
main_thread_tk.withdraw()

# Constants for showing/hiding the console window
SW_HIDE = 0
SW_SHOW = 5

# Get a handle to the console window
console_window_handle = ctypes.windll.kernel32.GetConsoleWindow()


def create_overlay(region):
    """Create a transparent overlay window with a green border around the specified region."""
    global overlay_root
    overlay_root = tk.Tk()
    overlay_root.overrideredirect(True)  # Remove window border and controls
    overlay_root.geometry(
        f"{region[2]}x{region[3]}+{region[0]}+{region[1]}"
    )  # Match the size and position
    overlay_root.lift()
    overlay_root.wm_attributes("-topmost", True)
    overlay_root.wm_attributes("-transparentcolor", "blue")

    canvas = tk.Canvas(overlay_root, bg="blue", highlightthickness=0, bd=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.create_rectangle(
        1, 1, region[2] - 1, region[3] - 1, outline="green", width=2
    )

    overlay_root.mainloop()


def toggle_overlay():
    """Toggle the visibility of the overlay window."""
    global overlay_visible
    if overlay_visible:
        hide_overlay()
    else:
        show_overlay()


def show_overlay():
    """Show the overlay window."""
    global overlay_visible
    if not overlay_visible:
        region = (
            var.region
        )  # Specify the screen region to capture (x, y, width, height)
        threading.Thread(target=create_overlay, args=(region,), daemon=True).start()
        overlay_visible = True


def hide_overlay():
    """Hide the overlay window."""
    global overlay_visible, overlay_root
    if overlay_visible and overlay_root:
        overlay_root.destroy()
        overlay_root = None
        overlay_visible = False


def compare_images(img1, img2):
    """Compare two images and return the difference."""
    difference = cv2.absdiff(img1, img2)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    count = cv2.countNonZero(thresh)
    return count > 0  # True if there's a difference


def alert():
    """Play an alert sound and show a popup message."""
    # Play an MP3 file
    pygame.init()
    pygame.mixer.music.load(mp3_file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for the music to finish playing
        pygame.time.Clock().tick(10)
    pygame.quit()
    # Schedule the messagebox to be shown in the main thread
    # main_thread_tk.after(0, show_messagebox)


def show_messagebox():
    """Show a popup message on top of all other windows."""
    top = tk.Toplevel(main_thread_tk)
    top.withdraw()  # Hide the window
    top.attributes("-topmost", True)  # Ensure it is on top
    messagebox.showinfo("Προσοχή", "Έχεις νέα μηνύματα για ενέργεια!", parent=top)
    top.destroy()


def toggle_console_window():
    """Toggle the visibility of the console window."""
    if ctypes.windll.user32.IsWindowVisible(console_window_handle):
        ctypes.windll.user32.ShowWindow(console_window_handle, SW_HIDE)
    else:
        ctypes.windll.user32.ShowWindow(console_window_handle, SW_SHOW)


def create_system_tray_icon():
    """Create system tray icon and menu."""
    try:
        icon_image = Image.open(var.icon_path)
        menu = pystray.Menu(
            pystray.MenuItem(
                "Εμφάνιση/Απόκρυψη Περιοχής Ελέγχου", lambda: toggle_overlay()
            ),
            pystray.MenuItem(
                "Εμφάνιση/Απόκρυψη Παραθύρου Κονσόλας", lambda: toggle_console_window()
            ),
            pystray.MenuItem("Έξοδος", exit_program),
        )
        icon = pystray.Icon(
            "monitor_screen", icon_image, "Έλεγχος Μηνυμάτων Operator", menu
        )
        icon.run()
    except Exception as e:
        print("Error creating system tray icon: %s", e)


def exit_program(icon, item):
    """Exit the program."""
    icon.stop()
    os._exit(0)


def monitor_screen():
    """Monitor the specified region of the screen and alert if changes are detected."""
    # Specify the screen region to capture (x, y, width, height)
    region = var.region  # Adjust this to your needs

    # Path to save the reference image
    reference_image_path = var.reference_image_path

    # Create and save the initial reference image
    screenshot = pyautogui.screenshot(region=region)
    reference_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    cv2.imwrite(reference_image_path, reference_image)
    # reference_image = cv2.imread(reference_image_path)

    while True:
        # Capture the specified region of the screen
        screenshot = pyautogui.screenshot(region=region)
        # Convert the screenshot to a format that can be compared with OpenCV
        screen_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        cv2.imwrite(var.current_image_path, screen_image)

        # Compare the screenshot with the reference image
        if compare_images(screen_image, reference_image):
            alert()
            # Snooze detection for 15 minutes
            time.sleep(15 * 60)  # Sleep for 15 minutes (in seconds)

        # Add a delay between consecutive checks (adjust as needed)
        time.sleep(10)  # Check every 10 seconds


if __name__ == "__main__":
    # Begin the screen monitoring
    # print("Script path: ", var.script_dir)
    print("Monitoring", var.region)
    email_thread = threading.Thread(target=monitor_screen)
    email_thread.daemon = True
    email_thread.start()

    create_system_tray_icon()
    main_thread_tk.mainloop()  # Start the Tkinter main loop
