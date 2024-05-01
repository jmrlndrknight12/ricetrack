import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame
from tkinter import ttk

class RiceTrackerApp(CTk):
    def __init__(self):
        super().__init__()
        self.title('Rice Tracker')
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}")

        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = CTkFrame(self, width=self.screen_width, height=self.screen_height, fg_color="white")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Type of Rice entry (ComboBox)
        label1 = CTkLabel(self.main_frame, text="Type of Rice:")
        label1.place(relx=0.5, rely=0.35, anchor="center")
        self.rice_types = ["White", "Blue", "Red"]
        self.rice_type_combo = ttk.Combobox(self.main_frame, values=self.rice_types)
        self.rice_type_combo.place(relx=0.5, rely=0.4, anchor="center")
        self.rice_type_combo.set("White")  # Set default value

        # Qty of Seeds entry (ComboBox)
        label2 = CTkLabel(self.main_frame, text="Qty of Seeds (sacks):")
        label2.place(relx=0.5, rely=0.5, anchor="center")
        self.quantity_values = list(range(1, 11))
        self.quantity_combo = ttk.Combobox(self.main_frame, values=self.quantity_values)
        self.quantity_combo.place(relx=0.5, rely=0.55, anchor="center")
        self.quantity_combo.set("1")  # Set default value

        # Date Planted entry with calendar
        label3 = CTkLabel(self.main_frame, text="Date Planted:")
        label3.place(relx=0.5, rely=0.6, anchor="center")
        self.date_entry = DateEntry(self.main_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.place(relx=0.5, rely=0.65, anchor="center")

        # 'Add' button
        add_button = CTkButton(self.main_frame, text="Add")
        add_button.place(relx=0.5, rely=0.75, anchor="center")

        # 'Rice Track' button
        rice_track_button = CTkButton(self.main_frame, text="Rice Track", command=self.show_rice_track)
        rice_track_button.place(relx=0.5, rely=0.8, anchor="center")

    def show_rice_track(self):
        self.main_frame.destroy()
        self.create_rice_track_frame()

    def create_rice_track_frame(self):
        rice_track_frame = CTkFrame(self, width=self.screen_width, height=self.screen_height, bg_color="white", fg_color="white")
        rice_track_frame.place(relx=0.5, rely=0.5, anchor="center")

        def button1_clicked():
            messagebox.showinfo("Button 1", "You clicked Button 1.")

        def button2_clicked():
            messagebox.showinfo("Button 2", "You clicked Button 2.")

        def button3_clicked():
            messagebox.showinfo("Button 3", "You clicked Button 3.")

        # Create a frame for the background with black color
        background_frame = CTkFrame(rice_track_frame, width=1000, height=300, bg_color="white", fg_color="black")
        background_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Button 1
        button1 = CTkButton(background_frame, text="W", command=button1_clicked, bg_color="black", fg_color="#ffffff", text_color="black", font=("Times New Roman", 80, "bold"), width=300, height=250)
        button1.place(relx=0.18, rely=0.5, anchor="center")

        # Button 2
        button2 = CTkButton(background_frame, text="B", command=button2_clicked, bg_color="black", fg_color="#0276fa", text_color="black", font=("Times New Roman", 80, "bold"), width=300, height=250)
        button2.place(relx=0.5, rely=0.5, anchor="center")

        # Button 3
        button3 = CTkButton(background_frame, text="R", command=button3_clicked, bg_color="black", fg_color="#ff0000", text_color="black", font=("Times New Roman", 80, "bold"), width=300, height=250)
        button3.place(relx=0.82, rely=0.5, anchor="center")

if __name__ == "__main__":
    app = RiceTrackerApp()
    app.mainloop()
