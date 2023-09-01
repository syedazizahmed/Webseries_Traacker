# Webseries_Traacker
The code provided is a Python script that uses the tkinter library to create a GUI application for tracking and recording web series. Here's a breakdown of the code:

1. The necessary imports are made, including tkinter, messagebox from tkinter, PIL's Image and ImageTk modules, and the json module.

2. The `TitleBar` class is defined, which represents the custom title bar of the application. It inherits from `tk.Frame` and creates a frame with close, minimize, and maximize buttons.

3. The `save_web_series` function is defined to save the recorded web series to a JSON file. It retrieves the series name and episodes watched from the entry field and writes the data to the "web_series.json" file.

4. The `episodes_watched_page` function is defined to display the page where the user can enter the number of episodes watched for a particular web series. It hides the main frame and shows the episodes frame. It also updates the selected series label with the chosen series name.

5. The `back_to_main` function is defined to return to the main frame from the episodes watched frame. It hides the episodes frame and view web series frame (if visible) and shows the main frame. It also clears the entry field and selected series label.

6. The `view_web_series` function is defined to view the recorded web series. It hides the main frame and shows the view web series frame. It retrieves the data from the "web_series.json" file, creates labels to display the series name and episodes watched, and updates the labels accordingly.

7. A list of default web series options is defined, each containing the series name and an image file path.

8. The `create_main_window` function is defined to create the main window and initialize the GUI application. It creates a tkinter window, sets the title, size, and background color. It creates the custom title bar, main frame, and packs labels and buttons for the default web series options. It also creates the episodes watched frame, view web series frame, and sets up various labels, entry fields, and buttons for user interaction. The main frame is initially shown.

9. The `__name__ == "__main__"` block checks if the script is being run directly and calls the `create_main_window` function to start the GUI application.

Overall, the code sets up a GUI application using tkinter to track and record web series. It allows users to select a web series, enter the number of episodes watched, save the data, view the recorded web series, and navigate between different frames.
