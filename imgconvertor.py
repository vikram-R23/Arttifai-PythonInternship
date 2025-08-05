import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def convert_images(input_files, output_format, resize=None, quality=85):
    for file_path in input_files:
        try:
            with Image.open(file_path) as img:
                # Resize if specified
                if resize:
                    img = img.resize(resize)

                # Get output path
                base = os.path.splitext(file_path)[0]
                output_path = base + '.' + output_format.lower()

                # Save with compression quality
                img.save(output_path, output_format.upper(), quality=quality)
        except Exception as e:
            print(f"Error converting {file_path}: {e}")

def browse_files():
    file_paths = filedialog.askopenfilenames(title="Select Images")
    if file_paths:
        file_list.delete(0, tk.END)
        for path in file_paths:
            file_list.insert(tk.END, path)

def start_conversion():
    selected_files = file_list.get(0, tk.END)
    output_format = format_combo.get()
    resize_option = resize_entry.get()
    quality = int(quality_entry.get())

    # Resize format: width,height
    resize = None
    if resize_option:
        try:
            w, h = map(int, resize_option.split(','))
            resize = (w, h)
        except:
            messagebox.showerror("Resize Error", "Invalid resize format! Use: width,height")
            return

    if not selected_files or not output_format:
        messagebox.showwarning("Missing Info", "Please select images and output format.")
        return

    convert_images(selected_files, output_format, resize, quality)
    messagebox.showinfo("Done", "Images converted successfully!")

# GUI Setup
root = tk.Tk()
root.title("Image Converter")
root.geometry("450x400")

tk.Label(root, text="Upload Images").pack()
tk.Button(root, text="Browse", command=browse_files).pack()

file_list = tk.Listbox(root, width=60, height=6)
file_list.pack(pady=5)

tk.Label(root, text="Output Format").pack()
format_combo = ttk.Combobox(root, values=["png", "jpg", "bmp", "gif"])
format_combo.pack()

tk.Label(root, text="Resize (width,height)").pack()
resize_entry = tk.Entry(root)
resize_entry.pack()

tk.Label(root, text="Compression Quality (1–100)").pack()
quality_entry = tk.Entry(root)
quality_entry.insert(0, "85")
quality_entry.pack()

tk.Button(root, text="Convert", command=start_conversion, bg="green", fg="white").pack(pady=10)

root.mainloop()