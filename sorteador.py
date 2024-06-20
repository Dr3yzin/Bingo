import random

numeros_rodados = []

def sortear_numero():
    while True:
        numero = random.randint(1, 75)
        if numero not in numeros_rodados:
            numeros_rodados.append(numero)
            if numero < 16:
                if numero < 10:
                    numero = str(numero)
                    numero = '0' + numero
                    numero = "B " + numero
                else:
                    numero = str(numero)
                    numero = "B " + numero
            elif numero < 31:
                numero = str(numero)
                numero = "I " + numero
            elif numero < 46:
                numero = str(numero)
                numero = "N " + numero
            elif numero < 61:
                numero = str(numero)
                numero = "G " + numero
            else:
                numero = str(numero)
                numero = "O " + numero
            return numero
        elif len(numeros_rodados) >= 75:
            return "000"