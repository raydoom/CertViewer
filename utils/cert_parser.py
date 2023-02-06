import OpenSSL

def get_cert_info(file_path):
    base_info_jl = {}
    base_info_xq = {}
    subject_info_list = []
    base_info = {}
    extension_info = {}
    subject_info_jl = ""
    subject_info_xq = ""
    # with open("/Users/maxd/Downloads/1.pem", "r") as f:
    with open(file_path, "r") as f:
        cert_data = f.read()

    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_data)
    certIssue = cert.get_issuer()
    print(certIssue.commonName)
    print(cert.get_signature_algorithm().decode("UTF-8"))

    print(cert.get_extension(1))

    base_info['cn'] = cert.get_subject().CN
    base_info['o'] = cert.get_subject().O
    subject_list = list(cert.get_subject().get_components())
    subject_len = len(subject_list)
    print(subject_len)
    cn = cert.get_subject().CN
    i = 0
    for i in range(0, subject_len):
        print (cert.get_subject().get_components()[i][0].decode("UTF-8"),
               cert.get_subject().get_components()[i][1].decode("UTF-8"))

        subject_info_list.append(cert.get_subject().get_components()[i][0].decode("UTF-8")+' = ' \
            +cert.get_subject().get_components()[i][1].decode("UTF-8"))
        subject_info_jl = subject_info_jl + subject_info_list[i]+ ", "
        subject_info_xq = subject_info_xq + subject_info_list[i]+ "\n"
        i = i + 1
    # 控制label宽度
    subject_info_xq = subject_info_xq + \
    "                                                                                              "
    print(subject_info_jl)
    base_info_jl['subject_info'] = subject_info_jl
    base_info_xq['subject_info'] = subject_info_xq
    # 算法
    signature_algorithm = cert.get_signature_algorithm().decode("UTF-8")
    print(signature_algorithm)
    signature_algorithm_jl = signature_algorithm
    signature_algorithm_xq = signature_algorithm

    base_info_jl['signature_algorithm'] = signature_algorithm_jl
    base_info_xq['signature_algorithm'] = signature_algorithm_xq

    return cn,base_info_jl,base_info_xq