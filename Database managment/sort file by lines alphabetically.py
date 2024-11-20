import PySimpleGUI as sg
import os
import time

def estimate_processing_time(file_size):
    # Estimate processing time based on file size
    # This is a placeholder function - adjust based on your actual processing speed
    return file_size / 1000000  # Assuming 1 MB per second processing speed

def process_file(input_file, output_file, window):
    file_size = os.path.getsize(input_file)
    estimated_time = estimate_processing_time(file_size)
    
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    total_lines = len(lines)
    sorted_lines = sorted(lines)
    
    with open(output_file, 'w') as outfile:
        for i, line in enumerate(sorted_lines):
            outfile.write(line)
            if estimated_time > 1:  # Update progress bar for longer operations
                progress = int((i + 1) / total_lines * 100)
                window['-PROG-'].update(progress)
                window.refresh()

sg.theme('DarkBlue3')

layout = [
    [sg.Text('Select a file to sort:')],
    [sg.Input(key='-FILE-'), sg.FileBrowse()],
    [sg.Button('Sort'), sg.Button('Exit')],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROG-', visible=False)]
]

window = sg.Window('File Line Sorter', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Sort':
        input_file = values['-FILE-']
        if not input_file:
            sg.popup_error('Please select a file to sort.')
            continue

        # Choose save location
        output_file = sg.popup_get_file('Save sorted file as:', save_as=True, file_types=(("Text Files", "*.txt"),))
        if not output_file:
            continue

        # Show progress bar
        window['-PROG-'].update(visible=True)
        
        # Process the file
        process_file(input_file, output_file, window)

        # Hide progress bar and show completion message
        window['-PROG-'].update(visible=False)
        sg.popup(f'Sorting complete!\nOutput saved to: {output_file}')

window.close()