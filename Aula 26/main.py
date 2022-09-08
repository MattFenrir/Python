from funcionario import Gerente, Vendedor
from endereco import *


est1 = Estado('Estado 1', 'SG')
cid1 = Cidade('Cidade 1', est1)
end1 = Endereco('Rua do End 1', 12, 'Bairro Nobre', '12365-789', cid1)

g = Gerente('Gerente Nome Completo', '15/02/1995', '123.654.897-74', 'Endereço Gerente')
print(g.enderecos.cidade.nome)
g.getSalario()

v = Vendedor('Vendedor Nome Completo', '05/11/1987', '144.789.652-87', 'Endereço Vendedor')
print(round(v.getSalario(), 2))
print(v.equipe)