import os
import requests
from tkinter import *

class OneDriveManager:
    AUTH_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
    TOKEN_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/token"

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def window(self):
        win=Tk()
        
        win.title("OneDrive Manager")
        win.geometry("500x500")
        
        
        
    
    def get_auth_url(self):
        params = {
            'client_id': self.client_id,
            'scope': 'files.readwrite',
            'response_type': 'code',
            'redirect_uri': self.redirect_uri
        }
        r = requests.get(self.AUTH_URL, params=params)
        return r.url

    def get_token(self, auth_code):
        data = {
            'client_id': self.client_id,
            'scope': 'files.readwrite',
            'code': auth_code,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code',
            'client_secret': self.client_secret
        }
        r = requests.post(self.TOKEN_URL, data=data)
        return r.json().get("access_token")

    def upload_file(self, token, filepath, remote_path):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        with open(filepath, 'rb') as f:
            r = requests.put(f"https://graph.microsoft.com/v1.0/me/drive/root:/{remote_path}:/content", headers=headers, data=f)
        return r.status_code == 201

    def upload_folder(self, token, local_folder, remote_folder):
        for root, dirs, files in os.walk(local_folder):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, local_folder)
                remote_path = os.path.join(remote_folder, relative_path)
                self.upload_file(token, local_path, remote_path)


if __name__ == "__main__":
    CLIENT_ID = 'YOUR_CLIENT_ID'
    CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
    REDIRECT_URI = 'http://localhost:8000/'

    one_drive = OneDriveManager(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    print(f"Visit the following URL and get the auth code: {one_drive.get_auth_url()}")
    auth_code = input("Enter the Auth code: ")
    token = one_drive.get_token(auth_code)
    one_drive.upload_folder(token, "/path/to/local/folder", "/path/on/onedrive")
