#!/usr/bin/python3

import tkinter
from tkinter import ttk
from tkinter.filedialog import *

from utils import cert_parser, crl_parser


# issue = crl_parser.get_crl_info()

def selectFile():
    file_path = askopenfilename()  # 选择打开什么文件，返回文件名
    print(file_path)
    return file_path


def file_load(tree, label_xiangqing, label_title):
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    file_path = selectFile()
    global cn, base_info_jl, base_info_xq
    cn, base_info_jl, base_info_xq = cert_parser.get_cert_info(file_path)
    label_title.configure(text=cn)
    for v in base_info_jl:
        tree.insert("", 0, values=(v, base_info_jl[v]))
    label_xiangqing.configure(text=base_info_xq['subject'])
    return 0


def select_tree(event, label_xiangqing):
    for item in tree.selection():
        item_text = tree.item(item, "values")
        label_xiangqing.configure(text=base_info_xq[item_text[0]])
        print(label_xiangqing)


def select_adapt(fun, **kwds):
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


# file_path = "/Users/maxd/Downloads/1.pem"

app = tkinter.Tk()
app.title("CertViewer")
app.geometry('450x600')
app.resizable(0, 0)
tree = ttk.Treeview(master=app, show="headings", height=12)
tree["columns"] = ("字段", "值")
tree.column("字段", width=150)
tree.column("值", width=260)
tree.heading("字段", text="字段")
tree.heading("值", text="值")

label_title = tkinter.Label(app, text='', padx=10, pady=15)
label_xiangqing = tkinter.Label(app, text='', padx=10, pady=10, width=43, height=10, bg="white", justify="left",
                                anchor='nw', wraplength='400')

label_title.grid(padx=20, )
tree.grid(padx=20, )
label_xiangqing.grid(padx=20, sticky="w", pady=20)

open_file_button = tkinter.Button(app, text='打开文件', command=lambda: file_load(tree, label_xiangqing, label_title))
open_file_button.grid(padx=5, pady=5)
tree.bind('<<TreeviewSelect>>', select_adapt(select_tree, label_xiangqing=label_xiangqing))

# 进入消息循环
app.mainloop()
