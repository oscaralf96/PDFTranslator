import PySimpleGUI as sg

# sg.Window(title="hello World", layout=[[]], margins=(100, 50)).read()

import PySimpleGUI as sg
import os.path

# my functions
from .pdf_translator import pdf_translator
def main():
    file_list_column = [
        [
            sg.Text("PDF File"),
            sg.In(size=(25, 1), enable_events=True, key="-PDF-"),
            sg.FileBrowse(),
        ],
        [
            sg.Text("Storage Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-STORAGE-"),
            sg.FolderBrowse(),
        ]
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(file_list_column),
        ],
        [
            sg.Button("Translate", key="-TRANSLATE-"),
        ]
    ]

    window = sg.Window("PDF Translator", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == "-PDF-":
            file = values["-PDF-"]
            print(file)
        elif event == "-STORAGE-":
            folder = values["-STORAGE-"]
            print(folder)
        elif event == "-TRANSLATE-":
            pdf_translator(file, folder)

    window.close()


if __name__ == "__main__":
    main()