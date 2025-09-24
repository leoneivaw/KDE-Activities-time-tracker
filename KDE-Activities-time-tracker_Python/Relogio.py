import os
from datetime import datetime, timedelta
from sys import stdout
from time import sleep
from colorama import Fore, Back, Style
from Atividade import Atividade

class Relogio:
    def Relogio(self, segundos, loop):
        # https://github.com/tartley/colorama
        # from colorama import Fore, Back, Style
        # print(Fore.RED + 'some red text')
        # print(Back.GREEN + 'and with a green background')
        # print(Style.DIM + 'and in dim text')
        # print(Style.RESET_ALL)
        # print('back to normal now')
        tempo = timedelta(seconds=segundos)
        atividade = Atividade()
        if atividade.Sistema() != "Estudo":
            msg = '///Não estudando///'
            print(Style.BRIGHT+Fore.LIGHTMAGENTA_EX+msg+Style.RESET_ALL)
        tempoAtividade = os.popen("utt report | grep ': "+atividade.Sistema()+"$'")
        output = tempoAtividade.read()
        print(Style.BRIGHT+Fore.RED+output,end=''+Style.RESET_ALL)
        tempoAtividade = os.popen("utt report | grep ': Estudo$'")
        output = tempoAtividade.read()
        print(Style.BRIGHT+Fore.GREEN+output,end=''+Style.RESET_ALL)

        print(tempo, " no loop: ", loop)

        while (str(tempo) != '0:00:00'):
            stdout.write("\r%s"%tempo)
            stdout.flush()
            tempo = tempo - timedelta(seconds=1)
            sleep(1)

            stdout.write("\r0:00:00")
            stdout.flush()

            print('\a', end='') # => sinal sonoro , pelo menos comigo funcionou '-'