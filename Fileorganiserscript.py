import os
import shutil

# Define categories and associated file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx"],
    "Music_Folder": [".mp3", ".wav", ".flac"],
    "Text_Folder": [".txt"],
    "Python_Folder": [".py"],
    "EXE_Folder": [".exe"],
    "Font_Folder": [".ttf", ".otf"],
    "Zip_Folder": [".zip", ".rar"],
    "Other_Folder": []
}

def get_category(filename):
    _, ext = os.path.splitext(filename.lower())
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Other_Folder"

def organize_files(target_dir):
    if not os.path.isdir(target_dir):
        print(" Invalid directory path.")
        return

    files = os.listdir(target_dir)
    for file in files:
        file_path = os.path.join(target_dir, file)
        if os.path.isfile(file_path):
            category = get_category(file)
            dest_dir = os.path.join(target_dir, category)

            # 🗂 Create category folder if it doesn't exist
            os.makedirs(dest_dir, exist_ok=True)

            #  Move the file
            try:
                shutil.move(file_path, os.path.join(dest_dir, file))
                print(f"Moved: {file} → {category}/")
            except Exception as e:
                print(f" Error moving {file}: {e}")

#  Change this to the folder you want to organize
organize_path = r"C:\Users\HP\OneDrive\Desktop"  # 🔁 Change this path
organize_files(organize_path)