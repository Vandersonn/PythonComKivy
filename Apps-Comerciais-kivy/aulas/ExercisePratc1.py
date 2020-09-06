#Exercícios Práticos 1 - Conceitos da Programação e do Python
"""
#1) Faça um algoritmo que apenas imprima o seu nome na tela e em seguida finalize a aplicação.
print('Vanderson de Castro')

#2) Faça um algoritmo que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase para
#a saída padrão: "O seu nome é: [nome do usuário]".
nome = input('Digite seu nome. ')
print("O seu nome é: ", nome)

#3) Faça um algoritmo que solicite o nome e a idade do usuário e então, envie a seguinte frase para o
#Console: "O seu nome é <nome> e a sua idade é <idade>".
nome = input('Digite seu nome. ')
idade = int(input('Digite sua idade. '))
print("O seu nome é: ", nome, "e a sua idade é: ", idade)

#4) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, armazene este número numa
#variável. Por fim, envie esse número para a saída padrão.
numero = input('Digite um numero. ')
print("O numero é: ", numero)

#5) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, escreva a seguinte mensagem:
#"O número digitado foi: ".
numero = input('Digite um numero. ')
print("O numero digitado é: ", numero)

#6) Faça um algoritmo que solicite ao usuário informar 3 números. Em seguida, some-os e envie para a saída
#padrão a seguinte frase: "A soma total é: "
num1 = float(input('Digite o 1 numero. '))
num2 = float(input('Digite o 2 numero. '))
num3 = float(input('Digite o 3 numero. '))
soma = num1 + num2 + num3
print("A soma total é : ", soma)

#7) Faça um algoritmo que solicite ao usuário informar 2 números. Em seguida, some os valores e envie para
#a saída padrão a seguinte frase: "A soma entre <X> e <Y> é igual <total>".
x = float(input('Digite o 1 numero. '))
y = float(input('Digite o 2 numero. '))
soma = x + y
print("A soma entre <x>", x," e <y>", y, "é igual <total> : ", soma)

#8) Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário. Em seguida, calcule e envie
#para a saída padrão a média:

num1 = float(input('Digite o 1 numero. '))
num2 = float(input('Digite o 2 numero. '))
num3 = float(input('Digite o 3 numero. '))
num4 = float(input('Digite o 3 numero. '))
soma = (num1 + num2 + num3 + num4)/4
print("A nota total é : ", soma)

#9) Faça um algoritmo em que o usuário informe uma medida em metros. Em seguida, converta essa medida para
#centímetros e envie para a saída padrão:

numero = int(input('Digite um numero. '))
print("Conversão de ",numero," metros para %.2f " %numero,"Cm")

#10) Faça um algoritmo que calcule o cubo e o quadrado de um determinado número:

numero = input('Digite um numero. ')
numero = numero
numero = numero
print("O cubo é: ", numero)
print("O quadrado é: ", numero)

#11) Faça um algoritmo que solicite ao usuário digitar 2 números. Em seguida, imprima o total decimal da
#divisão e o total inteiro (sem casas decimais):

numero1 = float(input('Digite o 1 numero. '))
numero2 = float(input('Digite o 2 numero. '))
numero = numero1 / numero2
num = numero1 // numero2
print("O  é: %.2f " %numero)
print("O  é:%.i " %num)
"""
#12) Faça um algoritmo que solicite a largura e a altura de um retângulo. Em seguida, imprima para o
#usuário quantos metros quadrados possui a área total.



#13) Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas, minutos e
#segundos. Em seguida, converta tudo para segundos:

#14) Faça um algoritmo que solicite ao usuário informar o valor de uma compra. Em seguida, aplique 10%
#de desconto e imprima na tela tanto o valor total e também o valor com o desconto aplicado.