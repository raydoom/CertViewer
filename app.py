#!/usr/bin/python3

import tkinter
from tkinter import ttk
from tkinter.filedialog import *

from utils import cert_parser, crl_parser

file_path = "/Users/maxd/Downloads/1.pem"

# issue = crl_parser.get_crl_info()
cn, base_info = cert_parser.get_cert_info(file_path)

root = tkinter.Tk()
root.title("CertViewer")
root.geometry('450x600')
root.resizable(0, 0)

app = tkinter.Canvas(root)
label_title = tkinter.Label(app, text=cn, padx=10, pady=15,font=("",18,"bold"))

img = tkinter.PhotoImage('resources/1.png')
label_img = tkinter.Label(app,image=img)

label_br = tkinter.Label(app, text='---------------------------------------------------------------', padx=10, pady=15)

label_img.grid(column=0, row=0)
label_title.grid(padx=20, )
label_br.grid()

print(base_info)
for k in base_info:
    label_k = tkinter.Label(app, text=k, padx=5, pady=5,justify='left', anchor='nw')
    label_v = tkinter.Label(app, text=base_info[k], padx=25, pady=0,justify='left',anchor='nw')
    label_k.grid(sticky="w",)
    label_v.grid(sticky="w",)
# 打开文件
# open_file_button = tkinter.Button(app, text='打开文件', command=lambda: file_load(cert_info, label_title))
# open_file_button.grid(padx=5, pady=5)

scroll_bar = tkinter.Scrollbar(app,)
scroll_bar.grid(sticky="w")
scroll_bar.config(command=app.yview)
app.pack(side="left")

# 进入消息循环
root.mainloop()
