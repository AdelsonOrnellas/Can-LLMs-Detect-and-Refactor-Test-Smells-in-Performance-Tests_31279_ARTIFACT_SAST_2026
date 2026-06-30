# k6 Performance Smell Detector 🔍 (Python)

Analisa scripts k6 contra **4 performance smells** usando **Claude, ChatGPT e Gemini simultaneamente**.

## Setup

### 1. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv

# Ativar no macOS/Linux:
source venv/bin/activate

# Ativar no Windows:
venv\Scripts\activate
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as API Keys
Edite o `.env`:
```
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=AIza...
```

### 4. Coloque seus scripts k6 na pasta `k6_scripts/`

### 5. Rode
```bash
# macOS/Linux
export $(cat .env | xargs) && python analyze.py

# Windows (PowerShell)
Get-Content .env | ForEach-Object { $k,$v = $_ -split '=',2; [System.Environment]::SetEnvironmentVariable($k,$v) }
python analyze.py

# Ou instale python-dotenv e adicione no topo do analyze.py:
# from dotenv import load_dotenv; load_dotenv()
```

## Estrutura
```
k6-smell-detector-py/
├── analyze.py            ← Script principal
├── requirements.txt      ← Dependências Python
├── .env                  ← Suas API keys
├── .env.example          ← Template
├── k6_scripts/           ← Coloque seus arquivos k6 aqui
│   └── example_with_smells.js
└── results/              ← Gerado automaticamente
    ├── results.json
    └── report.md
```

## Dica: carregar .env automaticamente

Instale `python-dotenv`:
```bash
pip install python-dotenv
```

E adicione no topo do `analyze.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

Assim não precisa exportar as variáveis manualmente.
