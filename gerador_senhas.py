# Gerador de Senhas em Python
# Este programa cria senhas aleatórias com diferentes níveis de complexidade.

import random
import string

# Função para gerar uma senha aleatória
def gerar_senha(tamanho, complexidade):
    # Define os conjuntos de caracteres d
    letras = string.ascii_letters  # Letras maiúsculas e minúsculisponíveisas
    numeros = string.digits        # Dígitos de 0 a 9
    simbolos = string.punctuation  # Símbolos especiais

    # Escolhe os tipos de caracteres com base na complexidade
    if complexidade == 1:
        caracteres = letras
    elif complexidade == 2:
        caracteres = letras + numeros
    elif complexidade == 3:
        caracteres = letras + numeros + simbolos
    else:
        return "Nível de complexidade inválido! Por favor, escolha entre 1, 2 ou 3."

    # Gera a senha com os caracteres escolhidos
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Mensagem de boas-vindas
print("Bem-vindo ao Gerador de Senhas!")
print("Vamos criar uma senha personalizada para você.")

# Exibição do menu de opções
print("Escolha o nível de complexidade da sua senha:")
print("1. Somente letras (mais simples)")
print("2. Letras e números (médio)")
print("3. Letras, números e símbolos (mais seguro)")

# Entrada de dados do usuário
try:
    complexidade = int(input("Digite o nível de complexidade (1, 2 ou 3): "))
    tamanho = int(input("Digite o tamanho desejado para a senha: "))

    # Verifica se o tamanho é válido
    if tamanho <= 0:
        print("O tamanho da senha precisa ser maior que zero. Tente novamente.")
        exit()

    # Gera e exibe a senha
    senha = gerar_senha(tamanho, complexidade)
    print(f"Aqui está a sua senha gerada: {senha}")

except ValueError:
    print("Erro: Por favor, insira valores numéricos para o nível de complexidade e o tamanho da senha.")