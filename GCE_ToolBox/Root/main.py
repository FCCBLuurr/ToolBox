import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
from Tools.Rename_GCE_Photos import start

class AppWindow(tk.Tk):

    def __init__(self):

        super().__init__()
        
        self.title("GCE Tool Box")
        self.geometry("800x800")
        self.resizable(False, False)
        
        self.btn1 = tk.Button(self, text="Rename Coins", command=self.start_gce_function)
        self.btn1.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn2 = tk.Button(self, text="Button 2", command=self.script_function)
        self.btn2.grid(row=0, column=1, padx=10, pady=10)

    def start_gce_function(self):
        start.start_gce_app()
    
    def script_function(self):
        print("Dummy Script")

class LogInWindow(tk.Toplevel):

    def __init__(self, main_app):

        super().__init__()

        
        self.main_app = main_app
        
        self.title("Login")
        self.geometry("320x200")
        self.resizable(False, False)
        
        # Label
        self.label = tk.Label(self, text="Enter Username:")
        self.label.grid(row=0, column=0, columnspan=1, pady=10, padx=(2, 2), sticky=tk.W)
        
        # User Name Entry
        self.username_entry = tk.Entry(self, show='', width=35)
        self.username_entry.grid(row=0, column=1, columnspan=1, pady=10, padx=(2, 2), sticky=tk.EW)
        
        # Label
        self.label = tk.Label(self, text="Enter Password:")
        self.label.grid(row=1, column=0, columnspan=1, pady=10, padx=(2, 2), sticky=tk.W)
        
        # Password Entry
        self.password_entry = tk.Entry(self, show='*', width=35)
        self.password_entry.grid(row=1, column=1, columnspan=1, pady=10, padx=(2, 2), sticky=tk.EW)
        
        # Remember Me Checkbutton
        self.remember_var = tk.IntVar()
        self.remember_chk = tk.Checkbutton(self, text="Remember Me", variable=self.remember_var)
        self.remember_chk.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        
        # Login Button
        self.login_button = tk.Button(self, text="Login", command=self.check_password)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.password_entry.bind('<Return>', self.on_enter_pressed)
    
    def on_enter_pressed(self, event=None):

        self.check_password()
    
    def check_password(self):
        
        correct_username = "BLuurr"
        correct_password = "1234"
        
        entered_username = self.username_entry.get().strip()
        entered_password = self.password_entry.get().strip()
        
        # For demonstration purposes, I am using a hardcoded password "1234"
        if entered_username == correct_username and entered_password == correct_password:
            if self.remember_var.get() == 1:
                with open("config.txt", "w") as file:
                    file.write("1")

            self.main_app.deiconify()
            self.destroy()

        else:
            messagebox.showerror("Error", "Incorrect username or password!")

def read_login_state():
    
    try:
    
        with open("config.txt", "r") as file:
            state = file.read().strip()
    
            if state == "1":
                return True
    
    except FileNotFoundError:
        pass
    
    return False

if __name__ == "__main__":

    main_app = AppWindow()

    if not read_login_state():

        main_app.withdraw()
        LogInWindow(main_app)

    main_app.mainloop()
