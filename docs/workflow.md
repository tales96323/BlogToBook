# Fluxo de Trabalho

1. **Web Scraping** (Feito no Easy Scraper)
   - Saída: JSON com `container` e `texts href`

2. **Transformação Inicial**
   - Separa título, data e conteúdo do `container`

3. **Extração de Tags**
   - Identifica tags no final do conteúdo
   - Gera relatório de frequência

4. **Categorização**
   - Mapeia tags para categorias pré-definidas
   - Permite interseção entre categorias

5. **Geração do Livro**
   - Cria arquivos por categoria
   - Opções de formato: Markdown, PDF, EPUB