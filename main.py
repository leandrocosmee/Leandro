# Importando o módulo 'funcs' que contém as funções de encriptação e desencriptação
import funcs

# Definindo o nome do arquivo que contém o texto a ser encriptado
ficheiro = "texto.txt"

# Solicitando ao usuário que forneça a chave para a encriptação
chave = int(input(">> Chave de encriptação: "))  # Converte a entrada do usuário para um número inteiro

# Encriptando o conteúdo do arquivo usando a função de encriptação do módulo 'funcs'
texto_encriptado = funcs.transposicao_encriptar(ficheiro, chave)

# Desencriptando o texto encriptado usando a função de desencriptação do módulo 'funcs'
texto_desencriptado = funcs.transposicao_desencriptar(texto_encriptado, chave)

# Abrindo um novo arquivo para escrever o texto encriptado
with open('texto_encriptado.txt', 'w', encoding='utf-8') as ficheiro_encriptado:
    # Escreve o texto encriptado no arquivo 'texto_encriptado.txt'
    ficheiro_encriptado.write(texto_encriptado)

# Abrindo um novo arquivo para escrever o texto desencriptado
with open('texto_desencriptado.txt', 'w', encoding='utf-8') as ficheiro_desencriptado:
    # Escreve o texto desencriptado no arquivo 'texto_desencriptado.txt'
    ficheiro_desencriptado.write(texto_desencriptado)

# Exibindo o texto encriptado na tela
print("Texto encriptado:")
print(texto_encriptado)

# Exibindo o texto desencriptado na tela
print("\nTexto desencriptado:")
print(texto_desencriptado)
