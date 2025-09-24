from datetime import datetime, time
from time import sleep
from colorama import Fore, Back, Style

class CountDown:
        def CountDown(self, data, prova):
            def dateDiffInSeconds(date1, date2):
                timedelta = date2 - date1
                return timedelta.days * 24 * 3600 + timedelta.seconds

            def daysHoursMinutesSecondsFromSeconds(seconds):
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                days, hours = divmod(hours, 24)
                return (days, hours, minutes, seconds)

            req = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
            now = datetime.now()
            msg = 'DIAS PARA A PROVA '+prova+''
        #    print(Style.BRIGHT+Fore.GREEN+msg+Style.RESET_ALL)
        #    print(Style.BRIGHT+Fore.GREEN+"%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req))+Style.RESET_ALL)
            contador = "%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req))
            return  contador, msg

            # while req>now:
            #     print("%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req)))
            #     sleep(1)
            #     now = datetime.now()
            #
            # print("Done")