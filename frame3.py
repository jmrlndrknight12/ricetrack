import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame
from tkinter import ttk
import datetime
import pymysql
from PIL import Image, ImageTk

class RiceTrackerApp(CTk):
    def __init__(self):
        super().__init__()
        self.title('Rice Tracker')
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}")
        self.conn = self.connection()

        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = CTkFrame(self, width=self.screen_width, height=self.screen_height, fg_color="white")

        # Load background image
        background_image = Image.open("ricetrack.png")
        background_image = background_image.resize((1950, 1050))
        background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to hold the background image
        background_label = tk.Label(self.main_frame, image=background_photo)
        background_label.image = background_photo  # Keep a reference to avoid garbage collection

        # Place the label on the frame
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Type of Rice entry (ComboBox)
        label1 = CTkLabel(self.main_frame, text="Type of Rice:", font=('Arial', 15))
        label1.place(relx=0.13, rely=0.45, anchor="center")
        self.rice_types = ["White", "Blue", "Red"]
        self.rice_type_combo = ttk.Combobox(self.main_frame, values=self.rice_types, font=('Arial', 13))
        self.rice_type_combo.place(relx=0.28, rely=0.45, anchor="center", width=250, height=40)
        self.rice_type_combo.set("White")  # Set default value

        # Qty of Seeds entry (ComboBox)
        label2 = CTkLabel(self.main_frame, text="Qty of Seeds (sacks):", font=('Arial', 15))
        label2.place(relx=0.148, rely=0.53, anchor="center")
        self.quantity_values = list(range(1, 11))
        self.quantity_combo = ttk.Combobox(self.main_frame, values=self.quantity_values, font=('Arial', 13))
        self.quantity_combo.place(relx=0.28, rely=0.529, anchor="center", width=250, height=40)
        self.quantity_combo.set("1")  # Set default value

        # Date Planted entry with calendar
        label3 = CTkLabel(self.main_frame, text="Date Planted:", font=('Arial', 15))
        label3.place(relx=0.132, rely=0.6, anchor="center")
        self.date_entry = DateEntry(self.main_frame, width=12, background='#AF7A1F', foreground='white', borderwidth=2, font=('Arial', 13))
        self.date_entry.place(relx=0.28, rely=0.60, anchor="center",  width=250, height=40)
        # 'Add' button
        add_button = CTkButton(self.main_frame, text="ADD", font=('Century Gothic', 15, "bold"), fg_color="#018a33", width=250, height=40, corner_radius=6, command=self.add_to_database)
        add_button.place(relx=0.23, rely=0.75, anchor="center")

        # 'Rice Track' button
        rice_track_button = CTkButton(self.main_frame, text="RICE TRACK", font=('Century Gothic', 15, "bold"), fg_color="#018a33", width=250, height=40, corner_radius=6, command=self.show_rice_track)
        rice_track_button.place(relx=0.23, rely=0.82, anchor="center")
        
        
    def button_frame(self):
        button_frame = CTkFrame(self, width=self.screen_width, height=self.screen_height, bg_color="white", fg_color="white")
        button_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Button 1
        button1 = CTkButton(button_frame, text="W", command=self.button1_clicked, bg_color="white", fg_color="#edeef0", text_color="black", font=("Times New Roman", 80, "bold"), width=300, height=250)
        button1.place(relx=0.30, rely=0.5, anchor="center")

        # Button 2
        button2 = CTkButton(button_frame, text="B", command=self.button2_clicked, bg_color="white", fg_color="#0276fa", text_color="black", font=("Times New Roman", 80, "bold"), width=300, height=250)
        button2.place(relx=0.5, rely=0.5, anchor="center")

    # Button 3
        button3 = CTkButton(button_frame, text="R", command=self.button3_clicked, bg_color="white", fg_color="#ff0000", text_color="black", font=("Times New Roman", 80, "bold"), width=300, height=250)
        button3.place(relx=0.70, rely=0.5, anchor="center")


    def show_rice_track(self):
        # Check if any of the buttons is clicked
        if hasattr(self, "button_frame_shown") and self.button_frame_shown:
            # If button frame is already shown, hide it
            self.button_frame.destroy()
            self.button_frame_shown = False
        else:
            # If button frame is not shown, create it
            self.button_frame()
            self.button_frame_shown = True

    def create_rice_track_frame(self):
        # Destroy existing frame if present
        if hasattr(self, "rice_track_frame"):
            self.rice_track_frame.destroy()

        self.rice_track_frame = CTkFrame(self, width=self.screen_width, height=self.screen_height)
        self.rice_track_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create a Treeview
        columns = ('No. of socks', 'Rice Type', 'Date Planted', 'Estimated Date Harvest', 'Harvested Rice', 'Sacks Sold', 'Stocks', 'Sales')
        self.tree = ttk.Treeview(self.rice_track_frame, columns=columns, show='headings')
        self.tree.heading('No. of socks', text='No. of socks')
        self.tree.heading('Rice Type', text='Rice Type')
        self.tree.heading('Date Planted', text='Date Planted')
        self.tree.heading('Estimated Date Harvest', text='Estimated Date Harvest')
        self.tree.heading('Harvested Rice', text='Harvested Rice')
        self.tree.heading('Sacks Sold', text='Sacks Sold')
        self.tree.heading('Stocks', text='Stocks')
        self.tree.heading('Sales', text='Sales')
        self.tree.pack()  

        # Create a frame for the back button
        back_button_frame = CTkFrame(self.rice_track_frame)
        back_button_frame.place(relx=0.5, rely=0.9, anchor="center")

    # Back button
        back_button = CTkButton(back_button_frame, text="Rice Track", command=self.back_to_buttons)
        back_button.pack()

    def back_to_buttons(self):
    # Destroy Treeview frame and show button frame
        self.rice_track_frame.destroy()
        self.show_rice_track()


    def add_to_database(self):
        rice_type = self.rice_type_combo.get()
        date_planted = self.date_entry.get_date()
        quantity = int(self.quantity_combo.get())
        estimated_date_harvest = date_planted + datetime.timedelta(days=120)  # Assuming 120 days for harvest
        harvested_rice = quantity * 100  # Assuming 100 kg per sack
        sacks_sold = 0  # Initialize sacks sold
        stocks = harvested_rice - sacks_sold
        sales = 0  # Initialize sales
        # Insert data into the database
        try:
            cursor = self.conn.cursor()
            insert_query = "INSERT INTO rice_records (rice_type, date_planted, estimated_date_harvest, harvested_rice, sacks_sold, stocks, sales) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (rice_type, date_planted, estimated_date_harvest, harvested_rice, sacks_sold, stocks, sales))
            self.conn.commit()
            cursor.close()
            messagebox.showinfo("Success", "Data added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add data to database: {str(e)}")

    def button1_clicked(self):
        self.create_rice_track_frame()
        self.update_treeview("White")

    def button2_clicked(self):
        self.create_rice_track_frame()
        self.update_treeview("Blue")

    def button3_clicked(self):
        self.create_rice_track_frame()
        self.update_treeview("Red")

    def update_treeview(self, rice_color=None):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Fetch records from database based on rice color
        cursor = self.conn.cursor()
        if rice_color:
            select_query = "SELECT * FROM rice_records WHERE rice_type = %s"
            cursor.execute(select_query, (rice_color,))
        else:
            select_query = "SELECT * FROM rice_records"
            cursor.execute(select_query)
        records = cursor.fetchall()
        cursor.close()     
        # Populate Treeview with records
        for record in records:
            self.tree.insert('', 'end', values=record)

    def connection(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',  # Enter your MySQL password here
            db='ricetrackerdb',
        )
        return conn

if __name__ == "__main__":
    app = RiceTrackerApp()
    app.mainloop()
