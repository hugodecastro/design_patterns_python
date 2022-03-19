from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass

    @abstractmethod
    def criar_pizza(self):
        pass

class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaCamarao()

class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocoli()

    def criar_pizza(self):
        return PizzaBolonha()

class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, pizza_veg):
        pass

class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, pizza_veg):
        pass

class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

class PizzaCamarao(Pizza):

    def servir(self, pizza_veg):
        print(f'{type(self).__name__} é servida com camarão na {type(pizza_veg).__name__}')

class PizzaBrocoli(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

class PizzaBolonha(Pizza):

    def servir(self, pizza_veg):
        print(f'{type(self).__name__} é servida com bolonha na {type(pizza_veg).__name__}')


class Pizzaria:

    def fazer_pizzas(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg()
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)

pizzaria = Pizzaria()

pizzaria.fazer_pizzas()