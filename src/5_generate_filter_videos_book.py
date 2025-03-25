import json
import re
import unicodedata

def limpar_prefixo(titulo):
    """Remove o padrão [Akitando] #... - do início do título"""
    return re.sub(r'^\[Akitando\] #\d+ - ', '', titulo).strip()

def normalizar_texto(texto):
    """Padroniza texto para comparação"""
    texto = limpar_prefixo(texto)  # Aplica a limpeza do prefixo primeiro
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto.strip().lower().translate(str.maketrans('', '', '!?.,:;-_\'\"'))

def filtrar_videos():
    try:
        # Carregar dados
        with open('processed/clean_posts.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
        with open('raw/videos.txt', 'r', encoding='utf-8') as f:
            titulos_txt = {normalizar_texto(linha.strip()) for linha in f}

        # Processar e filtrar
        dados_filtrados = []
        for item in dados:
            titulo_limpo = normalizar_texto(item.get('titulo', ''))
            
            if titulo_limpo in titulos_txt:
                dados_filtrados.append(item)
                print(f"Match encontrado:")
                print(f"Original: {item['titulo']}")
                print(f"Limpo:    {titulo_limpo}\n")

        # Salvar resultados
        with open('processed/videos_filtrados.json', 'w', encoding='utf-8') as f:
            json.dump(dados_filtrados, f, ensure_ascii=False, indent=4)
            
        print(f"Total de matches: {len(dados_filtrados)}")

    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == '__main__':
    filtrar_videos()