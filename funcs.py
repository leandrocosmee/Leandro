# Função para encriptar o texto utilizando a cifra de transposição
def transposicao_encriptar(nome_arquivo: str, chave: int) -> str:
    
    # Abrindo o arquivo e lendo o conteúdo como texto
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:  # Abertura do arquivo com codificação UTF-8
        texto = arquivo.read()  # Lê todo o conteúdo do arquivo
    
    # Criando uma lista de strings vazias para representar as colunas da grade
    grade = [''] * chave  # A lista 'grade' terá o número de colunas igual ao valor da chave
    
    # Distribuindo os caracteres do texto nas colunas
    for i in range(len(texto)):  # Percorre cada caractere do texto
        coluna = i % chave  # Calcula em qual coluna o caractere será inserido
        grade[coluna] += texto[i]  # Adiciona o caractere à coluna correspondente
    
    # Junta todas as colunas em uma string única e retorna o texto encriptado
    return ''.join(grade)  # Concatena as colunas e retorna o texto criptografado

# Função para desencriptar o texto utilizando a cifra de transposição
def transposicao_desencriptar(texto_encriptado: str, chave: int) -> str:
    
    # Calculando o número de linhas da grade
    num_linhas = len(texto_encriptado) // chave  # Número de linhas com base no tamanho do texto dividido pela chave
    if len(texto_encriptado) % chave != 0:  # Se houver um resto na divisão, significa que há uma linha extra
        num_linhas += 1  # Adiciona uma linha extra para acomodar o resto

    # Criando a lista de linhas da grade
    grade = [''] * num_linhas  # Inicializa uma lista de linhas com o número de linhas calculado
    col = 0  # Contador para percorrer os caracteres do texto criptografado
    
    # Preenchendo a grade com os caracteres do texto encriptado
    for i in range(chave):  # Para cada coluna da chave
        for j in range(num_linhas):  # Para cada linha da grade
            if col < len(texto_encriptado):  # Verifica se ainda há caracteres para preencher
                grade[j] += texto_encriptado[col]  # Adiciona o caractere à linha correspondente
                col += 1  # Avança para o próximo caractere
    
    # Junta todas as linhas em uma string única e retorna o texto desencriptado
    return ''.join(grade)  # Concatena as linhas e retorna o texto desencriptado
