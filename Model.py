class Model:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    """ def trocar(self, valorA, valorB):
        valorC = valorA
        valorA = valorB
        valorB = valorC
        return f'Valor A: {valorA} \nValor B: {valorB}'

    def tabuada(self, num):
        resultado = "" #Variável String
        for i in range(0, 11, 1): #Inicio Quantidade de Repetições e de quanto em quanto
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado
    def mediaTres(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3)/3"""

    def exercicioUm(self):
        resultado = ""
        for i in range(1, 11, 1):
            resultado += f'{i} \n'
        return resultado
    def exercicioDois(self):
        resultado = ''
        for i in range(0, 21, 2):
            resultado += f'{i}\n'
        return resultado
    def exercicioTres(self):
        resultado = 0
        for i in range(1, 101, 1):
            resultado += i
        return resultado
    def exercicioQuatro(self):
        resultado = ''
        for i in range(0, 51, 5):
            resultado += f'{i} \n'
        return resultado
    def exercicioCinco(self, num):
        if num % 2 == 0:
            return f'O número {num} é par'
        else:
            return f'O número {num} é impar'

    def exercicioSeis(self,num):
        if num > 0:
            return f'O número {num} é positivo'
        elif num < 0:
            return f'O número {num} é negativo'
        elif num == 0:
            return f'O número {num} é igualmente a Zero'

    def exercicioSete(self,num):
        resultado = ''
        for i in range(0, 11, 1):
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado

    def exercicioOito(self,num):
        resultado = ''
        for i in range(0, num, 1):
            resultado += f'{i}\n'
        return resultado

    def exercicioNove(self,num):
        resultado = 0
        for i in range(1, (num + 1), 1):
            resultado += i
        return resultado

    def exercicioDez(self,num):
        resultado = '2\n3\n5'
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                resultado += f'\n{i}'
        return resultado

    def exercicioOnze(self,num):
        if num >= 2:
            for i in range(2, num):
                if num % i != 0:
                    return f'O número é Primo'
                else:
                    return f'O número não é Primo'

    def exercicioDoze(self,num):
        resultado = 1
        for i in range(1, num, 1):
            resultado *= i
        return resultado

    def exercicioTreze(self):
        fib1 = 0
        fib2 = 1
        fib3 = 0
        resultado = '0\n1\n'
        for i in range(1,9,1):
            fib3 = fib1 + fib2
            resultado += f'{fib3}\n'
            fib1 = fib2
            fib2 = fib3
        return resultado

    def exercicioQuatorze(self,num):
        fib1 = 0
        fib2 = 1
        fib3 = 0
        resultado = '0\n1\n'
        for i in range(1, num - 2, 1):
            fib3 = fib1 + fib2
            resultado += f'{fib3}\n'
            fib1 = fib2
            fib2 = fib3
        return resultado

    def exercicioQuinze(self,num):
        resto = 0
        while num / 10 != 0:
            resto += num % 10
            num = (num / 10)
        return f'A soma dos números é {resto}'
    def exercicioDezeseis(self,num):
        pares = ''
        impares = ''
        for i in range(0, num, 1):
            if i % 2 == 0:
                pares += f'{i}\n'
            elif i % 2 == 1:
                impares += f'{i}\n'
        return f'{pares}\n =================\n {impares}\n'

    def exercicioDezesete(self,num):
        resultado = '2\n3\n5'
        for i in range(5, num, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                resultado += f'\n{i}'
        return resultado

    def exercicioDezoito(self,num):
        par = ''
        impar = ''
        if num % 2 == 0:
            par = num / 2
        elif num % 2 == 1:
            impar = num * 3 + 1
        return f'{par}\n{impar}\n'