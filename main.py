import math
from collections import defaultdict
from collections import Counter
import statistics
import pandas

def helloWorldFuncao():
    print('hello world python')


def retornaSoma(x, b):
    return x + b


print(retornaSoma(2, 3))


def apply_to_one(f):
    return 1 + f


print(f"Python eh beleza {retornaSoma(2, 4)}")

try:
    print(0 / 0)
except ZeroDivisionError:
    print('Nao pode dividir por zero')

lista = [5, 6]
listaDois = [1, 2, 3, 4]
print(len(lista))
print(sum(listaDois))

listaDois.extend(lista)
print(listaDois)
print(6 in listaDois)

tupla = (1, 4)


def retornaDoisValores(a, b):
    return (a + b), (a * b)


print(retornaDoisValores(2, 3))

dicionarvazio = {}
dicionariovaziodois = dict()

notas = {"Gabriel": 100, "Jorge": 95}

gabriel = notas["Gabriel"]

print(notas["Gabriel"])
print(f"João tem notas: {'Joao' in notas}")

jorgeNotas = notas.get("Jorge", 0)
print(jorgeNotas)

document = ["Bayern", "Vasco", "Corinthians", "Bayern", "Bayern", "Bayern", "Bayern"]

contadorPalavras = defaultdict(int)

for word in document:
    contadorPalavras[word] += 1

print(contadorPalavras.values())

c = Counter([0, 1, 2, 3])

print(c)

word_counts = Counter(document)
print(word_counts)

for word, count in word_counts.most_common(1):
    print(word, count)

numeros_primos_abaixo_10 = {2, 3, 5, 7}

s = set()
s.add(1)
s.add(2)
s.add(3)

vasco = ("true" if 2 % 3 == 0 else "false")
print(vasco)

resultado = 7

while resultado <= 1000:
    resultado = resultado * 7

print(resultado)

for character in 'Programacao':
    print(character)

print(f"Numero {7} vezes {5} = {7 * 5}")

for x in range(99, 0, -11):
    print(x)

notas = [30, 20, 10, 20, 40, 30, 229]

print(statistics.median(notas))
print(statistics.mode(notas))

print(sorted(notas)[math.floor(len(notas) / 2)])

valores = [47, 95, 88, 73, 88, 84]

print(f"Media: {statistics.mean(valores)}")
print(f"Mediana: {statistics.median(valores)}")
print(f"Moda: {statistics.mode(valores)}")



tupla = ("Sue", [89,94,85])
print(tupla)

nome = tupla[0]
notas = tupla[1]
print(f"Nome do aluno: {nome}, notas: {notas}")