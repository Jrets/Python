#1.2
sekinput = int(input("Укажите количество секунд "))
chas = sekinput // 60 // 60
min = (sekinput - chas * 60 * 60) // 60
sekund = sekinput - chas*60*60 - min*60
print("{:02d}".format(chas), ":", "{:02d}".format(min), ":", "{:02d}".format(sekund))





