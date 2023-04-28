# Orientação a objeto
  #Criar Classe

from datetime import datetime

#  Pedir nome, pedir sobrenome, pedir data de nascimento

class Pessoa:
  def __init__(self):
    self.nome = input('Digite seu nome / Type your name: ')
    self.sobrenome = input('Digite seu Sobrenome / Type your last name:  ')
    self.ano_nascimento = input('Digite seu ano de nascimento / Type your birth year: ')

  def nome_completo(self):
    return f'{self.nome} {self.sobrenome}'

# Ano de nascimento - data atual

  def idade(self):
    ano_atual = datetime.now().year
    self.ano_nascimento = (ano_atual - int(self.ano_nascimento))
    return self.ano_nascimento
    

# criar objeto
pessoa1 = Pessoa()

# print:
print(Pessoa.nome_completo(pessoa1), Pessoa.idade(pessoa1))
