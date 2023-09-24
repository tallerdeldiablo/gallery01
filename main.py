import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

# Function to get a list of image files in the current directory
def get_image_files(directory):
    image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(image_extensions)]
    return image_files

# Function to display the clicked image in the top screen
def show_preview_image(image_path):
    img = Image.open(image_path)
    img = img.resize((screen_width, screen_height - 150))
    img = ImageTk.PhotoImage(img)

    preview_label.configure(image=img)
    preview_label.image = img

# Function to play images as an infinite loop
def play_images():
    while True:
        for image_path in image_files:
            show_preview_image(image_path)
            root.update()
            time.sleep(2)  # Adjust the time interval between images

# Function to stop the image preview
def stop_preview():
    preview_label.configure(image=None)
    preview_label.image = None

# Function to handle image click event for preview
def image_click(image_path):
    show_preview_image(image_path)

# Function to create a left menu
def create_left_menu(root):
    menu_frame = ttk.Frame(root, style="TFrame")
    menu_frame.pack(side="left", fill="y")

    menu_label = ttk.Label(menu_frame, text="Menu", style="TLabel")
    menu_label.pack()

    new_button = ttk.Button(menu_frame, text="New", command=lambda: print("New button clicked"), style="TButton")
    new_button.pack()

    save_button = ttk.Button(menu_frame, text="Save", command=lambda: print("Save button clicked"), style="TButton")
    save_button.pack()

    credits_button = ttk.Button(menu_frame, text="Credits", command=lambda: print("Credits button clicked"), style="TButton")
    credits_button.pack()

# Function to display images in a gallery
def show_gallery(images):
    global root
    root = tk.Tk()
    root.title("Image Gallery")
    root.geometry(f"{screen_width}x{screen_height}")

    style = ttk.Style()
    style.configure("TFrame", background="light gray")
    style.configure("TLabel", background="light gray")
    style.configure("TButton", background="light gray")

    create_left_menu(root)

    frame = tk.Frame(root)
    frame.pack(side="bottom")

    preview_frame = tk.Frame(root)
    preview_frame.pack(side="top", fill="both", expand=True)

    global preview_label
    preview_label = tk.Label(preview_frame)
    preview_label.pack(fill="both", expand=True)

    play_button = ttk.Button(frame, text="Play", command=play_images, style="TButton")
    play_button.pack(side="left", padx=5, pady=5)

    stop_button = ttk.Button(frame, text="Stop", command=stop_preview, style="TButton")
    stop_button.pack(side="left", padx=5, pady=5)

    for image_path in images:
        img = Image.open(image_path)
        img.thumbnail((150, 150))  # Resize the image
        img = ImageTk.PhotoImage(img)

        label = tk.Label(frame, image=img)
        label.image = img
        label.pack(side="left", padx=5, pady=5)

        label.bind("<Button-1>", lambda event, image_path=image_path: image_click(image_path))

    root.mainloop()

if __name__ == "__main__":
    screen_width = 1920  # Full HD width
    screen_height = 1080  # Full HD height

    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_files = get_image_files(current_directory)

    if not image_files:
        print("No image files found in the current directory.")
    else:
        show_gallery(image_files)
