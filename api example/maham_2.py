import tkinter as tk
from tkinter import ttk

class HealthApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Health App")

        # Create tabs for different functionalities
        self.tab_control = ttk.Notebook(root)
        self.workout_tab = ttk.Frame(self.tab_control)
        self.progress_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.workout_tab, text='Workouts')
        self.tab_control.add(self.progress_tab, text='Progress')

        self.tab_control.pack(expand=1, fill='both')

        # Create components for the Workout tab
        self.workout_label = ttk.Label(self.workout_tab, text="Choose a workout:")
        self.workout_label.pack(pady=10)

        self.workout_combobox = ttk.Combobox(self.workout_tab, values=["Cardio", "Strength", "Flexibility"])
        self.workout_combobox.pack(pady=5)

        self.start_workout_button = ttk.Button(self.workout_tab, text="Start Workout", command=self.start_workout)
        self.start_workout_button.pack(pady=10)

        # Create components for the Progress tab
        self.progress_label = ttk.Label(self.progress_tab, text="Your progress:")
        self.progress_label.pack(pady=10)

        self.progress_text = tk.Text(self.progress_tab, height=10, width=40)
        self.progress_text.pack(padx=20, pady=5)

    def start_workout(self):
        selected_workout = self.workout_combobox.get()
        self.progress_text.insert(tk.END, f"Started {selected_workout} workout\n")

if __name__ == "_main_":
    root = tk.Tk()
    app = HealthApp(root)
    root.mainloop()