import tkinter as tk
from tkinter import messagebox

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("400x300")

        self.guest_list = []

        # Guest Name Label and Entry
        self.label_name = tk.Label(root, text="Guest Name:")
        self.label_name.pack(pady=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.pack(pady=5)

        # Room Number Label and Entry
        self.label_room = tk.Label(root, text="Room Number:")
        self.label_room.pack(pady=10)
        self.entry_room = tk.Entry(root)
        self.entry_room.pack(pady=5)
        
        # Add Guest Button
        self.btn_add = tk.Button(root, text="Add Guest", command=self.add_guest)
        self.btn_add.pack(pady=20)

        # View Guests Button
        self.btn_view = tk.Button(root, text="View Guests", command=self.view_guests)
        self.btn_view.pack(pady=5)

    def add_guest(self):
        name = self.entry_name.get()
        room = self.entry_room.get()
        if name and room:
            self.guest_list.append({'name': name, 'room': room})
            messagebox.showinfo("Success", f"Guest {name} added to Room {room}.")
            self.entry_name.delete(0, tk.END)
            self.entry_room.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both name and room number.")

    def view_guests(self):
        if not self.guest_list:
            messagebox.showinfo("Guests", "No guests currently.")
            return

        guest_info = "\n".join([f"Name: {guest['name']}, Room: {guest['room']}" for guest in self.guest_list])
        messagebox.showinfo("Guests", guest_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()