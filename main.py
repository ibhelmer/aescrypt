# Import the Fernet class.
from cryptography.fernet import Fernet
# Use Fernet to generate the key file.
key = Fernet.generate_key()
# Store the file to disk
with open('secret.key', 'wb') as new_key_file:
    new_key_file.write(key)
print(key)
msg = "En lille tekst der skal være hemmelig !"
# Encode this as bytes to feed into the algorithm.
msg = msg.encode()
# Instantiate the object with your key.
f = Fernet(key)
# Pass your bytes type message into encrypt.
ciphertext = f.encrypt(msg)
print("Cleantext: ", msg )
print("Ciphertext: ", ciphertext)

#### Send ciphertext
with open('secret.key', 'rb') as my_private_key:
    key = my_private_key.read()
# Instantiate Fernet on the recip system.
f = Fernet(key)
# Decrypt the message.
cleartext = f.decrypt(ciphertext)
# Decode the bytes back into a string.
cleartext = cleartext.decode()
print("Cleartext :", cleartext)

