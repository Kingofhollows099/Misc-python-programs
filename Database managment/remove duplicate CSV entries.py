import csv
from tkinter import Tk, Label, Button, filedialog, messagebox, StringVar, BooleanVar, Checkbutton, Frame, Toplevel, Scrollbar, Canvas
import tkinter as tk


def remove_duplicate_passwords():
    class DuplicatePasswordApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Duplicate Password Remover")

            self.input_file = None
            self.output_file = None
            self.rows = []
            self.match_columns = []
            self.fieldnames = []

            self.mode = StringVar(value="auto")
            self.current_duplicates = []
            self.unique_rows = []
            self.seen_values = {}
            self.selected_columns = []

            self.setup_ui()

        def setup_ui(self):
            Label(self.root, text="Select Mode:").grid(row=0, column=0, pady=10)

            Button(self.root, text="Open CSV", command=self.open_file).grid(row=0, column=1, padx=10)
            Button(self.root, text="Save As", command=self.save_file).grid(row=0, column=2, padx=10)

            Checkbutton(self.root, text="Automatic", variable=self.mode, onvalue="auto").grid(row=1, column=0, sticky="w")
            Checkbutton(self.root, text="Interactive", variable=self.mode, onvalue="interactive").grid(row=1, column=1, sticky="w")

            Button(self.root, text="Start", command=self.start_processing).grid(row=2, column=0, columnspan=3, pady=10)

        def open_file(self):
            self.input_file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
            if not self.input_file:
                messagebox.showerror("Error", "No file selected.")
                return

            with open(self.input_file, "r", newline="", encoding="utf-8") as infile:
                reader = csv.DictReader(infile)
                self.rows = list(reader)
                self.fieldnames = reader.fieldnames

                if not self.fieldnames:
                    messagebox.showerror("Error", "The selected CSV file has no columns.")
                    return

                self.select_columns()

        def save_file(self):
            self.output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if not self.output_file:
                messagebox.showerror("Error", "No output file selected.")

        def select_columns(self):
            top = Toplevel(self.root)
            top.title("Select Columns to Match")

            Label(top, text="Select the columns to use for identifying duplicates:").pack(pady=10)

            column_frame = Frame(top)
            column_frame.pack(pady=10)

            self.column_vars = {}
            for column in self.fieldnames:
                var = BooleanVar()
                Checkbutton(column_frame, text=column, variable=var).pack(anchor="w")
                self.column_vars[column] = var

            Button(top, text="Confirm", command=lambda: self.confirm_columns(top)).pack(pady=10)

        def confirm_columns(self, window):
            self.selected_columns = [col for col, var in self.column_vars.items() if var.get()]
            if not self.selected_columns:
                messagebox.showerror("Error", "No columns selected.")
                return

            window.destroy()

        def start_processing(self):
            if not self.input_file or not self.output_file:
                messagebox.showerror("Error", "Please select both input and output files.")
                return

            if not self.selected_columns:
                messagebox.showerror("Error", "Please select columns to match against.")
                return

            if self.mode.get() == "auto":
                self.auto_mode()
            elif self.mode.get() == "interactive":
                self.interactive_mode()

        def auto_mode(self):
            seen_values = set()
            unique_rows = []

            for row in self.rows:
                key = tuple(row[col] for col in self.selected_columns)
                if key not in seen_values:
                    seen_values.add(key)
                    unique_rows.append(row)

            self.write_output(unique_rows)
            messagebox.showinfo("Success", f"Duplicates removed. Output saved to {self.output_file}.")

        def interactive_mode(self):
            self.seen_values = {}
            for row in self.rows:
                key = tuple(row[col] for col in self.selected_columns)
                if key not in self.seen_values:
                    self.seen_values[key] = [row]
                else:
                    self.seen_values[key].append(row)

            self.unique_rows = []
            self.duplicate_keys = [key for key, rows in self.seen_values.items() if len(rows) > 1]
            self.duplicate_index = 0

            self.show_duplicates_ui()

        def show_duplicates_ui(self):
            if self.duplicate_index >= len(self.duplicate_keys):
                self.write_output(self.unique_rows)
                messagebox.showinfo("Success", f"Interactive processing completed. Output saved to {self.output_file}.")
                return

            key = self.duplicate_keys[self.duplicate_index]
            duplicates = self.seen_values[key]

            top = Toplevel(self.root)
            top.title("Resolve Duplicates")

            Label(top, text=f"Duplicates for key: {key}").pack(pady=10)

            canvas = Canvas(top)
            frame = Frame(canvas)
            scrollbar = Scrollbar(top, orient="vertical", command=canvas.yview)

            canvas.configure(yscrollcommand=scrollbar.set)

            scrollbar.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)

            canvas.create_window((0, 0), window=frame, anchor="nw")

            for duplicate in duplicates:
                row_frame = Frame(frame)
                row_frame.pack(fill="x", padx=5, pady=2)
                for col in self.fieldnames:
                    Label(row_frame, text=duplicate[col], relief="groove", width=15).pack(side="left", padx=1)

            frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

            Button(top, text="Delete Selected", command=lambda: self.delete_selected(top)).pack(side="left", padx=5, pady=10)
            Button(top, text="Merge Selected", command=lambda: self.merge_selected(top)).pack(side="left", padx=5, pady=10)
            Button(top, text="Next", command=lambda: self.skip_duplicates(top)).pack(side="right", padx=5, pady=10)

        def delete_selected(self, window):
            selected_indices = [int(item) for item in self.duplicate_list.curselection()]
            duplicates = self.seen_values[self.duplicate_keys[self.duplicate_index]]

            for index in sorted(selected_indices, reverse=True):
                duplicates.pop(index)

            if len(duplicates) == 1:
                self.unique_rows.append(duplicates[0])

            self.duplicate_index += 1
            window.destroy()
            self.show_duplicates_ui()

        def merge_selected(self, window):
            selected_indices = [int(item) for item in self.duplicate_list.curselection()]
            duplicates = self.seen_values[self.duplicate_keys[self.duplicate_index]]

            merged_row = {col: "" for col in self.fieldnames}
            for index in selected_indices:
                for col in self.fieldnames:
                    merged_row[col] += duplicates[index][col] + " | " if duplicates[index][col] else ""

            merged_row = {col: val.strip(" | ") for col, val in merged_row.items()}
            self.unique_rows.append(merged_row)

            self.duplicate_index += 1
            window.destroy()
            self.show_duplicates_ui()

        def skip_duplicates(self, window):
            self.duplicate_index += 1
            window.destroy()
            self.show_duplicates_ui()

        def write_output(self, rows):
            with open(self.output_file, "w", newline="", encoding="utf-8") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(rows)

    root = Tk()
    app = DuplicatePasswordApp(root)
    root.mainloop()

# Example usage
remove_duplicate_passwords()
