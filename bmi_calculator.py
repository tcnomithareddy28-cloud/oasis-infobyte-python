"""
BMI Calculator - Oasis Infobyte Python Internship
Project 2: BMI Calculator (Advanced - GUI with Tkinter)

Features:
- Weight & height input (kg/m or lbs/inches)
- BMI calculation & category display
- Color-coded result
- History storage (JSON file)
- View past records

No extra installs needed! Tkinter comes with Python.

Run:
    python bmi_calculator.py
"""

import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import datetime

# ── Data file for history ─────────────────────────────────────────────────────
HISTORY_FILE = "bmi_history.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_history(records):
    with open(HISTORY_FILE, "w") as f:
        json.dump(records, f, indent=2)


# ── BMI logic ─────────────────────────────────────────────────────────────────
def calculate_bmi(weight_kg, height_m):
    if height_m <= 0:
        raise ValueError("Height must be greater than 0")
    return round(weight_kg / (height_m ** 2), 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight", "#3498db"
    elif bmi < 25.0:
        return "Normal weight", "#2ecc71"
    elif bmi < 30.0:
        return "Overweight", "#f39c12"
    else:
        return "Obese", "#e74c3c"


def get_health_tip(category):
    tips = {
        "Underweight": "💡 Consider eating more nutritious foods and consult a doctor.",
        "Normal weight": "✅ Great job! Maintain your healthy lifestyle.",
        "Overweight": "💡 Try regular exercise and a balanced diet.",
        "Obese": "💡 Please consult a healthcare professional for guidance."
    }
    return tips.get(category, "")


# ── Main App ──────────────────────────────────────────────────────────────────
class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator - Oasis Infobyte")
        self.root.geometry("500x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")

        self.unit_var = tk.StringVar(value="metric")
        self.history = load_history()

        self.build_ui()

    def build_ui(self):
        # ── Title ──────────────────────────────────────────────────────────
        title = tk.Label(
            self.root, text="⚖️ BMI Calculator",
            font=("Helvetica", 22, "bold"),
            bg="#1a1a2e", fg="#e94560"
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self.root, text="Oasis Infobyte Internship - Project 2",
            font=("Helvetica", 9), bg="#1a1a2e", fg="#aaaaaa"
        )
        subtitle.pack()

        # ── Unit selector ──────────────────────────────────────────────────
        unit_frame = tk.Frame(self.root, bg="#1a1a2e")
        unit_frame.pack(pady=15)

        tk.Label(unit_frame, text="Units:", font=("Helvetica", 11),
                 bg="#1a1a2e", fg="white").pack(side="left", padx=5)

        tk.Radiobutton(unit_frame, text="Metric (kg/m)",
                       variable=self.unit_var, value="metric",
                       command=self.update_labels,
                       bg="#1a1a2e", fg="white", selectcolor="#16213e",
                       font=("Helvetica", 10)).pack(side="left", padx=10)

        tk.Radiobutton(unit_frame, text="Imperial (lbs/in)",
                       variable=self.unit_var, value="imperial",
                       command=self.update_labels,
                       bg="#1a1a2e", fg="white", selectcolor="#16213e",
                       font=("Helvetica", 10)).pack(side="left", padx=10)

        # ── Input frame ────────────────────────────────────────────────────
        input_frame = tk.Frame(self.root, bg="#16213e", padx=30, pady=20)
        input_frame.pack(padx=30, fill="x")

        # Name
        tk.Label(input_frame, text="Your Name (optional):",
                 font=("Helvetica", 11), bg="#16213e", fg="white").grid(
            row=0, column=0, sticky="w", pady=8)
        self.name_entry = tk.Entry(input_frame, font=("Helvetica", 12),
                                   width=20, bg="#0f3460", fg="white",
                                   insertbackground="white")
        self.name_entry.grid(row=0, column=1, pady=8, padx=10)

        # Weight
        self.weight_label = tk.Label(input_frame, text="Weight (kg):",
                                      font=("Helvetica", 11),
                                      bg="#16213e", fg="white")
        self.weight_label.grid(row=1, column=0, sticky="w", pady=8)
        self.weight_entry = tk.Entry(input_frame, font=("Helvetica", 12),
                                      width=20, bg="#0f3460", fg="white",
                                      insertbackground="white")
        self.weight_entry.grid(row=1, column=1, pady=8, padx=10)

        # Height
        self.height_label = tk.Label(input_frame, text="Height (m):",
                                      font=("Helvetica", 11),
                                      bg="#16213e", fg="white")
        self.height_label.grid(row=2, column=0, sticky="w", pady=8)
        self.height_entry = tk.Entry(input_frame, font=("Helvetica", 12),
                                      width=20, bg="#0f3460", fg="white",
                                      insertbackground="white")
        self.height_entry.grid(row=2, column=1, pady=8, padx=10)

        # ── Calculate button ───────────────────────────────────────────────
        calc_btn = tk.Button(
            self.root, text="Calculate BMI",
            font=("Helvetica", 13, "bold"),
            bg="#e94560", fg="white",
            activebackground="#c0392b",
            relief="flat", padx=20, pady=10,
            cursor="hand2",
            command=self.calculate
        )
        calc_btn.pack(pady=20)

        # ── Result frame ───────────────────────────────────────────────────
        self.result_frame = tk.Frame(self.root, bg="#16213e", padx=20, pady=15)
        self.result_frame.pack(padx=30, fill="x")

        self.bmi_label = tk.Label(
            self.result_frame, text="Your BMI: --",
            font=("Helvetica", 20, "bold"),
            bg="#16213e", fg="white"
        )
        self.bmi_label.pack()

        self.category_label = tk.Label(
            self.result_frame, text="Category: --",
            font=("Helvetica", 14),
            bg="#16213e", fg="white"
        )
        self.category_label.pack(pady=5)

        self.tip_label = tk.Label(
            self.result_frame, text="",
            font=("Helvetica", 10),
            bg="#16213e", fg="#aaaaaa",
            wraplength=400
        )
        self.tip_label.pack()

        # ── BMI Scale ──────────────────────────────────────────────────────
        scale_frame = tk.Frame(self.root, bg="#1a1a2e")
        scale_frame.pack(pady=10)

        ranges = [
            ("< 18.5\nUnderweight", "#3498db"),
            ("18.5–24.9\nNormal", "#2ecc71"),
            ("25–29.9\nOverweight", "#f39c12"),
            ("≥ 30\nObese", "#e74c3c"),
        ]
        for text, color in ranges:
            tk.Label(scale_frame, text=text, bg=color, fg="white",
                     font=("Helvetica", 8, "bold"),
                     width=11, height=2, relief="flat").pack(side="left", padx=2)

        # ── History button ─────────────────────────────────────────────────
        tk.Button(
            self.root, text="📋 View History",
            font=("Helvetica", 10),
            bg="#0f3460", fg="white",
            relief="flat", padx=10, pady=5,
            cursor="hand2",
            command=self.show_history
        ).pack(pady=10)

    def update_labels(self):
        if self.unit_var.get() == "metric":
            self.weight_label.config(text="Weight (kg):")
            self.height_label.config(text="Height (m):")
        else:
            self.weight_label.config(text="Weight (lbs):")
            self.height_label.config(text="Height (inches):")

    def calculate(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Please enter positive values!")
                return

            # Convert imperial to metric if needed
            if self.unit_var.get() == "imperial":
                weight = weight * 0.453592      # lbs to kg
                height = height * 0.0254        # inches to meters

            bmi = calculate_bmi(weight, height)
            category, color = get_category(bmi)
            tip = get_health_tip(category)

            # Update UI
            self.bmi_label.config(text=f"Your BMI: {bmi}", fg=color)
            self.category_label.config(text=f"Category: {category}", fg=color)
            self.tip_label.config(text=tip)

            # Save to history
            name = self.name_entry.get().strip() or "Anonymous"
            record = {
                "name": name,
                "bmi": bmi,
                "category": category,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            self.history.append(record)
            save_history(self.history)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height!")

    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No records yet!")
            return

        # New window
        hist_win = tk.Toplevel(self.root)
        hist_win.title("BMI History")
        hist_win.geometry("520x350")
        hist_win.configure(bg="#1a1a2e")

        tk.Label(hist_win, text="📋 BMI History",
                 font=("Helvetica", 16, "bold"),
                 bg="#1a1a2e", fg="#e94560").pack(pady=10)

        # Table
        cols = ("Name", "BMI", "Category", "Date")
        tree = ttk.Treeview(hist_win, columns=cols, show="headings", height=10)
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor="center")

        for r in reversed(self.history[-20:]):
            tree.insert("", "end", values=(
                r["name"], r["bmi"], r["category"], r["date"]
            ))

        tree.pack(padx=20, pady=10, fill="both", expand=True)

        tk.Button(hist_win, text="Clear History",
                  bg="#e94560", fg="white", relief="flat",
                  command=lambda: self.clear_history(hist_win)
                  ).pack(pady=5)

    def clear_history(self, window):
        self.history = []
        save_history(self.history)
        window.destroy()
        messagebox.showinfo("Done", "History cleared!")


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()