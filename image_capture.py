from PIL import Image, ImageDraw
import pyautogui

# Your region tuple (x, y, width, height)
region = (458, 969, 97, 39)

# Create an RGBA Image of the size of the region with a transparent background
img = Image.new("RGBA", (region[2], region[3]), (0, 0, 0, 0))

# Create a draw object
draw = ImageDraw.Draw(img)

# Define the border width and color
border_width = 2
color = "green"

# Draw a rectangle on the edges of the image to represent the border
draw.rectangle([0, 0, region[2]-border_width, region[3]-border_width], outline=color, width=border_width)

# Save the image if you want to see it as a file (optional)
img.save("border_overlay.png")

# Show the image on the screen using pyautogui
# Pyautogui's locateOnScreen function can be used to display the overlay at the correct screen location
# However, pyautogui does not support direct overlay, so we'll display the image temporarily
screen_img = pyautogui.screenshot(region=region)
overlay_img = Image.alpha_composite(screen_img.convert("RGBA"), img)
overlay_img.show()

# Note: This will open the image in your default image viewer, 
# not as an overlay on your screen due to limitations in pyautogui/PIL for direct screen manipulation.
