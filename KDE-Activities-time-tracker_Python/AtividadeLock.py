import os

from Atividade import Atividade

class Lock:
    def Lock(self):
        atividade = Atividade()
        if atividade.QuebraLog(-1) == "**":
            # TODO PEGAR HORÁRIO E COMPARAR
            # Pega a última e penultima linha e compara se são iguais em atividade, uma aberta e outra fechada.
            # Se if de cima for true, Substitui a última linha com hora do laço atual.
            atividade.QuebraLog()
            utt1, utt2, = 'utt add "', '"'
            utt = utt1 + atividade.QuebraLog(-2) + utt2
            print("Print UTT: ", utt)
            # Rotina executa algo ao sair
            os.system(utt)
