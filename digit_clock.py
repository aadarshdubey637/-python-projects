import tkinter as tk
import winsound
from time import strftime

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")



# Function to update the time
def time():
    string = strftime('%H:%M:%S %p \n %A,%B %d,%Y')
    label.config(text=string)
    label.after(1000, time) # Call `time()` every 1000ms (1 second)

# Create the label widget
label = tk.Label(root, font=("calibri", 50, "bold"), background="black", foreground="white")
label.pack(anchor="center")  # Pack the label to make it visible
winsound.Beep(1000, 200)  


# Start updating the time
time()

# Run the main event loop
root.mainloop()

