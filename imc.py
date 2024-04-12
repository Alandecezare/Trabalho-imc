##Solicite para o usuario informar:
##    - Nome
##    - Altura (cm)
##    - Peso (kg)
##    Com base nestes dados realize o calculo para 
##    descobrir qual o IMC (indice de massa corporea)
##    da pessoa.
##    Para o calculo utilize a tabela padrão do IMC.
##    abaixo de 18,5 - Abaixo do Peso (Pegue suplementos do Cariani)
##    entre 18,6 e 24,9 - Peso Ideal (Para Bens)
##    entre 25,0 e 29,9 - Sobrepeso
##    entre 30,0 e 34,9 - Obesidade Grau 1
##    entre 35,0 e 39,9 - Obesidade Grau 2
##    acima de 40,0 - Obesidade Grau 3 (Dr. Nowzaradan te espera)
##    formula: IMC = peso / altura²

##nome= (input("Digite seu nome: "))
##altura= int(input"Digite altura em centimetros: ")
##peso= 

def calcular_imc(peso, altura):
    imc = peso / (altura/100) ** 2  # Convertendo altura de cm para m
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso (Pegue suplementos do Cariani)"
    elif 18.5 <= imc <= 24.9:
        return "Peso Ideal (Para Bens)"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade Grau 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3 (Dr. Nowzaradan te espera)"

nome = input("Digite o seu nome: ")
altura = float(input("Digite a sua altura em centímetros: "))
peso = float(input("Digite o seu peso em kg: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"Olá, {nome}! Seu IMC é {imc:.2f}, o que indica {classificacao}.")
