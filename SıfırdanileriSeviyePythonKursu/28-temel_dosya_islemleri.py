# batarya bilgileri : /sys/class/power_supply/BAT1

dosya = open("/sys/class/power_supply/BAT1/capacity")
kayıt = dosya.read()

dosya.close()

print(kayıt)