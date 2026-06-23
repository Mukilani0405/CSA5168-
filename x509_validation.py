from cryptography import x509
from cryptography.hazmat.backends import default_backend

filename = input("Enter certificate file (.pem): ")

with open(filename, "rb") as file:
    cert = x509.load_pem_x509_certificate(
        file.read(),
        default_backend()
    )

print("\nIssuer:")
print(cert.issuer)

print("\nSubject:")
print(cert.subject)

print("\nValid From:")
print(cert.not_valid_before)

print("\nValid Until:")
print(cert.not_valid_after)

print("\nSerial Number:")
print(cert.serial_number)
