##conversões ou cast
# nome = input("Digite seu nome:")
# idade = int(input("Sua idade:"))
# peso = float(input("seu peso:"))

# print(nome)
# print(type(idade)) 
# print(type(peso))


##operadores
# soma = 1 + 1
# multipicacao = 4 * 4
# divisao = 30 / 3
# potencia = 7 ** 2

# print("soma", soma)
# print("multipicacao", multipicacao)
# print("divisao", divisao)
# print("potencia", potencia)


##condicionais
# idade = int(input("Informe sua idade: "))

# if idade >= 18:
#     print("Liberado !!")
# else:
#     print("Não liberado !!")


##If/Elif/Else
# salario = float(input("Informe seu salario:"))

# if salario <= 3000:
#     print("Junior")
# elif salario >3000 and salario <= 6000:
#     print("Pleno")
# elif salario > 6000 and salario <=15000:
#     print("senior")
# else:
#     print("gerente de projetos")    


##listas
# lista_numeros = [1, 2, 3]

# lista_numeros[0] = 5

# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])

# lista_vazia = []

# lista_vazia.append("Olá")
# lista_vazia.append("Mundo")

# print(lista_vazia)


##Repetições / loops (For e While)
notas = []

for X in range(3):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)