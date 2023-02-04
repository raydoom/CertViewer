#!/usr/bin/python3

import tkinter
from utils import cert_parser, crl_parser

cert_parser.get_cert_info()
crl_parser.get_crl_info()
top = tkinter.Tk()
# 进入消息循环
top.mainloop()