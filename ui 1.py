import tkinter as tk
from tkinter import filedialog
import subprocess
import os

cwd = os.getcwd()
rootpath = cwd.replace("\\", "/")

def browse_path(text_box):
    path = filedialog.askdirectory()
    text_box.delete(1.0, tk.END)  # Clear previous text
    text_box.insert(tk.END, path)
    check_next_button_state()  # Check if Next button should be enabled

def next_page():
    page_1_frame.grid_forget()
    page_2_frame.grid(row=0, column=0, padx=10, pady=10)
    check_next_button_state()  # Check whether to enable Next button

def previous_page():
    page_2_frame.grid_forget()
    page_1_frame.grid(row=0, column=0, padx=10, pady=10)

def check_next_button_state():
    if path2_text.get(1.0, tk.END).strip() == "":
        next_button.config(state=tk.DISABLED)
    else:
        next_button.config(state=tk.NORMAL)

def install_or_next():
    if path2_text.get(1.0, tk.END).strip() == "":
        return  # Do nothing if path2 is not selected
    elif install_button.cget("text") == "Next":  # If it's the second time clicking Next
        create_config_file()
    else:
        install()

def create_config_file():
    path1 = path1_text.get(1.0, tk.END).strip()
    path2 = path2_text.get(1.0, tk.END).strip()

    with open("config.properties", "w") as file:
        file.write(f"Path1={path1}\n")
        file.write(f"Path2={path2}\n")
        file.write(f"Path3={rootpath}/Application")

    print("Installation properties file created!")

    # Change the button text and command
    install_button.config(text="Install", command=install)

def install():
    # Execute the shell script
    # subprocess.run(r'D:\Logger\Application\copy.bat')

    # Make the Finish button visible
    install_button.grid_remove()
    finish_button.grid(row=1, column=2, pady=10)

def run_script():
    # Execute the shell script
    subprocess.run(r'D:\Logger\Application\copy.bat')

    # Close the Tkinter window after installation
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Installation")

# Page 1: Select Installation Path 1
page_1_frame = tk.Frame(root)

path1_label = tk.Label(page_1_frame, text="Select Installation Path :")
path1_label.grid(row=0, column=0, padx=10, pady=5)

path1_text = tk.Text(page_1_frame, height=1, width=50)
path1_text.grid(row=0, column=1, padx=10, pady=5)
path1_text.insert(tk.END, "C:/Program Files")

browse_button1 = tk.Button(page_1_frame, text="Browse", command=lambda: browse_path(path1_text))
browse_button1.grid(row=0, column=2, padx=10, pady=5)

next_button = tk.Button(page_1_frame, text="Next", command=next_page)
next_button.grid(row=1, column=1, pady=10)

page_1_frame.grid(row=0, column=0, padx=10, pady=10)

# Page 2: Select Installation Path 2
page_2_frame = tk.Frame(root)

path2_label = tk.Label(page_2_frame, text="Select Monitor Directory :")
path2_label.grid(row=0, column=0, padx=10, pady=5)

path2_text = tk.Text(page_2_frame, height=1, width=50)
path2_text.grid(row=0, column=1, padx=10, pady=5)

browse_button2 = tk.Button(page_2_frame, text="Browse", command=lambda: browse_path(path2_text))
browse_button2.grid(row=0, column=2, padx=10, pady=5)

previous_button = tk.Button(page_2_frame, text="Previous", command=previous_page)
previous_button.grid(row=1, column=0, pady=10)

install_button = tk.Button(page_2_frame, text="Next", command=install_or_next)
install_button.grid(row=1, column=1, pady=10)

# Create the Finish button and initially hide it
finish_button = tk.Button(page_2_frame, text="Finish", command=run_script)
finish_button.grid(row=1, column=2, pady=10)
finish_button.grid_remove()

# Run the main loop
root.mainloop()
