import os
import time

class Calculadora:
    def __init__(self, n1=10, n2=10):
        self.n1 = n1
        self.n2 = n2
        
    def soma(self, n1, n2):
        return n1 + n2
        
    def subtracao(self, n1, n2):
        return n1 - n2
    
    def multiplicacao(self, n1, n2):
        return n1 * n2
    
    def divisao(self, n1, n2):
        return n1 / n2
        

calculadora01 = Calculadora(50, 10)

print(calculadora01.soma(50, 10))