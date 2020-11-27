from datetime import *

before = datetime.now()

text = "merhaba codeofpython takipçileri"
print("Lütfen Yazın : {}".format(text))

if text == input(": "):
    after = datetime.now()

    speed = after - before
    seconds = speed.total_seconds()
    letter_per_second = round(len(text) / seconds, 1)

    print("Kazandın!")
    print("Yazma süreniz : {} saniye.".format(seconds))
    print("{} saniyedeki harf.".format(letter_per_second))
else:
    print("Kaybettin :( ")