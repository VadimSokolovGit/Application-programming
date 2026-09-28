import os
import re

base_path = os.path.join(os.path.dirname(__file__), 'base.txt')

with open(base_path, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'(?:SKU|артикул)\s*:?\s*([A-Z0-9]+(?:-[A-Z0-9]+)+)' #шаблон регулярки для поиска SKU и артикулов

articles = re.findall(pattern, text)

print(articles)
