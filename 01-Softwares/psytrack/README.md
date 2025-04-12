# PsyTrack — Sistema de Gestão de Sessões Psicológicas

PsyTrack é um aplicativo desktop desenvolvido com [Flet](https://flet.dev) e Python que permite a psicólogos registrarem sessões, justificativas de atendimento e gerarem relatórios automáticos em Excel. O foco principal foi criar uma solução simples, portátil e funcional que possa ser utilizada por diversos profissionais sem necessidade de instalações complexas.

## 🌟 Funcionalidades
- Cadastro de sessões clínicas com:
  - Nome do paciente
  - Data da sessão
  - Situação (Realizada / Não / Remarcada)
  - Justificativa
  - Comentários adicionais
- Exportação de relatórios mensais em Excel com:
  - Nome do psicólogo
  - Mês de referência
  - Cálculo automático da coluna "Cobrar" (1 ou 0)
- Interface amigável, responsiva e leve
- Dados armazenados localmente em SQLite

## ✨ Tecnologias Utilizadas
- Python 3.11+
- [Flet](https://flet.dev) — para a interface gráfica multiplataforma
- SQLite — banco de dados local
- OpenPyXL — geração e manipulação de arquivos Excel

## ⚖️ Instalação (Desenvolvedores)

1. Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Execute o aplicativo:
```bash
flet run main.py
```

## 🚀 Geração de Executável (Windows)

Para empacotar como `.exe` usando PyInstaller:
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```
O executável estará em `dist/main.exe`.

## 🌍 Estrutura do Projeto
```
psytrack/
├── main.py                  # ponto de entrada
├── db.py                    # operações com SQLite
├── relatorio_utils.py       # geração de Excel
├── views/
│   ├── home.py              # tela inicial
│   ├── cadastrar.py         # cadastro de sessões
│   └── relatorio.py         # geração de relatórios
├── modelo/
│   └── planilha_atendimento.xlsx  # modelo de relatório
├── relatorios/              # onde relatórios gerados serão salvos
├── requirements.txt         # dependências
├── .gitignore               # arquivos ignorados pelo git
└── README.md
```

## 📊 Exemplo de Uso
1. Abrir o aplicativo
2. Cadastrar sessões conforme forem realizadas ou não
3. Acessar a aba "Emitir Relatório"
4. Selecionar o mês, ano e nome do psicólogo
5. Gerar o relatório e salvar em Excel

## 🌞 Objetivo Profissional
Esse projeto foi desenvolvido como parte do meu portfólio pessoal com foco em:
- Demonstração de competências em Python, GUI e manipulação de arquivos
- Entrega de solução real usada por psicólogos parceiros
- Aplicação de boas práticas de organização de projeto

## 📢 Contato
Thiago Barboza | 
www.linkedin.com/in/devthiagobarboza |
devthiagobarboza@gmail.com  

---

**Este projeto está em evolução. Sugestões e colaborações são muito bem-vindas!**

