import pymysql
import tkinter as tk
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame, CTkImage
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess

# Define a function to handle the action when the "Continue" button is clicked
def continue_clicked():
    try:
        # Import frame2.py and execute its contents
        subprocess.run(["python", "frame2.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load frame2.py: {e}")

# Create the main application window
app = CTk()
app.title('frame1')

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}")


# Load and display the background image
original_img1 = Image.open("aboutbg.jpg")
resized_img1 = original_img1.resize((1950, 1000))  # Adjust the size to fit the window
img1 = ImageTk.PhotoImage(resized_img1)


# Create and pack the label with the background image
l1 = CTkLabel(master=app, image=img1)
l1.place(x=0, y=0, relwidth=1, relheight=1)

frame = CTkFrame(master=l1, width=350, height=500, corner_radius=20, bg_color='#e8220c', fg_color="#eeeeee")
frame.place(relx=0.5, rely=0.45, anchor="center")


# Create the "Continue" button and place it in front of the background image
continue_button = CTkButton(master=app, text="Continue", command=continue_clicked)
continue_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Start the Tkinter event loop
app.mainloop()
