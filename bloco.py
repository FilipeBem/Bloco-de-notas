import PySimpleGUI as sg

# Define the layout
def create_layout():
    layout = [
        [sg.Text('Enter text:')],
        [sg.Multiline(size=(80, 20), key='-INPUT-')],
        [sg.Button('Save'), sg.Button('Open'), sg.Button('Fullscreen'), sg.Button('Exit')]
    ]
    return layout

def create_fullscreen_layout():
    layout = [
        [sg.Text('Enter text:')],
        [sg.Multiline(size=(190, 38), key='-INPUT-')],
        [sg.Button('Save'), sg.Button('Open'), sg.Button('Minimize'), sg.Button('Exit')]
    ]
    return layout

# Create the window
def create_window(layout):
    window = sg.Window('Notepad', layout, finalize=True)
    return window

# Create the initial window
window = create_window(create_layout())

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Save':
        text = values['-INPUT-']
        filename = sg.popup_get_file('Browse', save_as=True, default_extension='.txt', initial_folder='.')
        if filename:
            with open(filename, 'w') as f:
                f.write(text)
    if event == 'Open':
        filename = sg.popup_get_file('Open', default_extension='.txt', initial_folder='.')
        if filename:
            with open(filename, 'r') as f:
                text = f.read()
                window['-INPUT-'].update(text)
    if event == 'Fullscreen':
        window.hide()
        window = create_window(create_fullscreen_layout())
        window.Maximize()
    if event == 'Minimize':
        window.hide()
        window = create_window(create_layout())

window.close()