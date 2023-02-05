import OpenSSL

def get_crl_info():
    with open(r"/Users/maxd/Downloads/1.crl", 'rb') as f:
        crl = f.read()

    # 注意crl文件的编码格式，如果是pem的用FILETYPE_PEM,der的用FILETYPE_ASN1
    # crl_object = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_PEM, crl)
    crl_object = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, crl)

    revoked_objects = crl_object.get_issuer()
    print(revoked_objects)
    return revoked_objects