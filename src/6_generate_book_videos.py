import json
import re

def limpar_titulo(titulo):
    """Remove o prefixo [Akitando] #... - dos títulos"""
    return re.sub(r'^\[Akitando\] #\d+ - ', '', titulo).strip()

def gerar_livro_didatico():
    try:
        # Carregar os vídeos filtrados (arquivo gerado no script anterior)
        with open('data/processed/videos_filtrados.json', 'r', encoding='utf-8') as f:
            videos = json.load(f)
    
        # Criar dicionário de mapeamento (título limpo -> vídeo completo)
        mapa_videos = {}
        for video in videos:
            titulo = video.get('titulo', '')
            titulo_limpo = limpar_titulo(titulo)
            video['titulo_limpo'] = titulo_limpo  # Armazena a versão limpa para referência
            mapa_videos[titulo_limpo] = video

        # Processar a estrutura de capítulos a partir do arquivo de capítulos
        estrutura_capitulos = {}
        with open('data/raw/caps.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                partes = linha.strip().split(' - ', 1)
                if len(partes) == 2:
                    capitulo, titulo_video = partes
                    titulo_video_limpo = limpar_titulo(titulo_video)
                    
                    if capitulo not in estrutura_capitulos:
                        estrutura_capitulos[capitulo] = []
                    
                    # Se o título limpo estiver no mapeamento, adiciona ao capítulo
                    if titulo_video_limpo in mapa_videos:
                        estrutura_capitulos[capitulo].append(mapa_videos[titulo_video_limpo])
                        # Remove o vídeo do mapeamento para não duplicar na seção de não catalogados
                        del mapa_videos[titulo_video_limpo]

        # Gerar conteúdo formatado do livro didático
        conteudo = []
        for capitulo, videos_capitulo in estrutura_capitulos.items():
            conteudo.append(f"\n\n=== {capitulo.upper()} ===")
            
            for idx, video in enumerate(videos_capitulo, 1):
                conteudo.append(f"\nAula {idx}: {video.get('titulo_limpo', 'Título não disponível')}")
                conteudo.append(f"Data: {video.get('data', 'Data não informada')}")
                conteudo.append(f"Conteúdo: {video.get('container', 'Conteúdo não disponível')}")
                conteudo.append(f"Link: {video.get('texts href', 'Link não informado')}")
                conteudo.append(f"Tags: {video.get('tag', 'Tags não informadas')}")
                conteudo.append("-" * 50)

        # Adicionar vídeos que não foram catalogados em nenhum capítulo
        if mapa_videos:
            conteudo.append("\n\n=== CONTEÚDO NÃO CATALOGADO ===")
            for video in mapa_videos.values():
                conteudo.append(f"\nTítulo: {video.get('titulo_limpo', 'Título não disponível')}")
                conteudo.append(f"Data: {video.get('data', 'Data não informada')}")
                conteudo.append(f"Conteúdo: {video.get('container', 'Conteúdo não disponível')}")
                conteudo.append(f"Link: {video.get('texts href', 'Link não informado')}")
                conteudo.append(f"Tags: {video.get('tag', 'Tags não informadas')}")
                conteudo.append("-" * 50)

        # Salvar o livro didático em um arquivo de saída
        with open('output/book/livro_didatico.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(conteudo))

        print("Livro didático gerado com sucesso!")

    except Exception as e:
        print(f"Erro ao gerar livro didático: {str(e)}")

if __name__ == '__main__':
    gerar_livro_didatico()