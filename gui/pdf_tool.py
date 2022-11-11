import os
import PySimpleGUI as sg

sg.theme('DarkAmber')

close_window_action = "Ja!"
print("Vilka snälla kollegor jag har")
file_selector_column = [
    [
        sg.Text("File Browser"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[],enable_events=True, size=(40,20), key = "-FILE LIST-"
        )
    ]
]

layout = [
    [file_selector_column],
    [sg.Text("Hej! Ska vi bygga ett grafiskt gränssnitt på SUP:en?")],
    [sg.Button(close_window_action)]
]

# Create the window
window = sg.Window("Demo", layout, margins=(200, 50))

# Event loop
while True:
    event, values = window.read()
#     if event == "-FOLDER-":
#         folder = values["-FOLDER-"]
#         try:
#             file_list = os.listdir(folder)
#         except:
#             file_list = []
#         filenames = [
#             f
#             for f in file_list
#             if os.path.isfile(os.path.join(folder, f))
#             and f.lower().endswith((".pdf"))
#         ]

#     elif event == "-FILE LIST-":
#         try:
#             filename = os.path.join(
#                 values["-FOLDER-"], values["-FILE LIST-"][0]
#             )
#             window["-TOUT-"].update(filename)
#             window["-IMAGE-"].update(filename=filename)

#         except:
#             pass

    if event in (close_window_action, sg.WIN_CLOSED):
        break

window.close()