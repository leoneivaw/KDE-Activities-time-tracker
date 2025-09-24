import os

class Atividade:
    def Log(self):
        with open('/home/leonardo/.local/share/utt/utt.log') as f:
            ln = 0 # Última linha
            for line in f:
                ln=ln+1
                pass
            logLinha = line

        #    print(ln, line)
        # TODO TERMINAR ESSA ROTINA DE COMPARAR LINHA E PROTEGER
        # BUG QUANDO PENULTIMA LINHA É HELLO E ÚLTIMA ATIVIDADE
        # Leu penultima linha
        ff = open('/home/leonardo/.local/share/utt/utt.log')
        lines = ff.readlines()
#        ultima = lines[ln-1]
#        penultima = lines [ln-2]
#        print("Última linha", ln, ultima)
#        print("Penúltma linha", ln-1, penultima)
        f.close()
        ff.close()
        return logLinha


    def QuebraLog(self, posicao):
        log = self.Log()

        # quebra a string em palabras
        quebrarLog = log.split()

        return quebrarLog[posicao]

    def LogVazio(self):
        caminho = '/home/leonardo/.local/share/utt/utt.log'
        vazio = 0
        # check if size of file is 0
        if os.stat(caminho).st_size == 0:
            print('Arquivo vazio')
            vazio = 1
        else:
            print('Arquivo não vazio')
            vazio = 0
        return vazio

    def Sistema(self):
        os.system(
            "qdbus org.kde.ActivityManager /ActivityManager/Activities ActivityName `qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity`")
        atividadeSys = os.popen(
            "qdbus org.kde.ActivityManager /ActivityManager/Activities ActivityName `qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity`")
        # Lê saida shell
        output = atividadeSys.read()
     #   output
        Atividade = output.replace('\r', '').replace('\n', '')
        return Atividade

    def removeLastLine(self):
        # remove last line from a text line in python
        fd = open("/home/leonardo/.local/share/utt/utt.log", "r")
        d = fd.read()
        fd.close()
        m = d.split("\n")
        s = "\n".join(m[:-2])
        fd = open("/home/leonardo/.local/share/utt/utt.log", "w+")
        for i in range(len(s)):
            fd.write(s[i])
        fd.close()

    def AddAtividade(self, acao, qualAtividade):
        # AÇÃO 1 ABRE A ATIVIDADE
        # AÇÃO ELSE FECHA
        uttA = 'utt add "'
        if acao == 1:
            uttB = ' **"'
        else:
            uttB = '"'
        uttT = uttA + qualAtividade + uttB
  #      print("Atividade adicionada: ", uttT)
        os.system(uttT)