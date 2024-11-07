import string

class PolybiusCipher:
    def __init__(self):
        self.size = 5
        self.alphabet = string.ascii_lowercase.replace("j", "")
        self.grid = self._create_grid()

    def _create_grid(self):
        grid = {}
        index = 0
        for row in range(1, self.size + 1):
            for col in range(1, self.size + 1):
                grid[self.alphabet[index]] = (row, col)
                index += 1
        return grid

    def encrypt(self, text):
        text = text.lower().replace("j", "i")
        encrypted = ""
        for char in text:
            if char in self.grid:
                row, col = self.grid[char]
                encrypted += f"{row}{col}"
            else:
                encrypted += char  # зберігаємо пробіли та розділові знаки
        return encrypted

    def decrypt(self, encrypted_text):
        decrypted = ""
        i = 0
        while i < len(encrypted_text):
            if encrypted_text[i].isdigit() and i + 1 < len(encrypted_text) and encrypted_text[i + 1].isdigit():
                row, col = int(encrypted_text[i]), int(encrypted_text[i + 1])
                for letter, (r, c) in self.grid.items():
                    if r == row and c == col:
                        decrypted += letter
                        break
                i += 2
            else:
                decrypted += encrypted_text[i]
                i += 1
        return decrypted

class HTMLGenerator:
    def __init__(self, title="Polybius Cipher Result"):
        self.title = title

    def generate_html(self, content):
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
</head>
<body>
    <h1>{self.title}</h1>
    <p>{content}</p>
</body>
</html>"""
        return html_template

    def save_html(self, content, filename="polybius_result.html"):
        html_content = self.generate_html(content)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML файл збережено як {filename}")

cipher = PolybiusCipher()
html_gen = HTMLGenerator("Polybius Cipher Example")

text_to_encrypt = "hello world"
encrypted_text = cipher.encrypt(text_to_encrypt)
print("Зашифрований текст:", encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
print("Розшифрований текст:", decrypted_text)

html_gen.save_html(encrypted_text)
