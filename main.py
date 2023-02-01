import re
import os

variavel = input('Digite o nome do arquvio com .txt: ')
arquivo = open(variavel, "r")  # abre arquivo a ser tratado
result = open("resultado.txt", "w")  # cria arquivo que irá receber o resultado

for linha in arquivo:
    x = re.findall("0x.{8};32", linha)
    if x:
        saida = "".join(x) + '\n'  # enter no final de cada/converte list em str
        saida = re.sub(";32", " ", saida)  # remove ;32
        result.writelines(saida)        # grava resultado da linha

result.close()
arquivo.close()

result = open("resultado.txt", "r")
dados = open("troca.txt", "w")
contador = 0

for linha in result:
    contador += 1
    if 4 <= contador <= 11:
        dados.writelines(linha)
    if contador == 11:
        contador = 0
dados.close()
result.close()

dados = open("troca.txt", "r")
result = open("resultado.txt", "w")
for linha in dados:
    x = re.findall("0x.{8}", linha)
    saida = "".join(x) + "\n"
    saida = re.sub("0x", "", saida)
    result.writelines(saida)        # grava resultado da linha

result.close()
dados.close()
os.remove("troca.txt")
print("Concluido.")
