"""
Passo 2: Analisa e relata as tags mais comuns
"""
import json
import os
from collections import Counter

INPUT_PATH = os.path.join('data', 'processed', 'clean_posts.json')
REPORT_PATH = os.path.join('data', 'analysis', 'tags_report.json')

def analyze_tags():
    # Carregar posts processados
    with open(INPUT_PATH, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    # Contar tags
    tag_counter = Counter()
    for post in posts:
        tags = post.get("tags", "").lower().split()
        tag_counter.update(tags)
    
    # Gerar relatório
    report = {
        "total_posts": len(posts),
        "total_tags": sum(tag_counter.values()),
        "unique_tags": len(tag_counter),
        "top_10_tags": tag_counter.most_common(10),
        "all_tags": dict(tag_counter)
    }
    
    # Salvar relatório
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=4)
    
    # Exibir resumo
    print("📊 Relatório de Tags:")
    print(f"- Total de Posts: {len(posts)}")
    print(f"- Tags Únicas: {len(tag_counter)}")
    print("\n🔝 Top 10 Tags:")
    for tag, count in report["top_10_tags"]:
        print(f"  {tag}: {count} posts")

if __name__ == "__main__":
    analyze_tags()