# 💧 Sistema de Monitoramento de Reservatório de Água

## 📌 Sobre o projeto

Este projeto foi desenvolvido em Python para simular o monitoramento do nível de água de um reservatório. A aplicação recebe um valor de 1 a 5 e exibe uma mensagem de alerta colorida no terminal, indicando a situação do reservatório.

## 🚨 Funcionalidades

- Classificação do nível da água em 5 faixas;
- Mensagens visuais com cores para facilitar a interpretação;
- Validação de entrada para aceitar apenas números inteiros de 1 a 5;
- Exibição de alerta em console para acompanhamento rápido.

## 🧪 Requisitos

- Python 3.8 ou superior;
- Biblioteca Colorama.

## ▶️ Como executar

1. Instale a dependência:

```bash
pip install colorama
```

2. Execute o programa:

```bash
python monitoramento.py
```

3. Informe um nível entre 1 e 5 quando solicitado.

## 📝 Exemplo de uso

```text
=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===
Informe o nível da água (1 a 5): 3
Nível 3: Médio - Normal
```

## 📊 Níveis disponíveis

- 1: Muito baixo - CRÍTICO
- 2: Baixo - Atenção
- 3: Médio - Normal
- 4: Alto - Atenção
- 5: Muito alto - ALERTA

Este projeto é uma solução simples e didática para demonstrar uso de entrada de dados, validação e apresentação visual em terminal.