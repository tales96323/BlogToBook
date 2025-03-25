import json
import re
import unicodedata

def limpar_prefixo(titulo):
    """Remove o padrão [Akitando] #... - do início do título"""
    return re.sub(r'^\[Akitando\] #\d+ - ', '', titulo).strip()

def normalizar_texto(texto):
    """Padroniza o texto para comparação removendo prefixos, acentos e pontuações"""
    texto = limpar_prefixo(texto)  # Limpa o prefixo primeiro
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto.strip().lower().translate(str.maketrans('', '', '!?.,:;-_\'\"'))

def filtrar_videos():
    try:
        # Carregar dados do JSON já limpo
        with open('data/processed/clean_posts.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
        # Carregar os títulos dos vídeos do arquivo
        with open('data/raw/videos.txt', 'r', encoding='utf-8') as f:
            titulos_txt = {normalizar_texto(linha.strip()) for linha in f if linha.strip()}

        # Processar e filtrar os posts que possuem título compatível com os vídeos
        dados_filtrados = []
        for item in dados:
            titulo = item.get('titulo', '')
            titulo_limpo = normalizar_texto(titulo)
            
            if titulo_limpo in titulos_txt:
                dados_filtrados.append(item)
                print("Match encontrado:")
                print(f"Original: {titulo}")
                print(f"Limpo:    {titulo_limpo}\n")

        # Salvar os resultados filtrados na pasta processed
        with open('data/processed/videos_filtrados.json', 'w', encoding='utf-8') as f:
            json.dump(dados_filtrados, f, ensure_ascii=False, indent=4)
            
        print(f"Total de matches: {len(dados_filtrados)}")

    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == '__main__':
    filtrar_videos()
