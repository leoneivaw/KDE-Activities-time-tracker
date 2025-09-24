#!/usr/bin/python3

import tkinter
from datetime import timedelta

from CountDown import *
import atexit
import os
import time
import atexit
import os
import time

# GUI QT - única coisa que funciona, é gerar o .ui via terminal.
# alias pyuic5="python3 -m PyQt5.uic.pyuic"
# pyuic5 form.ui -o form.py

from Cron import Cron
from Hoje import Hoje
from Iniciar import Iniciar
from Relogio import Relogio
from Atividade import Atividade
from CountDown import CountDown

class Gui(tkinter.Label):
    """ Class that contains the clock widget and clock refresh """
    '''
    # TODO PENDÊNCIAS
    # BUGS aqui

    QT OU GTK???
    QT INSTALAÇÃO
    https://pythonpyqt.com/how-to-install-pyqt5-in-pycharm/
    melhor: https://elementztechblog.wordpress.com/2015/04/14/getting-started-with-pycharm-and-qt-4-designer/

     TODO
    5 - Fazer rotina para evitar abrir duas instâncias. Se não achar código para isso, usar um arquivo de lock.
        Colocando um hello com uma data antiga no início do log e retirando quando o app for fechado.
        1980-07-22 21:43 hello
        Se ao abrir identificar esse hello, o programa pede para verificar outras instâncias abertas.
    6 - Rotina de proteção meia noite - Verifica hora atual e se o tempo do loop for ultrapassar meia noite.
    6.1 - Ou fecha o log, dobra o tempo de um loop para passar meia noite e executa hello já após meia noite.
    6.2 - Ou reinicia o programa ao dar meia noite.
    8 - Criar opção para abrir log
    9 - Criar opção para limpar log
    10 - Criar relatório log, para passar pro aprovado. Usar um for pegando cada linha que tiver hello e gerando o relatório de todos os dias..
                Relatórios
                utt report 2018-03-25 | grep ": Estudo$"
                utt report --from 2020-12-28 --to 2021-01-13
    10.2 - No for - Fazer o aproveitamento entre as atividades do dia. Ou seja, mostra quando em percentual cada atividade ocupou do dia.
    12 - Criar config. Tipo roda no terminal atividade -conf.
    12.1 - Abre tela com case e opção para setar cada configuração
    # TODO FUTURO
    Colocar para rodar em um widget

    Interfaces
    Obs: tkinter é nativo do python.
    https://realpython.com/python-gui-tkinter/
    https://realpython.com/pysimplegui-python/
    https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956

        '''
    #### CONFIGURAÇÕES ####
 #   segundos = 60
    notepadApp = "kate"
    logFile = "/home/leonardo/.local/share/utt/utt.log"
    mostrarAtividade = "Estudo"
    mostrarAtividadeAtual = 0
    provaPF = '2021-03-20 16:00:00'
    provaDEPEN = '2021-02-27 16:00:00'

    ########
    def __init__(self, parent=None, ciclo=False, prova=False):

        # Verifica se o log está vazio
        atividade = Atividade()
        isVazio = atividade.LogVazio()
        if isVazio == 1:
            atividade.AddAtividade(0, "hello")
        del atividade

        ConfereData = 0
        hoje = Hoje()
        resultadoData = hoje.Hoje(ConfereData)

        # Se a data for diferente da data de hoje, Insere Hello no log
        iniciar = Iniciar()
        iniciar.Hello(resultadoData)  # tratar a data no iniciar
        iniciar.IniciarLog()

        del resultadoData
        del hoje
        del iniciar




        """
        Create and place the clock widget into the parent element
        It's an ordinary Label element with two additional features.
        """
        tkinter.Label.__init__(self, parent)


        if prova:
            self.data_prova()
        self.after(200)


        if ciclo:
            self.rodar_loop()
        self.after(200)

    #### jogar esse loop para baixo
    def rodar_loop(self,loop=0, tempo=timedelta(seconds=60)):
        """ Updates the display clock every 200 milliseconds """
        atividade = Atividade()
        loop = loop+1
        textim= atividade.Sistema()
        tempo = tempo - timedelta(seconds=1)
     #   tkinter.Label(frame, text=" 999").pack()
        self.config(text=tempo)
        self.after(1000, self.rodar_loop)

    def data_prova(self):

        ########## Data prova ###########
        prova = 'PF'
        provaPF = '2021-03-20 16:00:00'
     #   prova = '(((DEPEN)))'
        provaDEPEN = '2021-02-27 16:00:00'
        countdown = CountDown()
        pr = countdown.CountDown(provaPF, prova)
        texto = pr[1]+'\n'+pr[0]
        self.config(text=texto)
        self.after(1000, self.data_prova)




if __name__ == "__main__":
    """
    Create a tkinter window and populate it with elements
    One of those elements merely happens to include the clocks.
    The clock widget can be configure()d like any other Label widget.
    Nothing special needs to be added to main(). The Clock class
      updates the widget automatically when you create the widget.
    """

    # Create window and frame

    window = tkinter.Tk()
    frame  = tkinter.Frame(window, width=400, height=400 )
    frame.pack()

    # Add the frame elements, including the clock like any other element

    tkinter.Label(frame, text="Clock with seconds:").pack()

    texto1 = Gui(frame,ciclo=True)
    texto1.pack()
    texto1.configure(bg='green',fg='yellow',font=("helvetica",35))

    tkinter.Label(frame, text=" ").pack()

    tkinter.Label(frame, text="Clock with blinking colon:").pack()

    texto2 = Gui(frame,prova=True)
    texto2.pack()
    texto2.configure(bg='red',fg='white',font=("arial",20))


    tkinter.Label(frame, text=" ").pack()
    tkinter.Label(frame, text="Have a nice day.").pack()
    window.mainloop()