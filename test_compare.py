import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
import variables as var


def compare_images(img1, img2):
    """Compare two images and return the difference."""
    difference = cv2.absdiff(img1, img2)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    count = cv2.countNonZero(thresh)
    return count > 0  # True if there's a difference


def alert(diff):
    # Popup message
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    if diff == "same":
        messagebox.showinfo("Alert", "The two pictures are the same!")
    else:
        messagebox.showinfo("Alert", "The two pictures are different!")
    root.destroy()


if __name__ == "__main__":
    # Path to save the reference image
    reference_image_path = var.reference_image_path
    reference_image = cv2.imread(reference_image_path)
    current_image_path = var.current_image_path
    current_image = cv2.imread(current_image_path)

    # Create and save the initial reference image
    # screenshot = pyautogui.screenshot(region=region)
    # screen_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    # cv2.imwrite(reference_image_path, screen_image)

    if compare_images(current_image, reference_image):
        alert("diff")
    else:
        alert("same")
