"""
Passo 1: Transforma o JSON bruto do Easy Scraper em estrutura limpa com tags
"""
import json
import os
from collections import defaultdict

# Configurações de pastas
RAW_PATH = os.path.join('data', 'raw', 'raw.json')
PROCESSED_PATH = os.path.join('data', 'processed', 'clean_posts.json')

def transform_raw_json():
    # Carregar dados brutos
    with open(RAW_PATH, 'r', encoding='utf-8') as f:
        raw_posts = json.load(f)

    # Processar cada post
    clean_posts = []
    for idx, post in enumerate(raw_posts):
        try:
            container = post.get("container", "")
            link = post.get("texts href", "")
            
            # Extrair título, data e conteúdo
            lines = container.split('\n')
            title = lines[0].strip() if len(lines) > 0 else f"Post Sem Título {idx}"
            date = lines[1].strip() if len(lines) > 1 else "Data Desconhecida"
            content = '\n'.join(lines[3:]).strip() if len(lines) > 3 else container
            
            # Extrair tags
            tags = ""
            if "tags: " in container:
                content, _, tags_part = container.rpartition("tags: ")
                tags = tags_part.strip()
                content = content.strip()

            clean_posts.append({
                "titulo": title,
                "data": date,
                "conteudo": content,
                "tags": tags,
                "link": link
            })
            
        except Exception as e:
            print(f"Erro no post {idx}: {str(e)}")
            continue

    # Salvar JSON processado
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    with open(PROCESSED_PATH, 'w', encoding='utf-8') as f:
        json.dump(clean_posts, f, ensure_ascii=False, indent=4)
    
    print(f"✅ {len(clean_posts)} posts processados e salvos em {PROCESSED_PATH}")

if __name__ == "__main__":
    transform_raw_json()