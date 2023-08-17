import os
from tkinter import Tk, filedialog, Label, Button

class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.selected_folder_path = None  # Newly introduced instance variable

    def setup_ui(self):
        # UI Setup is moved to a separate method for clarity and organization.
        self.root.title("File Renamer")
        self.root.geometry("200x150")
        self.root.resizable(False, False)
        # self.root.attributes("-toolwindow", True)

        self.folder_label = Label(self.root, text="Selected Folder: No folder selected")
        self.folder_label.pack(pady=10)

        browse_button = Button(self.root, text="Browse for Folder", command=self.select_folder)
        browse_button.pack(pady=5)

        self.rename_button = Button(self.root, text="Rename Files", command=self.rename_files_in_folder, state="disabled")
        self.rename_button.pack(pady=5)

        self.result_label = Label(self.root, text="")
        self.result_label.pack(pady=10)

    def select_folder(self):
        folder_path = browse_folder()
        if folder_path:
            self.selected_folder_path = folder_path  # The path is saved directly here
            self.folder_label.config(text=f"Selected Folder: {folder_path}")
            self.rename_button.config(state="normal")
    
    def rename_files_in_folder(self):
        if self.selected_folder_path:
            rename_files(self.selected_folder_path)
            self.result_label.config(text="Files renamed successfully!")
        else:
            self.result_label.config(text="No folder selected!")

def rename_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    folder_name = os.path.basename(folder_path)
    
    for index, file_name in enumerate(files):
        file_extension = os.path.splitext(file_name)[-1]
        new_file_name = f"{folder_name}_{index + 1}{file_extension}"
        
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file_name}' to '{new_file_name}'")
        except Exception as e:
            print(f"Error renaming '{file_name}': {e}")

def browse_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder")
    return folder_path

if __name__ == "__main__":
    root = Tk()
    app = FileRenamerApp(root)
    root.mainloop()
