import tkinter as tk
from tkinter import filedialog
from fix_litematica_import import fix_litematica_import
from support_optimizer import remove_slab_supports, replace_concrete_with_powder

# Functions for buttons
def open_file():
    global path
    litematic_filetypes = [("Litematic files", "*.litematic")]
    path = filedialog.askopenfilename(filetypes=litematic_filetypes, title="Select file")
    if path:
        label_archivo.config(text="Selected file:\n" + path, fg="blue")

def fix_NBT():
    fix_litematica_import(file_path=path)  # Calls the corresponding function
    label_message.config(text="NBT data fixed", fg="green")

def remove_slab_support():
    remove_slab_supports(file_path=path)  # Calls the corresponding function
    label_message.config(text="Slab supports removed", fg="green")

def replace_concrete():
    replace_concrete_with_powder(path)  # Calls the corresponding function
    label_message.config(text="Concrete replaced with powder", fg="green")

# Create main window
root = tk.Tk()
root.title("Mapart Tools")

# Window dimensions
root.geometry("550x330")  # Width x Height

# Label to display file path
label_archivo = tk.Label(root, text="Choose a litematic file.")
label_archivo.pack(pady=10)

# Frame to center buttons vertically
frame = tk.Frame(root)
frame.pack(expand=True)

# Buttons
btn_open = tk.Button(frame, text="Open File", command=open_file)
btn_open.pack(pady=10)

fix_NBT_btn = tk.Button(frame, text="Fix NBT data", command=fix_NBT)
fix_NBT_btn.pack(pady=10)

remove_slab_btn = tk.Button(frame, text="Remove slab supports", command=remove_slab_support)
remove_slab_btn.pack(pady=10)

replace_conc_btn = tk.Button(frame, text="Replace concrete with powder", command=replace_concrete)
replace_conc_btn.pack(pady=10)

# Label to display messages
label_message = tk.Label(root, text="")
label_message.pack(pady=10)

# Run the main window loop
root.mainloop()
