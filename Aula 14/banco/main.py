from conta import Conta
from cliente import Cliente

print('-' * 30)
print(' - - BANCO DOS BANCOS - - ')
print('-' * 30)

cliente1 = Cliente('Sayumi Souza', '123.654.987-1')
conta1 = Conta(cliente1, 1000)
print(conta1.titular.nome)
print(conta1.titular.cpf)

print(cliente1.nome)
print(cliente1.cpf)

print(cliente1)
print(conta1.titular)

if(conta1.sacar(500)):
    print('Saque Efetuado com sucesso')
else:
    print('Saldo insuficiente')

cliente2 = Cliente('Igor Oliveira', '987.851.753-58')
conta2 = Conta(cliente2, 1000, 3000.0)

if(not conta2.transferir(conta1, 150)):
    print('Saldo em conta insuficiente para realizar a transferência.')
else:
    print('Transferência efetuada com sucesso')

conta2.extrato()
conta1.extrato()

'''
    CRIAR UMA LOCADORA

    O Programa deve criar duas classes FILME e AUTOR

    Classe FILME
        (nome, autor, ano, tema, alugado(boolean))
        - Classe Filme deve conter a referência de um autor
        - Filme deve ter os métodos
            - Alugar Filme
            - Devolver Filme
            - O filme cs atributos (extrato/lista)
            EXIBIÇÃO
                FILME: O PODEROSO CHEFÃO
                AUTOR: COD AUTOR - NOME AUTOR
                ANO: 1992
                TEMA: TEMA
                Alugado: True / False
                
        O filme não pode ser alugado se ele já estiver alugado e nem devolvido se já estiver na loja

    Classe Autor
        (codigo, nome)
'''