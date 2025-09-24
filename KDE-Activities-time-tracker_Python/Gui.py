#!/usr/bin/python3

import tkinter
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
"""
Example tkinter Clock widget, counting seconds and minutes in realtime.
Functions just like a Label widget.
The Clock class has three functions:
__init__ creates the clock widget, which is just an ordinary label.
The tick() function rewrites the label every 200 milliseconds (5 times 
  each minute) to the current time. This updates the seconds.
The blink_colon() function rewrites the label every second, making the
  colon appear to blink every second.
The secret sauce is tkinter's .after command. When a function completes,
the .after command triggers another (or the same) function to run after
a specified delay. __init__ triggers tick(), then tick() keeps triggering
itself until stopped.
All that complexity is hidden from you. Simply treat the clock as another
label widget with a funny name. *It should automatically work.*
How to add the clock widget:
    tkinter.Label(parent, text="Foo").pack()      # A widget
    Clock(parent).widget.pack()                   # Just another widget 
    tkinter.Label(parent, text="Bar").pack()      # Yet another widget
How to start/stop the clock widget:
    You don't.
    If you create a Clock().widget, the clock will start.
    If you destroy the widget, the clock will also be destroyed.
    To hide/restore the clock, use .pack_forget() and re-.pack().
    The clock will keep running while hidden.
"""
class Main:
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
    segundos = 60
    notepadApp = "kate"
    logFile= "/home/leonardo/.local/share/utt/utt.log"
    mostrarAtividade = "Estudo"
    mostrarAtividadeAtual = 0
    provaPF = '2021-03-20 16:00:00'
    provaDEPEN = '2021-02-27 16:00:00'
    ########
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
    iniciar.Hello(resultadoData) # tratar a data no iniciar
    iniciar.IniciarLog()
    # Matando os objetos
    countdown = CountDown()
    # Chama duas vezes para reforçar
    # Chama duas vezes para reforçar
    prova = 'PF'
    countdown.CountDown(provaPF, prova)
    countdown.CountDown(provaPF, prova)
    prova = '(((DEPEN)))'
    countdown.CountDown(provaDEPEN, prova)


    cron = Cron()

    del countdown
    del resultadoData
    del hoje
    del iniciar

    # Executa sair ao terminar o programa com CTRL+C
    loop = 0
    while 1:
        countdown = CountDown()
        # Chama duas vezes para reforçar
        prova = 'PF'
        cor = "Fore.GREEN"
        countdown.CountDown(provaPF, prova)
        countdown.CountDown(provaPF, prova)
        prova = '(((DEPEN)))'
        cor = 'Fore.RED'
        countdown.CountDown(provaDEPEN, prova)
        cron = Cron()
        if loop != 0:
            cron.ifs()
        loop = loop+1
        relogio = Relogio()
        relogio.Relogio(segundos,loop)
    #    time.sleep(60)
        del cron
        os.system("clear")
        # IMPRIME HORAS
        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        print(time_string)

class Clock(tkinter.Label):
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent=None, seconds=True, colon=False):
        """
        Create and place the clock widget into the parent element
        It's an ordinary Label element with two additional features.
        """
        tkinter.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%H:%M:%S')
        else:
            self.time     = time.strftime('%I:%M %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        if self.display_seconds:
            new_time = time.strftime('%H:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


    def blink_colon(self):
        """ Blink the colon every second """
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)



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

    clock1 = Clock(frame)
    clock1.pack()
    clock1.configure(bg='green',fg='yellow',font=("helvetica",35))

    tkinter.Label(frame, text=" ").pack()

    tkinter.Label(frame, text="Clock with blinking colon:").pack()

    clock2 = Clock(frame, seconds=False, colon=True)
    clock2.pack()
    clock2.configure(bg='red',fg='white',font=("arial",20))

    tkinter.Label(frame, text=" ").pack()

    tkinter.Label(frame, text="Have a nice day.").pack()

    window.mainloop()