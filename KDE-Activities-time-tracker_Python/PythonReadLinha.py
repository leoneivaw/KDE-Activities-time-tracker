#   /home/leonardo/.local/share/utt/utt.log


with open('/home/leonardo/.local/share/utt/utt.log') as f:
    for line in f:
        pass
    linha = line

print(linha)
print(len(linha))
#TAMANHO
tamanho = len(linha)
print(linha[-7:tamanho])
print(linha[-8:-3])
# pula 1 caractere e imprime outro
print(linha[1:6:2])
print(linha[-1:])

# remove quebra de linha
linha2 = linha.replace('\r', '').replace('\n', '')
print(len(linha2))
print(linha2[-1:])


fim = linha2.endswith('do')
print(fim)

if  linha2.endswith('do'):
    print("Termina com do")
if linha2.endswith('**'):
    print("Termina com **")

print("Find: ",linha2.find("Estudo"))
first, *middle, last = linha.split()
quebra = linha.split()
print("Split", last, first, (middle))
print("quebra: ", quebra[-2])
