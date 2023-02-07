import OpenSSL
import time
from dateutil import parser

def get_cert_info(file_path):
    base_info = {}

    base_info = {}
    extension_info = {}


    with open("/Users/maxd/Downloads/1.pem", "r") as f:
    # with open(file_path, "r") as f:
        cert_data = f.read()

    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_data)
    cn = cert.get_subject().CN

    # 主题
    subject_list = list(cert.get_subject().get_components())
    subject_len = len(subject_list)
    print(subject_len)
    subject_info_list = []
    subject_info = ""
    i = 0
    for i in range(0, subject_len):
        subject_info_list.append(cert.get_subject().get_components()[i][0].decode("UTF-8")+'  ' \
            +cert.get_subject().get_components()[i][1].decode("UTF-8"))
        subject_info = subject_info + subject_info_list[i]+ "\n"
        i = i + 1
    # 控制label宽度
    subject_info = subject_info + \
    "                                                                                              "
    print(subject_info)
    base_info['subject'] = subject_info

    # 颁发者
    issuer_list = list(cert.get_issuer().get_components())
    issuer_len = len(issuer_list)
    print(issuer_len)
    issuer_info_list = []
    issuer_info = ""
    i = 0
    for i in range(0, issuer_len):
        issuer_info_list.append(cert.get_issuer().get_components()[i][0].decode("UTF-8")+'  ' \
            +cert.get_issuer().get_components()[i][1].decode("UTF-8"))
        issuer_info = issuer_info + issuer_info_list[i]+ "\n"
        i = i + 1
    # 控制label宽度
    issuer_info = issuer_info + \
    "                                                                                              "
    print(subject_info)
    base_info['issuer'] = issuer_info

    # 算法
    signature_algorithm = cert.get_signature_algorithm().decode("UTF-8")
    base_info['signature_algorithm'] = signature_algorithm

    # 版本version
    version = cert.get_version() + 1
    base_info['version'] = version

    # 序列号
    serial_number= hex(cert.get_serial_number())
    base_info['serial_number'] = serial_number

    #
    print(cert.get_issuer())

    # 有效期结束
    not_after = parser.parse(cert.get_notAfter().decode("UTF-8")).strftime('%Y-%m-%d %H:%M:%S')
    base_info['not_after'] = not_after

    # 有效期开始
    not_before = parser.parse(cert.get_notBefore().decode("UTF-8")).strftime('%Y-%m-%d %H:%M:%S')
    base_info['not_before'] = not_before

    # 公钥
    print(cert.get_pubkey().bits())
    print(OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, cert.get_pubkey()).decode("utf-8"))
    pubkey_jl = cert.get_pubkey().bits()
    pubkey_xq = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, cert.get_pubkey()).decode("utf-8")
    base_info['pubkey'] = pubkey_jl

    # 扩展
    print(cert.get_extension_count())
    print(cert.get_extension(2).get_data())
    for i in range(0, cert.get_extension_count()):
        print(cert.get_extension(i).__str__())
        print(cert.get_extension(i).get_short_name())
        print(cert.get_extension(i))

    return cn,base_info