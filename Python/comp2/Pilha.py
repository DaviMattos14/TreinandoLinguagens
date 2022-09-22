"""
    Nome: Davi dos Santos Mattos    DRE: 119133049
"""

class Pilha:

    def __init__(self, elementos = []): # list → list
        """
            Método construtor, criar o atributo 'elemento' da classe Pilha,
            recebendo uma lista e retornando uma mensagem de sucesso juntamente com os itens atribuidos,
            caso a parâmetro recebido não seja uma lista,
            ele retorna uma mensagem de erro
        """
        if(isinstance(elementos, list)==True):
            self.elementos = elementos
            print(self.elementos)
            print("Sucesso\n")
        elif (isinstance(elementos, list) == False):
            self.elementos = []
            print(self.elementos)
            print("Erro\n")

    def empilhar(self, elemento): # list → list
        """
            Adiciona um elemento no final da lista
        """
        self.elementos.append(elemento)
    
    def desempilhar(self): # list → list, string
        """
            Remove o elemento no final da lista, 
            caso a lista eseteja vazia ele retona uma mensagem de erro
        """
        if(len(self.elementos) > 0):
            self.elementos.pop(len(self.elementos)-1)
        elif(len(self.elementos) == 0):
            print("Erro")

    def getPilha(self): # list → list
        """
            Retorna uma lista
        """
        return self.elementos
    
    def lenPilha(self): # list → int
        """
            Retorna a quantidade de elementos da lista
        """
        return len(self.elementos)


# 7.a) Testando método construtor
p1 = Pilha([1,7,9])
p2 = Pilha()

# 7.b) Testando método empilhar
p3 = Pilha(10)

# 7.c) Testando método desempilhar
p2.empilhar(4)
p2.empilhar(10)

# 7.d)
for i in range(len(p2.elementos)+1):
	p2.getPilha()
	p2.desempilhar()

# 7.e)
p2.empilhar(5)

# 7.f)


# 7.g) 
p3.getPilha()