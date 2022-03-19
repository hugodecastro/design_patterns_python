

class Instalador:

    def __init__(self, fonte, destino) -> None:
        self.opcoes = []
        self.fonte = fonte
        self.destino = destino

    def preferencias(self, escolha):
        self.opcoes.append(escolha)

    def executar(self):
        for opcao in self.opcoes:
            if list(opcao.values())[0]:
                print(f'Copiando os binários de {self.fonte} para {self.destino}')
            else:
                print('Operação finalizada')

if __name__ == '__main__':

    instalador = Instalador('python3.9.1.gzip', '/usr/bin')

    instalador.preferencias({'python': True})
    instalador.preferencias({'java': False})

    instalador.executar()