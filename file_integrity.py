import hashlib

def file_hash(filename):
    sha = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            sha.update(data)

    return sha.hexdigest()

file1 = input("Enter file name: ")

print("SHA-256 Hash:", file_hash(file1))
