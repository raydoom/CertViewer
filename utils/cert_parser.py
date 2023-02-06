import OpenSSL
import time
from dateutil import parser

def get_cert_info(file_path):
    base_info_jl = {}
    base_info_xq = {}

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
    subject_info_jl = ""
    subject_info_xq = ""
    i = 0
    for i in range(0, subject_len):
        subject_info_list.append(cert.get_subject().get_components()[i][0].decode("UTF-8")+' = ' \
            +cert.get_subject().get_components()[i][1].decode("UTF-8"))
        subject_info_jl = subject_info_jl + subject_info_list[i]+ ", "
        subject_info_xq = subject_info_xq + subject_info_list[i]+ "\n"
        i = i + 1
    # 控制label宽度
    subject_info_xq = subject_info_xq + \
    "                                                                                              "
    print(subject_info_jl)
    base_info_jl['subject'] = subject_info_jl
    base_info_xq['subject'] = subject_info_xq

    # 颁发者
    issuer_list = list(cert.get_issuer().get_components())
    issuer_len = len(issuer_list)
    print(issuer_len)
    issuer_info_list = []
    issuer_info_jl = ""
    issuer_info_xq = ""
    i = 0
    for i in range(0, issuer_len):
        issuer_info_list.append(cert.get_issuer().get_components()[i][0].decode("UTF-8")+' = ' \
            +cert.get_issuer().get_components()[i][1].decode("UTF-8"))
        issuer_info_jl = issuer_info_jl + issuer_info_list[i]+ ", "
        issuer_info_xq = issuer_info_xq + issuer_info_list[i]+ "\n"
        i = i + 1
    # 控制label宽度
    issuer_info_xq = issuer_info_xq + \
    "                                                                                              "
    print(subject_info_jl)
    base_info_jl['issuer'] = issuer_info_jl
    base_info_xq['issuer'] = issuer_info_xq

    # 算法
    signature_algorithm = cert.get_signature_algorithm().decode("UTF-8")
    base_info_jl['signature_algorithm'] = signature_algorithm
    base_info_xq['signature_algorithm'] = signature_algorithm

    # 版本version
    version = cert.get_version()+1
    base_info_jl['version'] = version
    base_info_xq['version'] = version

    # 序列号
    serial_number= hex(cert.get_serial_number())
    base_info_jl['serial_number'] = serial_number
    base_info_xq['serial_number'] = serial_number

    #
    print(cert.get_issuer())

    # 有效期结束
    not_after = parser.parse(cert.get_notAfter().decode("UTF-8")).strftime('%Y-%m-%d %H:%M:%S')
    base_info_jl['not_after'] = not_after
    base_info_xq['not_after'] = not_after

    # 有效期开始
    not_before = parser.parse(cert.get_notBefore().decode("UTF-8")).strftime('%Y-%m-%d %H:%M:%S')
    base_info_jl['not_before'] = not_before
    base_info_xq['not_before'] = not_before

    # 公钥
    print(cert.get_pubkey().bits())
    print(OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, cert.get_pubkey()).decode("utf-8"))
    pubkey_jl = cert.get_pubkey().bits()
    pubkey_xq = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, cert.get_pubkey()).decode("utf-8")
    base_info_jl['pubkey'] = pubkey_jl
    base_info_xq['pubkey'] = pubkey_xq

    # 扩展
    print(cert.get_extension_count())
    print(cert.get_extension(2).get_data())
    for i in range(0, cert.get_extension_count()):
        print(cert.get_extension(i).__str__())
        print(cert.get_extension(i).get_short_name())
        print(cert.get_extension(i))

    return cn,base_info_jl,base_info_xq