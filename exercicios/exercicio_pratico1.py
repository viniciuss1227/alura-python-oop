"""
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
"""

# Respostas
# 1) Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
#    Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)

# 2) Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
#   Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria, ativo, capacidade, nota):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota = nota
         
meu_restaurante = Restaurante(
    nome = 'Vinicius Bakery',
    categoria = 'Café',
    ativo = True,
    capacidade = 25,
    nota = 9.5
)

# 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão.
# Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=15, nota=9.5):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota = nota

meu_restaurante = Restaurante(
    nome='Vinicius Bakery',
    categoria='Café',
    ativo = True,
    capacidade = 25,
    nota = 9.6
)


#4)Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria.
# Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = 25
        self.nota = 9.5

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

#5)Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor

class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

cliente1 = Cliente(
    nome = 'Vinicius',
    idade = '22',
    email = 'vinicius.matheus1227@gmail.com',
    telefone = '11952387401'
)
cliente2 = Cliente(
    nome = 'João',
    idade = '30',
    email = 'joao@email.com',
    telefone = '11987654321'
)
cliente3 = Cliente(
    nome = 'Maria',
    idade = '25',
    email = 'maria@email.com',
    telefone = '11912345678'
)

