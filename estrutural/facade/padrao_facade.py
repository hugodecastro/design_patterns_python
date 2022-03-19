
class GerenciamentoEventos:

    def __init__(self) -> None:
        print('GerenciamentoEventos: Vou organizar com todo mundo!\n\n')

    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()


class SalaoFestas:
    
    def __init__(self) -> None:
        print('SalaoFestas: Agendando o salão de festas para o casamento...')

    def esta_disponivel(self) -> bool:
        print('Salão disponivel')
        return True

    def agendar(self) -> str:
        if self.esta_disponivel:
            print('Agendamento feito com sucesso!')

class Florista:
    
    def __init__(self) -> None:
        print('Florista: Flores para um evento')

    def arranjar_flores(self) -> str:
        print('Rosas, Margaridas e Lírios \n')

class Restaurante:
    
    def __init__(self) -> None:
        print('Restaurante: Comida para eventos...')

    def preparar(self) -> None:
        print('Comida japonesa e brasileira serão servidas...\n')

class Banda:
    
    def __init__(self) -> None:
        print('Banda: Arranjos musicais para o evento...')

    def montar_palco(self) -> str:
        print('Preparando o palco para tocar jazz e rock no evento... \n')

class Cliente:

    def __init__(self) -> None:
        print('Cliente: Uau! Preparação para o casamento!')

    def contrata_gerente_eventos(self) -> None:
        
        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Cliente: Foi muito simples organizar esse evento com o Façade...')

if __name__ == '__main__':

    cliente = Cliente()
    cliente.contrata_gerente_eventos()