````markdown
# BlogToBook 📚

Transforme conteúdos de blogs (extraídos via Easy Scraper) em livros organizados por tags e categorias.

---

## **Funcionalidades**

- 🛠️ Transforma JSON bruto (com `container` e `texts href`) em estrutura categorizada
- 🏷️ Extrai tags automaticamente do conteúdo
- 📊 Analisa frequência de tags e interseções
- 📂 Gera arquivos separados por assunto (ex: `career`, `philosophy`)
- 📕 Cria um livro estruturado com introdução e capítulos temáticos

---

## **Pré-requisitos**

- Python 3.10+
- Pip instalado

---

## **Instalação**

```bash
git clone https://github.com/seu-usuario/BlogToBook.git
cd BlogToBook
pip install -r requirements.txt
```
````

---

## **Uso**

### Passo 1: Prepare o JSON Bruto

Salve o JSON do Easy Scraper em:

```
data/raw/raw.json
```

### Passo 2: Execute os Scripts

```bash
# 1. Transforma JSON inicial
python src/1_transform_raw_json.py

# 2. Extrai tags e gera relatório
python src/2_extract_tags.py

# 3. Categoriza posts por assunto
python src/3_categorize_posts.py

# 4. Gera o livro final (Markdown)
python src/4_generate_book.py
```

---

## **Resultados**

| Pasta             | Conteúdo                                 |
| ----------------- | ---------------------------------------- |
| `data/processed/` | JSONs processados e categorizados        |
| `data/analysis/`  | Relatório de tags (`tags_report.json`)   |
| `output/book/`    | Livro em Markdown (`livro_compilado.md`) |

---

## **Estrutura do Projeto**

```
BlogToBook/
├── data/
│   ├── raw/                  # JSON bruto do Easy Scraper
│   ├── processed/            # Dados processados
│   └── analysis/             # Relatórios de análise
├── src/
│   ├── 1_transform_raw_json.py  # Transformação inicial
│   ├── 2_extract_tags.py        # Extração de tags
│   ├── 3_categorize_posts.py    # Categorização
│   └── 4_generate_book.py       # Geração do livro
├── output/
│   └── book/                 # Livro finalizado
├── docs/
│   └── workflow.md           # Fluxo detalhado
├── .gitignore                # Arquivos ignorados
├── requirements.txt          # Dependências
└── README.md                 # Este arquivo
```

## **Licença**

MIT License - [LICENSE](LICENSE)

---

## **Exemplo de Fluxo**

1. **Web Scraping**  
   Use o Easy Scraper para coletar dados do blog
2. **Processamento**  
   Execute os scripts para organizar posts em categorias
3. **Geração do Livro**  
   Personalize a introdução e exporte para PDF/EPUB

---

## **Dúvidas?**

Consulte [workflow.md](docs/workflow.md) ou abra uma **issue** no repositório

---

Feito com ❤️ por Tales
