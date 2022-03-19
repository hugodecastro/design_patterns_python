from abc import ABCMeta, abstractmethod

class Comando(metaclass=ABCMeta):

    def __init__(self, recv) -> None:
        self.recv = recv

    @abstractmethod
    def executar(self):
        pass


class ComandoConcreto(Comando):

    def __init__(self, recv) -> None:
        super().__init__(recv)

    def executar(self):
        self.recv.acao()

class Receiver:

    def acao(self):
        print('Ação do Receiver')

class Invoker:

    def comando(self, cmd):
        self.cmd = cmd

    def executar(self):
        self.cmd.executar()


if __name__ == '__main__':
    recv = Receiver()
    cmd = ComandoConcreto(recv)

    inv = Invoker()
    inv.comando(cmd)
    inv.executar()