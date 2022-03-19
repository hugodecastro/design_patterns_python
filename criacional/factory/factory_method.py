from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):

    @abstractmethod
    def __repr__(self):
        pass

class SecaoPessoal(Secao):

    def __repr__(self):
        return 'Seção Pessoal'

class SecaoAlbum(Secao):

    def __repr__(self):
        return 'Seção Album'

class SecaoProjeto(Secao):

    def __repr__(self):
        return 'Seção Projeto'

class SecaoPublicacao(Secao):

    def __repr__(self):
        return 'Seção Publicação'

class Perfil(metaclass=ABCMeta):

    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass
    
    def get_secoes(self):
        return self.secoes

    def add_sessao(self, secao):
        self.secoes.append(secao)

class LinkedIn(Perfil):

    def criar_perfil(self):
        self.add_sessao(SecaoPessoal())
        self.add_sessao(SecaoProjeto())
        self.add_sessao(SecaoPublicacao())
    
class Facebook(Perfil):

    def criar_perfil(self):
        self.add_sessao(SecaoPessoal())
        self.add_sessao(SecaoAlbum())

if __name__ == '__main__':
    rede_social = input('Qual rede social quer criar o perfil? [LinkedIn / Facebook] ')

    perfil = eval(rede_social)()

    print(f'Criando perfil no {type(perfil).__name__}')
    print(f'O perfil tem as seções {perfil.get_secoes()}')