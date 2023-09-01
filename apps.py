import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

class TitleBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pack(fill=tk.X)
        self.configure(bg="#12065F")
        self.create_widgets()

    def create_widgets(self):
        # Close button
        close_button = tk.Button(self, text="X", bg="#FF5C58", fg="white", command=self.master.destroy,
                                 font=("SF Pro", 12, "bold"))
        close_button.pack(side=tk.RIGHT)

        # Minimize button
        minimize_button = tk.Button(self, text="-", bg="#FFBD4F", fg="white", command=self.master.iconify,
                                    font=("SF Pro", 12, "bold"))
        minimize_button.pack(side=tk.RIGHT)

        # Maximize button
        self.maximized = False
        restore_button = tk.Button(self, text="[]", bg="#FFBD4F", fg="white", command=self.toggle_maximize,
                                   font=("SF Pro", 12, "bold"))
        restore_button.pack(side=tk.RIGHT)

    def toggle_maximize(self):
        if self.maximized:
            self.master.attributes("-zoomed", False)
            self.maximized = False
        else:
            self.master.attributes("-zoomed", True)
            self.maximized = True

# Function to save the recorded web series
def save_web_series(series_name, episodes_watched_entry):
    web_series = {
        "Name": series_name,
        "Episodes": episodes_watched_entry.get()
    }

    with open("web_series.json", "a") as file:
        json.dump(web_series, file)
        file.write("\n")

    messagebox.showinfo("Success", "Web series recorded successfully!")

# Function to display the number of episodes watched page
def episodes_watched_page(series_name):
    # Hide the main frame
    main_frame.pack_forget()

    # Create the episodes watched frame
    episodes_frame.pack()

    selected_series_label.config(text=series_name)

# Function to return to the main frame
def back_to_main():
    # Hide the episodes watched frame
    episodes_frame.pack_forget()

    # Hide the view web series frame
    view_frame.pack_forget()

    # Show the main frame
    main_frame.pack()

    # Clear the entry field
    episodes_watched_entry.delete(0, tk.END)

    # Clear the selected series label
    selected_series_label.config(text="")

# Function to view the recorded web series
def view_web_series():
    # Hide the main frame
    main_frame.pack_forget()

    # Show the view web series frame
    view_frame.pack()

    # Clear the previous data
    for label in view_series_labels.values():
        label.destroy()
    view_series_labels.clear()

    # Load and display the recorded web series
    with open("web_series.json", "r") as file:
        web_series_list = file.readlines()

    for web_series_json in web_series_list:
        web_series = json.loads(web_series_json)
        series_name = web_series['Name']
        episodes_watched = web_series['Episodes']

        if series_name not in view_series_labels:
            # Create a new entry
            series_info = f"Name: {series_name}\nEpisodes Watched: {episodes_watched}\n\n"
            label = tk.Label(view_frame, text=series_info, font=("SF Pro", 14), bg="#12065F", fg="white")
            label.pack()
            view_series_labels[series_name] = label
        else:
            # Update the episodes watched entry
            label = view_series_labels[series_name]
            label.config(text=f"Name: {series_name}\nEpisodes Watched: {episodes_watched}\n\n")

# Default web series options
default_web_series = [
    {"name": "Stranger Things", "image": r"c:\Users\Syed Aziz Ahmed\Downloads\R (3).jpg"},
    {"name": "Game of Thrones", "image": r"c:\Users\Syed Aziz Ahmed\Downloads\OIP (1).jpg"},
    {"name": "Breaking Bad", "image": r"c:\Users\Syed Aziz Ahmed\Downloads\R (4).jpg"},
    {"name": "Friends", "image": r"c:\Users\Syed Aziz Ahmed\Downloads\MV5BNDVkYjU0MzctMWRmZi00NTkxLTgwZWEtOWVhYjZlYjllYmU4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_FMjpg_UX1000_.jpg"},
    {"name": "The Office", "image": r"c:\Users\Syed Aziz Ahmed\Downloads\p7893511_b_v8_ab.jpg"}
]

# Function to create the main window
def create_main_window():
    global main_frame, episodes_frame, view_frame, view_series_labels, selected_series_label, episodes_watched_entry

    window = tk.Tk()
    window.title("Web Series Tracker")
    window.geometry("360x640")  # Set window size for mobile interface
    window.configure(bg="#12065F")

    # Create custom title bar
    title_bar = TitleBar(window)

    # Create main frame
    main_frame = tk.Frame(window, bg="#12065F")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Create and pack labels and buttons for default web series options
    series_name_label = tk.Label(main_frame, text="Select Web Series:", font=("SF Pro", 16, "bold"),
                                 fg="white", bg="#12065F")
    series_name_label.pack()

    row_frame = None
    for i, series in enumerate(default_web_series):
        if i % 2 == 0:
            row_frame = tk.Frame(main_frame, bg="#12065F")
            row_frame.pack()

        series_name = series["name"]
        series_image = Image.open(series["image"])
        series_image = series_image.resize((150, 150), Image.ANTIALIAS)
        series_photo = ImageTk.PhotoImage(series_image)

        button = tk.Button(row_frame, text=series_name, image=series_photo, compound=tk.TOP,
                           command=lambda series_name=series_name: episodes_watched_page(series_name),
                           font=("SF Pro", 14), bg="black", fg="white")
        button.photo = series_photo
        button.pack(side=tk.LEFT, padx=10, pady=10)

    # View recorded web series button
    view_button = tk.Button(main_frame, text="View Recorded Web Series", command=view_web_series,
                            font=("SF Pro", 14, "bold"), bg="black", fg="white")
    view_button.pack()

    # Create episodes watched frame
    episodes_frame = tk.Frame(window, bg="#12065F")

    series_label = tk.Label(episodes_frame, text="Web Series:", font=("SF Pro", 16, "bold"),
                            fg="white", bg="#12065F")
    series_label.pack()

    selected_series_label = tk.Label(episodes_frame, text="", font=("SF Pro", 14),
                                     fg="white", bg="#12065F")
    selected_series_label.pack()

    episodes_watched_label = tk.Label(episodes_frame, text="Number of Episodes Watched:",
                                      font=("SF Pro", 16, "bold"), fg="white", bg="#12065F")
    episodes_watched_label.pack()

    episodes_watched_entry = tk.Entry(episodes_frame, font=("SF Pro", 14))
    episodes_watched_entry.pack()

    back_button = tk.Button(episodes_frame, text="Back", command=back_to_main,
                            font=("SF Pro", 14, "bold"), bg="black", fg="white")
    back_button.pack(pady=10)

    save_button = tk.Button(episodes_frame, text="Save", command=lambda: save_web_series(selected_series_label.cget("text"), episodes_watched_entry),
                            font=("SF Pro", 14, "bold"), bg="black", fg="white")
    save_button.pack()

    # Create view web series frame
    view_frame = tk.Frame(window, bg="#12065F")

    back_to_main_button = tk.Button(view_frame, text="Back", command=back_to_main,
                                    font=("SF Pro", 14, "bold"), bg="black", fg="white")
    back_to_main_button.pack(pady=10)

    # Dictionary to store the view series labels
    view_series_labels = {}

    # Initially show the main frame
    main_frame.pack()

    window.mainloop()

# Run the program
if __name__ == "__main__":
    create_main_window()