import tkinter as tk
from tkinter import messagebox, ttk

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("800x600")

        self.guest_list = []

        # Create a notebook for tabbed navigation
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.home_tab = ttk.Frame(self.notebook)
        self.guest_management_tab = ttk.Frame(self.notebook)
        self.services_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.home_tab, text="Home")
        self.notebook.add(self.guest_management_tab, text="Guest Management")
        self.notebook.add(self.services_tab, text="Services")

        # Initialize tab content
        self.create_home_page()
        self.create_guest_management_page()
        self.create_services_page()

    def create_home_page(self):
        """Create the home tab."""
        welcome_label = ttk.Label(
            self.home_tab, text="Welcome to the Hotel Management System", font=("Arial", 18)
        )
        welcome_label.pack(pady=20)

        # Navigation Buttons
        btn_guest_management = ttk.Button(
            self.home_tab, text="Go to Guest Management", command=lambda: self.notebook.select(self.guest_management_tab)
        )
        btn_guest_management.pack(pady=10)

        btn_services = ttk.Button(
            self.home_tab, text="View Services", command=lambda: self.notebook.select(self.services_tab)
        )
        btn_services.pack(pady=10)

    def create_guest_management_page(self):
        """Create the guest management tab."""
        frame = ttk.LabelFrame(self.guest_management_tab, text="Manage Guests")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Guest Name
        ttk.Label(frame, text="Guest Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_name = ttk.Entry(frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        # Room Number
        ttk.Label(frame, text="Room Number:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_room = ttk.Entry(frame)
        self.entry_room.grid(row=1, column=1, padx=5, pady=5)

        # Buttons for guest management
        btn_add = ttk.Button(frame, text="Add Guest", command=self.add_guest)
        btn_add.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        btn_delete = ttk.Button(frame, text="Delete Guest", command=self.delete_guest)
        btn_delete.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        btn_view = ttk.Button(frame, text="View Guests", command=self.view_guests)
        btn_view.grid(row=3, column=0, columnspan=2, pady=10)

        # Reserved Rooms List
        ttk.Label(frame, text="Reserved Rooms:").grid(row=4, column=0, columnspan=2, pady=5)
        self.reserved_rooms_list = tk.Listbox(frame, height=6)
        self.reserved_rooms_list.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

    def create_services_page(self):
        """Create the services tab."""
        frame = ttk.LabelFrame(self.services_tab, text="Available Services")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.services_list = tk.Listbox(frame, height=6)
        self.services_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Add example services
        self.services_list.insert(tk.END, "Room Service")
        self.services_list.insert(tk.END, "Laundry")
        self.services_list.insert(tk.END, "Spa")
        self.services_list.insert(tk.END, "Pool Access")

    def add_guest(self):
        name = self.entry_name.get()
        room = self.entry_room.get()
        if name and room:
            self.guest_list.append({'name': name, 'room': room})
            self.reserved_rooms_list.insert(tk.END, room)
            messagebox.showinfo("Success", f"Guest {name} added to Room {room}.")
            self.entry_name.delete(0, tk.END)
            self.entry_room.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both name and room number.")

    def delete_guest(self):
        name = self.entry_name.get()
        for guest in self.guest_list:
            if guest['name'] == name:
                self.guest_list.remove(guest)
                messagebox.showinfo("Success", f"Guest {name} has been deleted.")
                self.entry_name.delete(0, tk.END)
                self.update_reserved_rooms()
                return
        messagebox.showwarning("Error", f"No guest found with the name {name}.")

    def view_guests(self):
        if not self.guest_list:
            messagebox.showinfo("Guests", "No guests currently.")
            return

        guest_info = "\n".join([f"Name: {guest['name']}, Room: {guest['room']}" for guest in self.guest_list])
        messagebox.showinfo("Guests", guest_info)

    def update_reserved_rooms(self):
        self.reserved_rooms_list.delete(0, tk.END)
        for guest in self.guest_list:
            self.reserved_rooms_list.insert(tk.END, guest['room'])

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
