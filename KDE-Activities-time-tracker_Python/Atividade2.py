# CREIO QUE NÃO ESTÁ USANDO. É CÓPIA ANTERIOR DO ATIVIDADELOG.PY
# .......

import os

class Atividade:
    def Atividade(self):
        # ATIVIDADE
        LastLineAtividade = os.popen("tail -1 /home/leonardo/.local/share/utt/utt.log |grep -o Estudo")
        LastLineAtividadeSaida = LastLineAtividade.read()
        print("Dentro atividade", LastLineAtividadeSaida)
        return LastLineAtividadeSaida