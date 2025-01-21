import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def remove_duplicate_passwords():
    """
    Removes duplicates from a CSV file based on user-selected columns. Offers auto or interactive mode.
    """
    try:
        # Hide the root Tkinter window
        Tk().withdraw()

        # Prompt the user to select the input file
        input_file = askopenfilename(title="Select Input CSV File", filetypes=[("CSV Files", "*.csv")])
        if not input_file:
            print("No file selected. Exiting.")
            return

        # Prompt the user to select the output file
        output_file = asksaveasfilename(title="Save Output CSV File As", defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not output_file:
            print("No output file selected. Exiting.")
            return

        # Read the input CSV file
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            rows = list(reader)

        if not reader.fieldnames:
            raise ValueError("The input CSV has no columns.")

        # Prompt the user to select columns to match
        print("Available columns:")
        for i, column in enumerate(reader.fieldnames):
            print(f"{i + 1}. {column}")

        selected_columns = input("Enter the numbers of the columns to match against, separated by commas: ").split(',')
        try:
            match_columns = [reader.fieldnames[int(i.strip()) - 1] for i in selected_columns if i.strip().isdigit() and 0 < int(i.strip()) <= len(reader.fieldnames)]
        except (IndexError, ValueError):
            print("Invalid column selection. Exiting.")
            return

        if not match_columns:
            print("No valid columns selected. Exiting.")
            return

        print(f"Matching on columns: {', '.join(match_columns)}")

        # Ask the user if they want auto or interactive mode
        mode = input("Select mode: 'auto' to automatically remove duplicates or 'interactive' to review duplicates manually: ").strip().lower()

        if mode == 'auto':
            # Auto mode: Remove duplicates based on the selected columns
            seen_values = set()
            unique_rows = []

            for row in rows:
                key = tuple(row[column] for column in match_columns)
                if key not in seen_values:
                    seen_values.add(key)
                    unique_rows.append(row)

            # Write the unique rows to the output CSV file
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(unique_rows)

            print(f"Duplicates removed successfully. Output saved to {output_file}.")

        elif mode == 'interactive':
            # Interactive mode: Review and handle duplicates manually
            seen_values = {}
            for row in rows:
                key = tuple(row[column] for column in match_columns)
                if key not in seen_values:
                    seen_values[key] = [row]
                else:
                    seen_values[key].append(row)

            unique_rows = []
            for key, duplicates in seen_values.items():
                if len(duplicates) == 1:
                    unique_rows.append(duplicates[0])
                else:
                    print(f"Duplicate entries found for key: {key}")
                    for i, duplicate in enumerate(duplicates):
                        print(f"{i + 1}: {duplicate}")

                    action = input("Enter the number of the entry to keep, 'm' to merge, or 'i' to ignore these entries: ").strip().lower()
                    if action.isdigit() and 1 <= int(action) <= len(duplicates):
                        unique_rows.append(duplicates[int(action) - 1])
                    elif action == 'm':
                        merged_entry = {column: "" for column in reader.fieldnames}
                        for duplicate in duplicates:
                            for column in reader.fieldnames:
                                merged_entry[column] += duplicate[column] + " | " if duplicate[column] else ""
                        unique_rows.append({column: value.strip(' | ') for column, value in merged_entry.items()})
                    elif action == 'i':
                        print("Ignored these entries.")

            # Write the unique rows to the output CSV file
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(unique_rows)

            print(f"Interactive deduplication completed. Output saved to {output_file}.")

        else:
            print("Invalid mode selected. Exiting.")

    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
remove_duplicate_passwords()
