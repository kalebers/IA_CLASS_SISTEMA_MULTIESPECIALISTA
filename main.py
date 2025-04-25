#!/usr/bin/env python

from blackboard.QuadroNegro import QuadroNegro
from controlador.Controlador import Controlador
from geradordetarefa.GeradorDeTarefa import GeradorDeTarefa
from especialista.Aluno import Aluno
from especialista.Estudante import Estudante
from especialista.Professor import Professor
from especialista.SuperAluno import SuperAluno
from especialista.SuperEstudante import SuperEstudante

if __name__ == '__main__':

    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista( Aluno(quadro_negro) )
    quadro_negro.adicionaEspecialista( Estudante(quadro_negro) )
    quadro_negro.adicionaEspecialista( Professor(quadro_negro) )

    quadro_negro.adicionaEspecialista( SuperAluno(quadro_negro) )
    quadro_negro.adicionaEspecialista( SuperEstudante(quadro_negro) )

    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 120).loop()

    for x in contribuicoes:
        print(x)
