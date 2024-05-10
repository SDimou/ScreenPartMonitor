import tkinter as tk

# Your region tuple (x, y, width, height)
region = (503, 977, 18, 18)  # (456, 968, 97, 39)


def create_overlay(region):
    root = tk.Tk()
    # Removes the window decorations
    root.overrideredirect(True)
    # Makes the window stay on top
    root.wm_attributes("-topmost", True)
    # Skip the taskbar and alt+tab
    # root.wm_attributes("-skip_taskbar", True)
    # root.wm_attributes("-skip_alttab", True)

    # Set the window position
    root.geometry(f"+{region[0]}+{region[1]}")
    # Make the background of the window transparent
    root.wm_attributes("-transparentcolor", "blue")

    # Create a canvas to draw your rectangle
    canvas = tk.Canvas(root, width=region[2], height=region[3], highlightthickness=0)
    canvas.pack()

    # The color 'blue' here is used as the transparent color, thus not shown.
    # You may choose a different color for transparency, but ensure it's consistent
    canvas.configure(bg="blue")

    # Draw your rectangle, you can customize this per your needs
    border_width = 2
    canvas.create_rectangle(
        border_width / 2,
        border_width / 2,
        region[2] - border_width / 2,
        region[3] - border_width / 2,
        outline="green",
        width=border_width,
    )

    return root


try:
    while True:
        # Run the overlay
        overlay = create_overlay(region)
        overlay.mainloop()
except KeyboardInterrupt:
    print("\nDone.")
