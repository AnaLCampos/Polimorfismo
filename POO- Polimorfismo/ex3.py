class calculo:
    def calcular(self):
        pass

    def calcularsoma(self, num1, num2):
        return num1 + num2

    def calcularmultiplicacao(self, num1, num2):
        return num1 * num2

calculo = calculo()

soma = calculo.calcularsoma(8, 11)
print("Soma:", soma)

multiplicacao = calculo.calcularmultiplicacao(7, 9)
print("Multiplicação:", multiplicacao)
