import hashlib
import time

data = input("Enter the text: ")

# MD5
start = time.time()
md5_hash = hashlib.md5(data.encode()).hexdigest()
md5_time = time.time() - start

# SHA-256
start = time.time()
sha256_hash = hashlib.sha256(data.encode()).hexdigest()
sha256_time = time.time() - start

print("\nMD5 Hash      :", md5_hash)
print("SHA-256 Hash  :", sha256_hash)

print("\nMD5 Time      :", md5_time)
print("SHA-256 Time  :", sha256_time)
