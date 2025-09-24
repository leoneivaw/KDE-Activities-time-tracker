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


class Main:
    '''
# TODO PENDÊNCIAS
# BUGS aqui

QT OU GTK??? QT POIS PELO QUE EU OUVI FALAR, É MAIS FÁCIL COMPILAR PARA WINDOWS.
QT INSTALAÇÃO
https://pythonpyqt.com/how-to-install-pyqt5-in-pycharm/
melhor: https://elementztechblog.wordpress.com/2015/04/14/getting-started-with-pycharm-and-qt-4-designer/

 TODO
 Refazer todo o programa com banco de dados SQLite
    SQL no pelo aqui: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
    Procurar sql com django, pois ele mapeia as classes e cria o sql e consultas, igual hibernate.
 Esse vídeo creio dar a base para fazer a label mudar com um for. https://youtu.be/zGHgiIiFiMo

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