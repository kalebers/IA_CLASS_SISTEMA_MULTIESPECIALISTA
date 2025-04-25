import random
from especialista.Estudante import Estudante

class SuperEstudante(Estudante):
    ### especialize o SuperEstudante para ele retorne o menor valor de uma lista
    ### ....
    @property
    def eh_ativado(self):
        return 'minimo' in self.QuadroNegro.estadoCompartilhado['problemas']

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa('minimo')
        return ['minimo', p, '=', min(p)]

    @property
    def progresso(self):
        return random.randint(5, 15)
    ### função que implementar a contribuição do 'super estudante'.
    def contribui(self):
        # Esse especialista roda em paralelo: ignora contribuições anteriores
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)
