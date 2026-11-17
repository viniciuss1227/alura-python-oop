"""
Mão na massa: refatorando uma função
Discutir no fórum
A criação de classes em Python é uma maneira poderosa de estruturar código de forma orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Livro que representa informações sobre um livro, como título, autor e número de páginas:

class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade
"""

"""
Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
"""

class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e minha profissão é {self.profissao}'
        else:
            return f'Olá, meu nome é {self.nome}, tenho {self.idade} anos!'
            

p1 = Pessoa('Vinicius', 22, 'Engenheiro de Software')
p2 = Pessoa('Hideki', 22)
print(p1.saudacao)
print(p2.saudacao)
