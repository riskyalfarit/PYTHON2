import PySimpleGUI as sg
sg.theme("Black2") #penentuan tema
sg.theme_text_color("#FFFFFF")
window = sg.Window(title="Profile",
layout=[[sg.Text("TEKNOLOGI INFORMASI ",size=(25,1), justification="center")],
[sg.Text("TEKNOLOGI INFORMASI ",size=(25,1), justification="left")],
 [sg.Text("TEKNOLOGI INFORMASI ",size=(25,1), justification="right")],
[sg.Text(("TEKNOLOGI INFORMASI "+" ")* 2,size=(25,2), justification="center")],
 [sg.Text("UNISKA MAB BANJARMASIN", text_color="#007FFF")]],
size=(400,250),
font=("Times", 18))
window()
window.close()