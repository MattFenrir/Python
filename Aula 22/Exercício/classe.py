class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    def listar(self):
        print(f'Nome: {self.__nome}')

class Aluno(Pessoa):
    def __init__(self, nome, ano_nascimento, ano_escolar):
        super().__init__(nome)
        self.__ano_nascimento = ano_nascimento
        self.__ano_escolar = ano_escolar

    def listar_aluno(self):
        super().listar()
        print(f'Idade: {self.idade_aluno()}')
        print(f'Ano: {self.__ano_escolar}')

    def alterar_ano_escolar(self, valor):
        self.__ano_escolar = valor

    def idade_aluno(self):
        return (2022 - self.__ano_nascimento) 

    
class Professor(Pessoa):
    __materias = ['Matemática', 'Português', 'História', 'Química', 'Física', 'Geografia' ]
    def __init__(self, nome, cpf, materia):
        super().__init__(nome) 
        self.__cpf = cpf 
        self.__materia = materia

    def listar_professor(self):
        super().listar()
        print(f'    CPF: {self.__cpf}')
        print(f'MATÉRIA: {self.__materias[self.__materia]}')

'''
class Pessoa:
    def __init__(self, _nome):
        self.__nome = _nome

    def listar_pessoa(self):
        print('____' * 5)
        print(f' NOME: {self.__nome}')

class Materia:
    __materias = ["Matemática", "Português", "História", "Química", "Física", "Geografia"]
    def __init__(self, materia):
        self.__materia = materia
    
    def pegarMateria(self):
        return self.__materias[self.__materia]
        
class Professor(Pessoa):
    def __init__(self, nome, cpf, materia):
        super().__init__(nome)
        self.__cpf = cpf
        self.__materia = materia

    def pegarMateria(self):
        materia = Materia(self.__materia)
        return materia.pegarMateria()

    def listar_pessoa(self):
        super().listar_pessoa()
        print(f' CPF: {self.__cpf}')
        print(f' MATÉRIA: {p.pegarMateria()}')
        print('____' * 5)

p = Professor('João', '12345678', 0)
p.listar_pessoa()

class Aluno(Pessoa):
    def __init__(self, nome, ano_nascimento, idade_aluno):
        super().__init__(nome)
        self.__ano = ano_nascimento
        self.__idade = idade_aluno

    def listar_pessoa(self):
        super().listar_pessoa()
        print(f' ANO DE NASCIMENTO: {self.__ano}')
        print(f' IDADE: {self.__idade}')
        print('____' * 5)

    def alterar_ano_escolar(self, valor):
        self.__ano = valor

    def idade_aluno(self, valor):
        self.__idade = valor

a = Aluno('Pedro', 2000, 22)
a.listar_pessoa()
'''