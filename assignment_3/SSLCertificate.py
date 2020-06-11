from OpenSSL import crypto, SSL
import SSLCertificate

def write_to_file(data, filename):
    f = open(filename,"wb")
    f.write(data)
    f.close()

def create_public_key_pair(key_file):
    data = open(key_file, "wb")
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)
    data.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    data.close()
    return k


def create_self_signed_cert(cert_file, key):
    data = open(cert_file, "wb")
    cert = crypto.X509()
    cert.set_serial_number(1001)
    cert.set_notBefore(b"20190101000000Z")
    cert.set_notAfter(b"20290101000000Z")

    subject = cert.get_subject()
    subject.C = "NO" # Country
    subject.ST = "Aust-Agder" # State/county
    subject.L = "Grimstad" # Location/city
    subject.O = "UiA" # Organization
    subject.OU = "IKT" # Organizational unit
    subject.CN = "localhost" # Common name
    cert.set_issuer(subject)

    cert.set_pubkey(key)
    cert.sign(key, "SHA256")

    data.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    data.close()
    return cert # You need to return the created cert

if __name__ == '__main__':
    SSLCertificate.create_self_signed_cert('example.crt', create_public_key_pair('example.key'))
