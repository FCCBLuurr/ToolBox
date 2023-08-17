import os
from tkinter import Tk, filedialog

def rename_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    files = os.listdir(folder_path)
    folder_name = os.path.basename(folder_path)
    
    for index, file_name in enumerate(files):
        file_extension = os.path.splitext(file_name)[-1]
        new_file_name = f"{folder_name}_{index + 1}{file_extension}"
        
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file_name}' to '{new_file_name}'")

def browse_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder")
    return folder_path

if __name__ == "__main__":
    print("Select the folder containing the files to rename:")
    folder_path = browse_folder()
    
    if folder_path:
        rename_files(folder_path)
