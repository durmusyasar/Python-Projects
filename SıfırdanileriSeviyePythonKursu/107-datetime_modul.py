from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")

print(datetime.now())

suan = datetime.now()
print(suan.year)
print(suan.month)
print(suan.hour) 

print(datetime.ctime(suan))

print(datetime.strftime(suan, "%Y"))
print(datetime.strftime(suan, "%M"))
print(datetime.strftime(suan, "%B"))
print(datetime.strftime(suan, "%Y %B %A"))

saniye = datetime.timestamp(suan)
print(saniye)

suan2 = datetime.fromtimestamp(saniye)
print(suan2)

suan3 = datetime.fromtimestamp(0)
print(suan3)

tarih = datetime(2019,12,1)
su_an = datetime.now()
print(tarih - su_an)