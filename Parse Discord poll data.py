import json
import tkinter as tk
from tkinter import filedialog

def extract_polls(json_file):
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)
    
    polls = []
    for message in data['messages']:
        if message.get('type') == '46':
            polls.append({
                'question': message.get('question', {}).get('text', 'Unknown'),
                'answers': [a.get('text', 'Unknown') for a in message.get('answers', [])],
                'timestamp': message.get('timestamp', 'Unknown')
            })
    return polls

# Open file explorer to select JSON file
root = tk.Tk()
root.withdraw()  # Hide the root window
file_path = filedialog.askopenfilename(
    title="Select JSON file",
    filetypes=[("JSON files", "*.json")]
)

if file_path:
    polls = extract_polls(file_path)
    with open('polls_output.json', 'w') as f:
        json.dump(polls, f, indent=2)
    print(f"Polls extracted and saved to polls_output.json")
else:
    print("No file selected.")