import PySimpleGUI as sg
sg.theme("Black2") #penentuan tema
sg.theme_text_color("#FFFFFF")
window = sg.Window(title="Profile",
layout=[[sg.Text("FTI UNISKA",font=("Helvetica",24),text_color="#FFFFFF")],[sg.Text("FAKULTAS TEKNOLOGI INFORMASI",font=("Courier",18,"italic","bold","underline"))],
[sg.Text("UNISKA MABBANJARMASIN",text_color="#007FFF")]],
size=(430,200),
font=("Times", 18))
window()
window.close()