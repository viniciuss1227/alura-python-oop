# ==========================================
# 1. DEFINIÇÃO DAS CLASSES
# ==========================================

class ContaBancaria:
    """Versão inicial (Desafios 1 a 3)."""
    def __init__(self, titular, saldo, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo

    def __str__(self):
        return f'Titular: {self.titular} - Saldo: R${self.saldo:.2f}'

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True


class ContaBancariaPythonica:
    """Versão refatorada com atributos protegidos e @property (Desafios 4 e 5)."""
    def __init__(self, titular, saldo, ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f'Titular: {self._titular} - Saldo: R${self._saldo:.2f}'

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def ativar_conta(self):
        self._ativo = True


class ClienteBanco:
    """Modelo de cliente e fábrica de contas (Desafios 6 e 7)."""
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        return ContaBancariaPythonica(titular, saldo_inicial)

# ==========================================
# 2. EXECUÇÃO E TESTES DOS DESAFIOS
# ==========================================

conta1 = ContaBancaria('Vinicius', 500.00)
conta2 = ContaBancaria('Hideki', 1000.00)
print(conta1)
print(conta2)

ContaBancaria.ativar_conta(conta1)
print(f'Conta 1 ativa? {conta1.ativo}\n')

conta3 = ContaBancariaPythonica('Alice', 1500.00)
print(f'Titular da conta 3: {conta3.titular}\n')

cliente1 = ClienteBanco('Vinicius', 22, 'São Paulo', '50525223432', 'Engenheiro de Software')
conta_cliente1 = ClienteBanco.criar_conta(cliente1.nome, 2000.00)
print(f'Conta de {conta_cliente1.titular} | Saldo inicial: R${conta_cliente1.saldo:.2f}')