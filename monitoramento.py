import sys

from colorama import Fore, Style, init

# Garante que a codificação do terminal suporte caracteres acentuados
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")
except AttributeError:
    pass

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    {"nivel": 1, "situacao": "Muito baixo - CRÍTICO", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo - Atenção", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio - Normal", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto - Atenção", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto - ALERTA", "cor": Fore.BLUE}
]

# Função que exibe o alerta com a cor correspondente
def exibir_alerta(nivel_informado):
    for item in niveis:
        if item["nivel"] == nivel_informado:
            print(
                item["cor"]
                + f"Nível {item['nivel']}: {item['situacao']}"
                + Style.RESET_ALL
            )
            return

    print("Nível inválido! Digite um número de 1 a 5.")

# Programa principal
print("=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===")

try:
    nivel_atual = int(input("Informe o nível da água (1 a 5): "))
    exibir_alerta(nivel_atual)
except ValueError:
    print("Entrada inválida! Digite um número inteiro.")