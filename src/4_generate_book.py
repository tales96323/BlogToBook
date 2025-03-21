"""
Passo 4: Gera o livro final em Markdown com introdução e estrutura completa
"""
import json
import os
from datetime import datetime

INPUT_DIR = os.path.join('data', 'processed', 'categorized')
OUTPUT_PATH = os.path.join('output', 'book', 'livro_compilado.md')

def generate_book():
    # Criar estrutura do livro
    book_content = [
        "# 📖 Livro Compilado do Blog\n",
        f"*Gerado em {datetime.now().strftime('%d/%m/%Y')}*\n",
        "## 🖼️ Capa\n",
        "**Conteúdo compilado automaticamente**\n",
        "### Origem do Projeto\n",
        "Este livro foi criado a partir de posts de blog obtidos via Easy Scraper, "
        "processados e organizados por temas usando scripts em Python.\n",
        "---\n"
    ]

    # Adicionar capítulos
    for category in os.listdir(INPUT_DIR):
        if not category.endswith('.json'):
            continue
            
        cat_name = os.path.splitext(category)[0]
        with open(os.path.join(INPUT_DIR, category), 'r', encoding='utf-8') as f:
            posts = json.load(f)
        
        book_content.append(f"## 🧩 {cat_name.capitalize()}\n")
        book_content.append(f"**{len(posts)} posts**\n\n")
        
        for post in posts:
            book_content.append(f"### {post['titulo']}\n")
            book_content.append(f"**Data**: {post['data']} | **Tags**: {post['tags']}\n")
            book_content.append(f"{post['conteudo']}\n\n---\n")
    
    # Salvar arquivo final
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(book_content))
    
    print(f"📕 Livro gerado em {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_book()