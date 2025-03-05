import subprocess
import tkinter as tk
from tkinter import messagebox

def get_wifi_profiles():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    return profiles
def get_wifi_password(profile):
    try:
        mesaj="s v b b b b b"
     

        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        password = None
        for line in results:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                return password
        return "No password found"
    except subprocess.CalledProcessError as e:
        return f"Error retrieving details: {str(e)}"
def show_password(event):
    selected_profile = listbox.get(listbox.curselection())
    password = get_wifi_password(selected_profile)
    messagebox.showinfo("Parola Wi-Fi ", f"Retea: {selected_profile}\nParola: {password}")

def create_gui():
    root = tk.Tk()
    root.title("Profile Wi-Fi ")

    global listbox
    listbox = tk.Listbox(root, width=50, height=15)
    listbox.pack(pady=20)

    profiles = get_wifi_profiles()
    for profile in profiles:
        listbox.insert(tk.END, profile)

    listbox.bind("<<ListboxSelect>>", show_password)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
