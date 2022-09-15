from empresa import Chefe, Comissionado

c = Chefe()
c.adicionarEmpregado('Mateus M Amaral', 'haushaisja')
c.adicionarSalario('500')
c.adicionarSalario('100.489')
c.exibirEmpregado()
c.calcularSalario()



com = Comissionado(2000, 68, 12)
com.adicionarEmpregado('Pedroooooooo', 'Rua Tal')
com.exibirEmpregado()
print(f'Salário: R${com.calcularSalario()}')



'''
    Classes
        - Explicações
        - Exemplos
        - Pesquisas

    Instância / Objetos
        - Explicações
        - Exemplos
        - Pesquisas

    Encapsulamento
        - Explicações
        - Exemplos
        - Pesquisas

    POO
        - Explicações
        - Exemplos
        - Pesquisas


'''