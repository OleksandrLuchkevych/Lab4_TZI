class HTMLGenerator:
    def __init__(self, title):
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

    def save_html(self, content, filename):
        html_content = self.generate_html(content)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML файл збережено як {filename}")