import os


class AtividadeLog:
    def AtividadeLog(self):
        with open('/home/leonardo/.local/share/utt/utt.log') as f:
            for line in f:
                pass
            LastLineAtividadeSaida = str(line)
        return LastLineAtividadeSaida
