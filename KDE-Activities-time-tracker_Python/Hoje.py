import os
from datetime import date
from Atividade import Atividade

class Hoje():
    def Hoje(self, ConfereData):
#        print("Data iniciada")
        today = date.today()
        hoje = str(today)

        # DATA
        # LastLineData = os.popen("tail -1 /home/leonardo/.local/share/utt/utt.log |head -c 10")
        # LastLineDataSaida = LastLineData.read()
        # print(LastLineDataSaida)

        atividade = Atividade()
        print("hoje sistema: ", hoje)
        print("Hoje log: ", atividade.QuebraLog(0))
        if hoje == atividade.QuebraLog(0):
            print("Mesma data")
            ConfereData = 1
        else:
            print("Data diferente")

        return ConfereData