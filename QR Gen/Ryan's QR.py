from tkinter import *
import tkinter as tk
from tkinter import filedialog
from MyQR import myqr
def generate_qr():
    url = url_entry.get()
    picName = iName.get()
    source = src.get()

#Actual QR function
    myqr.run(words=url, picture=source, version = 6, contrast=1.0, brightness=1.0,
         colorized=True, save_name= picName)

# Create the GUI
root = tk.Tk()
root.title("Ryan's QR")

# Create the URL entry
url_label = tk.Label(root, text="Enter the URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

#Source label
sauce = tk.Label(root, text="What's the source Image (add the extension: .png):")
sauce.pack()
src = tk.Entry(root)
src.pack()

#name label
name = tk.Label(root, text="Name the Qr code (add the extension: .png):")
name.pack()
iName = tk.Entry(root)
iName.pack()


# Create the generate button
generate_button = tk.Button(root, text="Generate", command=generate_qr)
generate_button.pack()

# Run the GUI
root.mainloop()