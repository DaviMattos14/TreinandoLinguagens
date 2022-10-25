class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def getTelefone(self):
        return self.__telefone

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getEndereco(self):
        return self.__endereco

    def setIdentidade(self, identidade):
        self.__identidade = identidade

    def getIdentidade(self):
        return self.__identidade

    def setIdade(self, idade):
        self.__idade = idade

    def getIdade(self):
        return self.__idade


class Notas:
    def __init__(self, nota1, nota2, nota3):
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3

    def setNota1(self, novaNota):
        self.__nota1 = novaNota

    def getNota1(self):
        return self.__nota1

    def setNota2(self, novaNota):
        self.__nota2 = novaNota

    def getNota2(self):
        return self.__nota2

    def setNota3(self, novaNota):
        self.__nota3 = novaNota

    def getNota3(self):
        return self.__nota3

    def calcular_Media(self):
        return (self.getNota3() + self.getNota2() + self.getNota1()) / 3

    def __str__(self):
        return str('P1: {} P2: {} P3: {}'.format(self.__nota1, self.__nota2, self.__nota3))


class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, notaAluno):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.__notaAluno = notaAluno

    def setMatricula(self, nova_matricula):
        self.__matricula = nova_matricula

    def getMatricula(self):
        return self.__matricula

    def setNotaAluno(self, nova_notaAluno):
        self.__notaAluno = nova_notaAluno

    def getMatricula(self):
        return self.__notaAluno

    def visualisarMedia(self):
        return self.__notaAluno.calcular_Media()

    def __str__(self):
        return str("Nome: {} CPF: {} Matricula: {} \nNotas: {}\n".format(self.nome, self.cpf, self.__matricula, self.__notaAluno))


class Professor(Pessoa):
    def __init__(self, nome, cpf, salario=0):
        super().__init__(nome, cpf)
        self.salario = salario

    def mostrarSalario(self):
        print(self.salario)


class Professor_Horista(Professor):
    def __init__(self, nome, cpf, salario, hora_de_aula, valor_de_aula):
        super().__init__(nome, cpf, salario)
        self.hora_de_aula = hora_de_aula
        self.valor_de_aula = valor_de_aula

    def calcula_salario(self):
        return self.hora_de_aula * self.valor_de_aula


class Controller:
    lista_professor = []
    lista_aluno = []

    def incluir_professor(self, professor): self.lista_professor.append(professor)
    def incluir_aluno(self, aluno): self.lista_aluno.append(aluno)

    def pesquisa_aluno_nome(self, nome_aluno):
        aux = ''
        for aluno in self.lista_aluno:
            if aluno.nome == nome_aluno:
                aux = str(aluno)
        if aux != '': print(aux)
        else: print("O Aluno não consta na listagem")
    def pesquisa_aluno_cpf(self, cpf_aluno):
        aux = 0
        for aluno in self.lista_aluno:
            if aluno.cpf == cpf_aluno:
                aux = str(aluno)
        if aux != 0: print(aux)
        else: print("O Aluno não consta na listagem")

    def pesquisa_professor_nome(self, nome_professor):
        aux = ''
        for professor in self.lista_professor:
            if professor.nome == nome_professor:
                aux = str(professor)
        if aux != '': print(aux)
        else: print("O Professor não consta na listagem")
    
    def pesquisa_professor_cpf(self, cpf_professor):
        aux = 0
        for professor in self.lista_professor:
            if professor.cpf == cpf_professor:
                aux = str(professor)
        if aux != 0: print(aux)
        else: print("O Professor não consta na listagem")

if __name__ == '__main__':
    n1 = Notas(7,8,9)
    n2 = Notas(6,5,4)
    a1 = Aluno('Davi',176,11,n1)
    a2 = Aluno('Maria', 184,12,n2)
    l = Controller()
    l.incluir_aluno(a1)
    l.incluir_aluno(a2)
