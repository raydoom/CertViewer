import OpenSSL

def get_cert_info():
    with open("/Users/maxd/Downloads/1.pem", "r") as f:
        crt_data = f.read()

    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, crt_data)
    certIssue = cert.get_issuer()
    print(certIssue.commonName)
    print(cert.get_signature_algorithm().decode("UTF-8"))
    # 输出吊销列表里面的证书序列号s
    #for rvk in revoked_objects:
    #    print("Serial:", rvk.get_serial())