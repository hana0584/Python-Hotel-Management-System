import tkinter as tk
from tkinter import messagebox, ttk

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")

        self.guest_list = []

        # Create a main frame
        self.main_frame = tk.Frame(root, bg="#f5f5f5")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title = tk.Label(self.main_frame, text="Hotel Management System", font=("Arial", 24), bg="#f5f5f5")
        title.pack(pady=20)

        # Initialize pages
        self.pages = {}
        self.create_home_page()
        self.create_guest_management_page()
        self.create_services_page()

        # Show home page initially
        self.show_page("home")

    def create_home_page(self):
        """Create the home page."""
        frame = tk.Frame(self.main_frame, bg="#f5f5f5")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Welcome to the Hotel Management System", font=("Arial", 18), bg="#f5f5f5").pack(pady=20)

        btn_guest_management = tk.Button(frame, text="Go to Guest Management", command=lambda: self.show_page("guest_management"), bg="#2196F3", fg="white")
        btn_guest_management.pack(pady=10)

        btn_services = tk.Button(frame, text="View Services", command=lambda: self.show_page("services"), bg="#4CAF50", fg="white")
        btn_services.pack(pady=10)

        self.pages["home"] = frame

    def create_guest_management_page(self):
        """Create the guest management page."""
        frame = tk.Frame(self.main_frame, bg="#f5f5f5")

        # Guest Name Label and Entry
        tk.Label(frame, text="Guest Name:", bg="#f5f5f5").pack(pady=5)
        self.entry_name = tk.Entry(frame)
        self.entry_name.pack(pady=5)

        # Room Number Label and Entry
        tk.Label(frame, text="Room Number:", bg="#f5f5f5").pack(pady=5)
        self.entry_room = tk.Entry(frame)
        self.entry_room.pack(pady=5)

        # Add Guest Button
        btn_add = tk.Button(frame, text="Add Guest", command=self.add_guest, bg="#4CAF50", fg="white")
        btn_add.pack(pady=10)

        # Delete Guest Button
        btn_delete = tk.Button(frame, text="Delete Guest", command=self.delete_guest, bg="#f44336", fg="white")
        btn_delete.pack(pady=5)

        # View Guests Button
        btn_view = tk.Button(frame, text="View Guests", command=self.view_guests, bg="#2196F3", fg="white")
        btn_view.pack(pady=5)

        # Cleaning Status
        tk.Label(frame, text="Cleaning Status (Room Number):", bg="#f5f5f5").pack(pady=10)
        self.entry_cleaning = tk.Entry(frame)
        self.entry_cleaning.pack(pady=5)

        btn_clean = tk.Button(frame, text="Mark as Clean", command=self.mark_as_clean, bg="#4CAF50", fg="white")
        btn_clean.pack(pady=5)

        # Loyalty Points
        tk.Label(frame, text="Loyalty Points (Guest Name):", bg="#f5f5f5").pack(pady=10)
        self.entry_loyalty = tk.Entry(frame)
        self.entry_loyalty.pack(pady=5)

        btn_add_loyalty = tk.Button(frame, text="Add Loyalty Points", command=self.add_loyalty_points, bg="#2196F3", fg="white")
        btn_add_loyalty.pack(pady=5)

        # Information Desk
        tk.Label(frame, text="Expenses (Birr):", bg="#f5f5f5").pack(pady=10)
        self.entry_expenses = tk.Entry(frame)
        self.entry_expenses.pack(pady=5)

        btn_add_expense = tk.Button(frame, text="Add Expense", command=self.add_expense, bg="#FF9800", fg="white")
        btn_add_expense.pack(pady=5)

        # Reserved Rooms List
        tk.Label(frame, text="Reserved Rooms:", bg="#f5f5f5").pack(pady=10)
        self.reserved_rooms_list = tk.Listbox(frame)
        self.reserved_rooms_list.pack(pady=5, padx=10, fill=tk.X)

        # Save the frame
        self.pages["guest_management"] = frame

    def create_services_page(self):
        """Create the services page."""
        frame = tk.Frame(self.main_frame, bg="#f5f5f5")

        tk.Label(frame, text="Available Services", font=("Arial", 18), bg="#f5f5f5").pack(pady=20)

        self.services_list = tk.Listbox(frame)
        self.services_list.pack(pady=10, padx=10, fill=tk.X)
        self.services_list.insert(tk.END, "Room Service")
        self.services_list.insert(tk.END, "Laundry")
        self.services_list.insert(tk.END, "Spa")
        self.services_list.insert(tk.END, "Pool Access")

        tk.Button(frame, text="Back to Home", command=lambda: self.show_page("home"), bg="#2196F3", fg="white").pack(pady=10)

        self.pages["services"] = frame

    def show_page(self, page_name):
        """Show the specified page."""
        for page in self.pages.values():
            page.pack_forget()  # Hide all pages
        self.pages[page_name].pack(fill=tk.BOTH, expand=True)  # Show the selected page

    def add_guest(self):
        name = self.entry_name.get()
        room = self.entry_room.get()
        if name and room:
            self.guest_list.append({'name': name, 'room': room, 'points': 0, 'clean': False, 'expenses': 0})
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

        guest_info = "\n".join([f"Name: {guest['name']}, Room: {guest['room']}, Points: {guest['points']}, Clean: {'Yes' if guest['clean'] else 'No'}, Expenses: {guest['expenses']} Birr" for guest in self.guest_list])
        messagebox.showinfo("Guests", guest_info)

    def mark_as_clean(self):
        room = self.entry_cleaning.get()
        for guest in self.guest_list:
            if guest['room'] == room:
                guest['clean'] = True
                messagebox.showinfo("Success", f"Room {room} marked as clean.")
                self.entry_cleaning.delete(0, tk.END)
                return
        messagebox.showwarning("Error", f"No guest found in Room {room}.")

    def add_loyalty_points(self):
        name = self.entry_loyalty.get()
        for guest in self.guest_list:
            if guest['name'] == name:
                guest['points'] += 10  # Adding 10 points as an example
                messagebox.showinfo("Success", f"Added 10 loyalty points to {name}. Total Points: {guest['points']}.")
                self.entry_loyalty.delete(0, tk.END)
                return
        messagebox.showwarning("Error", f"No guest found with the name {name}.")

    def add_expense(self):
        name = self.entry_loyalty.get()
        expense = self.entry_expenses.get()
        if expense.isdigit():
            expense = int(expense)
            for guest in self.guest_list:
                if guest['name'] == name:
                    guest['expenses'] += expense
                    messagebox.showinfo("Success", f"Added {expense} Birr to {name}'s expenses.")
                    self.entry_expenses.delete(0, tk.END)
                    return
            messagebox.showwarning("Error", f"No guest found with the name {name}.")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid expense amount.")

    def update_reserved_rooms(self):
        self.reserved_rooms_list.delete(0, tk.END)
        for guest in self.guest_list:
            self.reserved_rooms_list.insert(tk.END, guest['room'])

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()