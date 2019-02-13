#!/usr/bin/python3


texto_grotesco = "Por conseguinte, o novo modelo estrutural aqui preconizado nos obriga à análise das condições financeiras e administrativas exigidas. Ainda assim, existem dúvidas a respeito de como o surgimento do comércio virtual faz parte de um processo de gerenciamento das regras de conduta normativas. Neste sentido, a execução dos pontos do programa exige a precisão e a definição do fluxo de informações." 


nomes = ['Hector', 'Guilherme', 'Joel', 'Flávio', 'Fabiano', 'Roger', 'Cícero', 'Hugo', 'Ayron', 'Leonel', 'Pedro', 'Lucas']


if "virtual" in texto_grotesco:

    
    print(nomes[-4:])


print(len(texto_grotesco.split(" ")))


for n in nomes:

    if n[0] == "F":

        print(n)

    elif n[0] == "H":

        print(n)

        

    



#OPERADORES

exit()
n1 = int(input ("numero 1: "))
n2 = int(input ("numero 1: "))

n3 = n1 + n2

if n3 == 100:

    print("O Numero é igual")

elif n3 > 100:
        
    print("Que numero Grandão")

else:

    print("Que numero Pequene")
