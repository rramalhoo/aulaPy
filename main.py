## Conversões ou cast
# nome = input("Digite seu nome:")
# idade = int(input("Sua idade:"))
# peso = float(input("seu peso:"))

# print(nome)
# print(type(idade)) 
# print(type(peso))


## Operadores
# soma = 1 + 1
# multipicacao = 4 * 4
# divisao = 30 / 3
# potencia = 7 ** 2

# print("soma", soma)
# print("multipicacao", multipicacao)
# print("divisao", divisao)
# print("potencia", potencia)


## Condicionais
# idade = int(input("Informe sua idade: "))

# if idade >= 18:
#     print("Liberado !!")
# else:
#     print("Não liberado !!")


## If/Elif/Else
# salario = float(input("Informe seu salario:"))

# if salario <= 3000:
#     print("Junior")
# elif salario >3000 and salario <= 6000:
#     print("Pleno")
# elif salario > 6000 and salario <=15000:
#     print("senior")
# else:
#     print("gerente de projetos")    


## Listas
# lista_numeros = [1, 2, 3]

# lista_numeros[0] = 5

# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])

# lista_vazia = []

# lista_vazia.append("Olá")
# lista_vazia.append("Mundo")

# print(lista_vazia)


## Repetições / loops (For e While)
# COM FOR
# notas = []

# for X in range(3):
#     codigo_aluno = input("RM: ")
#     nota = float(input("Nota: "))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

# print ("quantidade de notas", len(notas) )

# for n in notas:
#     codigo_aluno = n[0]
#     nota = n[1]
#     print("O RM", codigo_aluno, "tirou a nota:", nota)

# COM WHILE
# notas = []

# contador = 1

# while contador <= 5:
#      codigo_aluno = input("RM: ")
#      nota = float(input("Nota: "))
#      resultado = [codigo_aluno, nota]
#      notas.append(resultado)

#      #alternativa: contador += 1 
#      contador = contador + 1

# print("quantidade de notas", len(notas))


## Dicionários
# player = {
#     "nome": "Raphael",
#     "level": 1,
#     "hp": 100,
#     "xp": 0,
#     "dano": 5,
# }

## Lista de inimigos
# npcs = [
#     { "nome": "Down", "dano": 2, "hp":50, "xp":5 },
#     { "nome": "Mano Down", "dano": 5, "hp":100, "xp":10 },
#     { "nome": "Super Mano Down", "dano": 10, "hp":150, "xp":15 },
#     { "nome": "Mano Down Supremo", "dano": 25, "hp":200, "xp":20 },
# ]


# ## Criando um chat de mensagens
# import os

# mensagens = []

# nome = input("Nome: ")

# while True:
    
#     #Limpando terminal usando a importação OS
#     os.system('cls')

#     if len(mensagens) > 0:
#         for m in mensagens:
#             print(m['nome'], "-", m['texto'])

#     #separar lista de mgs exibida cm o input
#     print("_______________")

#     #obtendo texto
#     texto = input("mensagem: ")
#     if texto == "fim":
#         break

#     #adicionando mensagem na lista
#     mensagens.append({
#         "nome": nome,
#         "texto": texto
#     })


##Funcoes
# def minha_funcao(valor1, valor2):
#     return valor1 + valor2

# while True:
#     valor1 = int(input("Primeiro valor: "))
#     valor2 = int(input("Segundo valor"))

#     resposta = minha_funcao(valor1, valor2)

#     print(valor1, "+", valor2, "=", resposta)

##Joguinho basico
import os

player = {"nome": "Python", "x": 0, "y": 0}

def andar(direcao):
    if direcao == "d":
        player['x'] += 1
    elif direcao == "a":
        player['x'] -= 1
    elif direcao == "w":
        player['y'] -= 1
    elif direcao == "s":
        player['y'] += 1

while True:
    os.system('clear')

    print("------------------------------")
    for y in range(5):
        print("\n")
        for x in range(10):
            if player['x'] == x and player['y'] == y:
                print("🧍", end="")
            else:
                print("⬜", end="")
    
    print("\n------------------------------")
    
    direcao = input("Próxima direção (w,s,d,a): ")
    andar(direcao)