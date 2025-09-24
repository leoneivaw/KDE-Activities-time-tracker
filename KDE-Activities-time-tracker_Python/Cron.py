import atexit
import time
import os
from Atividade import Atividade

# RODA A PRIMEIRA VEZ AJUSTANDO O LOG

class Cron:

    def ifs(self):
        # posicao define se pega a última ou penultima palavra do log.
        # se a atividade estiver fechada, pega a penultima. Atividade em aberto, pega a úlitma.
        atividade = Atividade()
        posicao = -2


        # Pode ser que essa rotina não seja necessária, tendo em vista que fecharemos cada atividade.
        if atividade.QuebraLog(-1) == "**":
            posicao = -2
        else:
            posicao = -1

            # Colocar uma rotina que salva
            # Se não mudou de atividade
        if atividade.QuebraLog(posicao) == atividade.Sistema():
                # PROTEÇÃO
                # apaga a última linha
                if atividade.QuebraLog(posicao) != "hello":
                    qualAtividade = atividade.QuebraLog(posicao)

                    atividade.removeLastLine()
                #    time.sleep(1)

                    # reinsere a última linha
                    atividade.AddAtividade(0, qualAtividade)


            # Se mudou de atividade
        print("ponto cego")
        if atividade.QuebraLog(posicao) != atividade.Sistema():
          #      print("Log e atividade Diferem")
          #      print("INICIANDO UTT")
                # FECHA ATIVIDADE DO LOG

                # Abre atividade
                atividade.AddAtividade(1, atividade.Sistema())
                # Fecha atividade
                atividade.AddAtividade(0, atividade.Sistema())

                #
                # utt1 = 'utt add "'
                # utt2 = '"'
                # utt = utt1+atividade.QuebraLog(-1)+utt2
                # print("Log alterado: ",utt)
                # os.system(utt)
                # # ABRE ATIVIDADE DO SISTEMA
                # uttA = 'utt add "'
                # uttB = ' **"'
                # uttT = uttA+atividade.Sistema()+uttB
                # print("Log alterado: ",uttT)
                # os.system(uttT)

        def Sair():

            atividade = Atividade()
        #    print("SAIR")
            if atividade.QuebraLog(-1) != "**":
                print("Log já está pronto para sair")
            else:
                uttX, uttXX = 'utt add "', '"'
                #uttXX = '"'
                uttZ = uttX + atividade.QuebraLog(-2) + uttXX
                print("Print UTT: ", uttZ)
                # Rotina executa algo ao sair
                os.system(uttZ)
                exit()
        atexit.register(Sair)
