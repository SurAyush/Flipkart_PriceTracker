import tkinter as tk
from tkinter import messagebox
import csv

from pip._internal.utils import urls


def gui_win():
    def get_integer():
        try:
            value = int(threshold_entry.get())
            # Do something with the integer value
            if (value < 0):
                raise ValueError(-1)
            submit()

        except (ValueError):
            # Display an error message
            messagebox.showerror("Error", "Please enter a valid positive integer")

    def validate_url():
        url = url_entry.get().strip()  # Get the URL from the Entry widget
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")  # Show error message if URL is empty
            return False
        else:
            return True

    def validate_gmail():
        gmail = gmail_entry.get().strip()  # Get the URL from the Entry widget
        if not gmail:
            messagebox.showerror("Error", "Please enter a gmail.")  # Show error message if URL is empty
            return False
        else:
            return True

    def error_box():
        x = True
        x = validate_url()
        y = True
        y = validate_gmail()
        if (x and y):
            get_integer()

    url_list = []
    threshold_list = []
    gmail_list = []

    def submit():
        url = url_entry.get()
        threshold_price = threshold_entry.get()
        gmail = gmail_entry.get()
        url_list.append(url)
        threshold_list.append(threshold_price)
        gmail_list.append(gmail)

        messagebox.showinfo("Submitted", f"URL: {url}\nThreshold Price: {threshold_price}\nGmail: {gmail}")

        # Clear the input fields
        url_entry.delete(0, 'end')
        threshold_entry.delete(0, 'end')
        gmail_entry.delete(0, 'end')

    root = tk.Tk()
    root.title("Flipkart Price Tracker")
    root.geometry("600x300")
    root.minsize(600, 300)
    root.maxsize(600, 300)

    # Set background image
    bg_image = tk.PhotoImage(file=r"bg_img.png")
    bg_image_resized = bg_image.subsample(3)
    bg_label = tk.Label(root, image=bg_image_resized)
    bg_label.place(relwidth=0.5, relheight=2.5)
    bg_label.pack()

    def on_enter(event):
        submit_button.config(bg="#e0e0e0")

    def on_leave(event):
        submit_button.config(bg="SystemButtonFace")

    # URL Entry
    url_label = tk.Label(root, text="Enter URL:", font=("Helvetica", 12, "bold"))
    url_label.place(relx=0.1, rely=0.1)

    url_entry = tk.Entry(root, borderwidth=0.5, relief="solid")
    url_entry.place(relx=0.4, rely=0.1, relwidth=0.5)

    # Threshold Price Entry
    threshold_label = tk.Label(root, text="Enter Threshold Price:", font=("Helvetica", 12, "bold"))
    threshold_label.place(relx=0.1, rely=0.25)

    threshold_entry = tk.Entry(root, borderwidth=0.5, relief="solid")
    threshold_entry.place(relx=0.4, rely=0.25, relwidth=0.5)

    # gmail Entry
    gmail_label = tk.Label(root, text="Enter Gmail ID:", font=("Helvetica", 12, "bold"))
    gmail_label.place(relx=0.1, rely=0.4)

    gmail_entry = tk.Entry(root, borderwidth=0.5, relief="solid")
    gmail_entry.place(relx=0.4, rely=0.4, relwidth=0.5)

    # Submit Button
    submit_button = tk.Button(root, text="Submit", command=error_box, font=("Helvetica", 12, "bold"), borderwidth=1.6,
                              relief="solid")
    submit_button.place(relx=0.7, rely=0.7, relwidth=0.2)

    # Bind mouse events for hover effect
    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)

    root.mainloop()

    try:
        with open('data.csv', 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            for index,url in enumerate(url_list):
                data = [url,threshold_list[index],gmail_list[index]]
                writer.writerow(data)
    except:
        print("Error while writing into CSV files")

gui_win()