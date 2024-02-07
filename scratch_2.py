import tkinter as tk
from tkinter import messagebox
import schedule
import time

def remind():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show reminder message
    messagebox.showinfo("Vitamin Reminder", "It's time to take your vitamins Angelina!")

# Schedule the reminder at 15:30 every day
schedule.every().day.at("15:30").do(remind)

try:
    # Infinite loop to keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Program stopped by user")


# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
