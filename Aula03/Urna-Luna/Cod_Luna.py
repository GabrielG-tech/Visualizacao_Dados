import os

tabela_votacao = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

# Nome da pasta onde o arquivo será gerado
pasta_resultados = "C:\\Users\\gabriel.gsouza\\Documents\\Visualização_Dados\\Aula03\\Urna-Luna"

# Verifica se a pasta existe, senão a cria
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)

# Nome do arquivo de saída
nome_arquivo = os.path.join(pasta_resultados, "resultados_votacao.txt")

# Cria ou abre o arquivo para escrita
with open(nome_arquivo, 'w') as arquivo_txt:
    # Escreve o cabeçalho
    arquivo_txt.write("A\tB\tC\tBranco\tNulo\n")
     
    # Escreve no arquivo de texto
    for i in range(10):
        linha = "{}\t{}\t{}\t{}\t{}\n".format(tabela_votacao[i][0], tabela_votacao[i][1], tabela_votacao[i][2], tabela_votacao[i][3], tabela_votacao[i][4])
        arquivo_txt.write(linha)