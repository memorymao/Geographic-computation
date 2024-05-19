# 
import PySimpleGUI as sg
from all_shps_to_gpkg import extract_shps_to_gpkg

layout = [[sg.Text("Data Folder: "),sg.Input(key='-FOLDER_INPUT-'), sg.FolderBrowse('Choose a Folder')],
          [sg.Text("GeoPackage File:"), sg.Input(key='-FILE_OUTPUT-'), sg.FileSaveAs('Select a File', file_types=(("ALL Files", ".*"),("GeoPackage Files", ".gpkg")))],
          [sg.Button('Save'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    if event == 'Save':
        folderName = values['-FOLDER_INPUT-']
        gpkgFileName = values['-FILE_OUTPUT-']

        extract_shps_to_gpkg(folderName, gpkgFile=gpkgFileName)

# Finish up by removing from the screen
window.close()

