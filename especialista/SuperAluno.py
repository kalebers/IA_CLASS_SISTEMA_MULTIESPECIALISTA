import random
from especialista.Aluno import Aluno

class SuperAluno(Aluno):
    ### especialize o SuperAluno para ele retorne o maior valor de uma lista
    ### ....
    @property
    def eh_ativado(self):
        return 'maximo' in self.QuadroNegro.estadoCompartilhado['problemas']

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa('maximo')
        return ['maximo', p, '=', max(p)]

    @property
    def progresso(self):
        return random.randint(5, 15)

    def contribui(self):
        # Lê contribuições anteriores
        contribs = self.QuadroNegro.pegaContribuicoes()

        # Só contribui se já houver uma soma feita por um Aluno (sequencial)
        if any(c[0] == 'Aluno' and c[1][0] == 'soma' for c in contribs):
            self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
            self.QuadroNegro.atualizaProgresso(self.progresso)
