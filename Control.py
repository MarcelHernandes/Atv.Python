from Model import Model

class Control:
    def __init__(self):
        self.modelo = Model() #Instanciando a classe model
        self.opcao = 0

    def mostrarMenu(self):
        print('Escolha uma das opções abaixo: ' +
              '\n0. Sair'                       +
              '\n1. Exercicio 1'                +
              '\n2. Exercicio 2'                +
              '\n3. Exercicio 3'                +
              '\n4. Exercicio 4'                +
              '\n5. Exercicio 5'                +
              '\n6. Exercicio 6'                +
              '\n7. Exercicio 7'                +
              '\n8. Exercicio 8'                +
              '\n9. Exercicio 9'                +
              '\n10. Exercicio 10'              +
              '\n11. Exercicio 11'              +
              '\n12. Exercicio 12'              +
              '\n13. Exercicio 13'              +
              '\n14. Exercicio 14'              +
              '\n15. Exercicio 15'              +
              '\n16. Exercicio 16'              )

    def operacoes(self):
        while(self.opcao != 1):
            self.mostrarMenu()
            self.opcao = int(input('Informe um número: '))
            if self.opcao == 0:
                print('Obrigado!')
            elif self.opcao == 1:
                print(self.modelo.exercicioUm())
            elif self.opcao == 2:
                print(self.modelo.exercicioDois())
            elif self.opcao == 3:
                print(self.modelo.exercicioTres())
            elif self.opcao == 4:
                print(self.modelo.exercicioQuatro())
            elif self.opcao == 5:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioCinco(num))
            elif self.opcao == 6:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioSeis(num))
            elif self.opcao == 7:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioSete(num))
            elif self.opcao == 8:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioOito(num))
            elif self.opcao == 9:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioNove(num))
            elif self.opcao == 10:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioDez(num))
            elif self.opcao == 11:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioOnze(num))
            elif self.opcao == 12:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioDoze(num))
            elif self.opcao == 13:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioDoze(num))
            else:
                print('Opção escolhida não é válida!')
            return
