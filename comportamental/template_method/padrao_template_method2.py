from abc import ABCMeta, abstractmethod

class Abstrata(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def operacao1(self):
        pass

    @abstractmethod
    def operacao2(self):
        pass

    def template_method(self):
        print('Definindo o algoritmo: Operação 1 após Operação 2')
        self.operacao2()
        self.operacao1()


class Concreta(Abstrata):

    def operacao1(self):
        print('Minha operação concreta 1')

    def operacao2(self):
        print('Minha operação concreta 2')


class Cliente:

    def main(self):
        self.concreta = Concreta()
        self.concreta.template_method()


cliente = Cliente()
cliente.main()