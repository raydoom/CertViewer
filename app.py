#!/usr/bin/python3

import tkinter
import OpenSSL

import OpenSSL

with open(r"/Users/maxd/Downloads/1.crl", 'rb') as _crl_file:
    crl = _crl_file.read()

# 注意crl文件的编码格式，如果是pem的用FILETYPE_PEM,der的用FILETYPE_ASN1
# crl_object = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_PEM, crl)
crl_object = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, crl)

revoked_objects = crl_object.get_issuer()
#print(revoked_objects)

with open("/Users/maxd/Downloads/1.pem", "r") as fp:
    crt_data = fp.read()

cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, crt_data)
certIssue = cert.get_issuer()
#print(certIssue.commonName)
#print(cert.get_signature_algorithm().decode("UTF-8"))
# 输出吊销列表里面的证书序列号s
#for rvk in revoked_objects:
#    print("Serial:", rvk.get_serial())

top = tkinter.Tk()
# 进入消息循环
top.mainloop()