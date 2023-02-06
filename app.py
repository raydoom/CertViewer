#!/usr/bin/python3

import tkinter
from tkinter import ttk
from tkinter.filedialog import *
from utils import cert_parser, crl_parser

#issue = crl_parser.get_crl_info()

def selectFile():
    file_path = askopenfilename()  # 选择打开什么文件，返回文件名
    print(file_path)
    return file_path

def file_load(tree,label_xiangqing,label_title):
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    file_path = selectFile()
    cn,base_info_jl,base_info_xq = cert_parser.get_cert_info(file_path)
    label_title.configure(text=cn)
    tree.insert("", 0, values=('Subject', base_info_jl['subject_info']))
    tree.insert("", 0, values=('signature_algorithm', base_info_jl['signature_algorithm']))
    label_xiangqing.configure(text=base_info_xq['subject_info'])
    print("f1")

file_path = "/Users/maxd/Downloads/1.pem"

app = tkinter.Tk()
app.title("CertViewer")
cn,base_info_jl,base_info_xq = cert_parser.get_cert_info(file_path)
tree = ttk.Treeview(master=app, show="headings")
tree["columns"] = ("项目", "值")
tree.column("项目",width=100)
tree.column("值",width=260)
tree.heading("项目", text="项目")
tree.heading("值", text="值")
tree.insert("", 0, values=('Subject',base_info_jl['subject_info']))
tree.insert("", 0, values=('signature_algorithm', base_info_jl['signature_algorithm']))

label_title = tkinter.Label(app, text=cn,padx=10, pady=15)

label_xiangqing = tkinter.Label(app, text=base_info_xq['subject_info'],padx=10, pady=10,bg="white",justify="left")

label_title.grid(padx=20,)
tree.grid(padx=20,)
label_xiangqing.grid(padx=20, sticky="w",pady=20)

open_file_button = tkinter.Button(app, text='打开文件', command=lambda:file_load(tree,label_xiangqing,label_title))
open_file_button.grid(padx=5, pady=5)
# 进入消息循环
app.mainloop()

