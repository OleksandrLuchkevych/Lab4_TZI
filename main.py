from PolybiusCipher import *
from HTMLGenerator import *

cipher = PolybiusCipher()
html_gen_encr = HTMLGenerator("Encrypted message")
html_gen_decr = HTMLGenerator("Decrypted message")

with open("message.txt", "r", encoding="utf-8") as file:
    message = file.read().strip()

encrypted_message = cipher.encrypt(message)
print("Зашифрований текст:", encrypted_message)

decrypted_message = cipher.decrypt(message)
print("Розшифрований текст:", decrypted_message)

html_gen_encr.save_html(encrypted_message, "Encrypted message.html")
html_gen_decr.save_html(decrypted_message, "Decrypted message.html")