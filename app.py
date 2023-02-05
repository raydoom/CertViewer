#!/usr/bin/python3

import tkinter
from tkinter import ttk
from tkinter.filedialog import *
from utils import cert_parser, crl_parser



#issue = crl_parser.get_crl_info()

def selectFile(a1):
    global img
    file_path = askopenfilename()  # 选择打开什么文件，返回文件名
    print(file_path)
    a1.update()
    return file_path

subject_info,subject_info_xq= cert_parser.get_cert_info(file_path)

app = tkinter.Tk()
app.title("CertViewer")
subject_info, subject_info_xq = cert_parser.get_cert_info(file_path)
tree = ttk.Treeview(master=app, show="headings")
tree["columns"] = ("项目", "值")
tree.column("项目",width=100)
tree.column("值",width=260)
tree.heading("项目", text="项目")
tree.heading("值", text="值")
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))
tree.insert("", 0, values=('Subject',subject_info))


label_title = tkinter.Label(app, text='subje',padx=10, pady=15)

label_xiangqing = tkinter.Label(app, text=subject_info_xq,padx=10, pady=10,bg="white",justify="left")

open_file_button = tkinter.Button(app, text='打开文件', command=selectFile(app))

label_title.grid(padx=20,)
tree.grid(padx=20,)
label_xiangqing.grid(padx=20, sticky="w",pady=20)
open_file_button.grid(padx=5, pady=5)
# 进入消息循环
app.mainloop()

