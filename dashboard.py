import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Intrusion Detection System Dashboard")
        self.root.geometry("800x500")

        # Text area
        self.alert_area = scrolledtext.ScrolledText(self.root, font=("Consolas", 12))
        self.alert_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Status label
        self.status_label = tk.Label(self.root, text="Total Alerts: 0", font=("Arial", 12))
        self.status_label.pack(anchor="w", padx=10)

        self.alert_count = 0

    def add_alert(self, alert_text):
        self.alert_count += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.alert_area.insert(tk.END, f"[{timestamp}] {alert_text}\n")
        self.status_label.config(text=f"Total Alerts: {self.alert_count}")
        self.alert_area.see(tk.END)

    def run(self):
        self.root.mainloop()
