# Screen Monitoring and Alert System

This Python script monitors a specified region of the screen for changes and alerts the user when changes are detected. It also includes functionality to play an alert sound and display a popup message.

## Features

- **Screen Monitoring**: Monitors a specified region of the screen for changes.
- **Alert System**: Plays an alert sound and displays a popup message when changes are detected.
- **System Tray Icon**: Provides a system tray icon for easy access to program controls.
- **Overlay Window**: Creates a transparent overlay window with a green border around the monitored region.

## Dependencies

- **Python**: Version 3.6 or higher
- **OpenCV**: Open Source Computer Vision library for image processing
- **PyAutoGUI**: Cross-platform GUI automation library for Python
- **Tkinter**: Python's de-facto standard GUI (Graphical User Interface) package
- **Pygame**: Cross-platform set of Python modules designed for writing video games
- **PyStray**: Library for creating system tray icons in Python
- **Pillow**: Python Imaging Library (PIL fork) for opening, manipulating, and saving many different image file formats

## Installation

1. **Clone the Repository**: Clone this repository to your local machine.
   
    ```bash
    git clone <repository_url>
    ```

2. **Install Dependencies**: Install the required Python dependencies using pip.

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Script**: Execute the main Python script to start the screen monitoring and alert system.

    ```bash
    python screen_monitoring.py
    ```

2. **System Tray Icon**: Once the script is running, you can control the program using the system tray icon. Right-click on the icon to access the menu options.

3. **Adjust Configuration**: Modify the configuration variables in the `variables.py` file to customize the script according to your requirements.

## Configuration

- **Region**: Specify the region of the screen to monitor (x, y, width, height).
- **MP3 File Path**: Path to the MP3 file to play when an alert occurs.
- **Icon Path**: Path to the icon image used for the system tray icon.
- **Reference Image Path**: Path to save the reference image for comparison.
- **Current Image Path**: Path to save the current screenshot image for comparison.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
