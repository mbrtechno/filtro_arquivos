import re

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
print("Concluído.")
