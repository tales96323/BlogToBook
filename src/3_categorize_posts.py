"""
Passo 3: Categoriza posts com base em tags pré-definidas
"""
from collections import defaultdict
import json
import os
from itertools import combinations

INPUT_PATH = os.path.join('data', 'processed', 'clean_posts.json')
CATEGORIES_PATH = os.path.join('data', 'processed', 'categorized')

# Categorias e tags relacionadas (personalize conforme necessário)
CATEGORIES = {
    "akitando": {"akitando", "pessoal"},
    "learning_principles": {"aprendizado", "princípios", "mental-models"},
    "career": {"carreira", "produtividade"},
    "management": {"gestão", "liderança"},
    "philosophy": {"filosofia", "reflexão"},
    "science": {"ciência", "tecnologia"},
    "startups": {"startups", "empreendedorismo"}
}

def categorize_posts():
    # Carregar posts
    with open(INPUT_PATH, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    # Inicializar estrutura
    categorized = {cat: [] for cat in CATEGORIES}
    categorized["uncategorized"] = []
    intersections = defaultdict(int)

    # Classificar posts
    for post in posts:
        post_tags = set(post.get("tags", "").lower().split())
        matched_cats = []
        
        for cat, tags in CATEGORIES.items():
            if post_tags & tags:
                matched_cats.append(cat)
        
        if not matched_cats:
            categorized["uncategorized"].append(post)
        else:
            for cat in matched_cats:
                categorized[cat].append(post)
            
            # Registrar interseções
            for pair in combinations(matched_cats, 2):
                intersections[f"{pair[0]}-{pair[1]}"] += 1

    # Salvar por categoria
    os.makedirs(CATEGORIES_PATH, exist_ok=True)
    for cat, posts in categorized.items():
        with open(os.path.join(CATEGORIES_PATH, f'{cat}.json'), 'w', encoding='utf-8') as f:
            json.dump(posts, f, ensure_ascii=False, indent=4)
    
    print(f"📂 Posts categorizados salvos em {CATEGORIES_PATH}")
    print("\n🔗 Interseções mais comuns:")
    for pair, count in sorted(intersections.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"- {pair}: {count} posts")

if __name__ == "__main__":
    categorize_posts()