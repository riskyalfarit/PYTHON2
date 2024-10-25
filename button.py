import PySimpleGUI as sg
sg.theme("DarkTeal") 
sg.theme_text_color("#F0FFFF")
window =sg.Window(title="Contoh Button",
		layout=[[sg.Text("Are u okey?")],
		[sg.Button("YA")],
		[sg.Button("TIDAK")]
		],
			size=(400,200),
			font=("Times", 18))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()