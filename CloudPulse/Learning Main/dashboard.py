
import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path


# Find the CloudPulse project folder.
project_folder = Path(__file__).resolve().parent.parent

# Add the folder containing service.py to Python's import path.
oop_folder = project_folder / "OOP Concepts"
sys.path.insert(0, str(oop_folder))

# Import our existing backend service checker.
from service import Service


# Define the services that CloudPulse will monitor.
services = [
    Service("Example Website", "https://example.com"),
    Service("Python Website", "https://www.python.org"),
    Service("GitHub", "https://github.com"),
    Service("Google", "https://www.google.com")
]


# Check services and update the dashboard table.
def refresh_services():
    # Remove the previous results before displaying new ones.
    for item in table.get_children():
        table.delete(item)

    # Run each service's existing health check.
    for service in services:
        result = service.check_health()

        # Add the real results to the table.
        table.insert(
            "",
            "end",
            values=(
                result["name"],
                result["health"],
                (
                    f'{result["response_time_ms"]:.2f} ms'
                    if result["response_time_ms"] is not None
                    else "N/A"
                ),
                result["performance"]
            )
        )


# Create the main dashboard window.
root = tk.Tk()
root.title("CloudPulse - Service Health Dashboard")
root.geometry("750x400")

# Display the dashboard heading.
heading = ttk.Label(
    root,
    text="CloudPulse Health Dashboard",
    font=("Arial", 18, "bold")
)
heading.pack(pady=15)

# Create the results table.
columns = ("Service", "Health", "Response Time", "Performance")

table = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

# Configure the table headings and widths.
for column in columns:
    table.heading(column, text=column)
    table.column(column, width=170)

table.pack(fill="both", expand=True, padx=20, pady=10)

# Clicking this button runs the checks again.
refresh_button = ttk.Button(
    root,
    text="Refresh Services",
    command=refresh_services
)
refresh_button.pack(pady=10)

# Load real results when the dashboard starts.
refresh_services()

# Keep the window open.
root.mainloop()
