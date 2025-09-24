import os
from Atividade import Atividade

class Iniciar:
    def Hello(self, ResultadoData):
        print("hello", ResultadoData)
        if ResultadoData == 0:
            qualAtividade = "hello"
            atividade = Atividade()
            atividade.AddAtividade(0, qualAtividade)

    def IniciarLog(self):
        # Importante para não  continuar uma atividade que já foi fechada horas atrás.

#        if atividade.QuebraLog(-1) != "**" or atividade.QuebraLog(-1) == "hello":

        atividade = Atividade()
        print("iniciar log")
        qualAtividade = atividade.Sistema()
        atividade.AddAtividade(1, qualAtividade)
        atividade.AddAtividade(0, qualAtividade)
        print("...Log iniciado...")