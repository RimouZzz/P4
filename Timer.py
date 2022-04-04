import datetime
import keyboard
import Sound

Sound.AudioDirection()
a = datetime.datetime.now()
count = 0
array = []

while True:
    if count < 10:
        if keyboard.read_key() == "p":
            b = datetime.datetime.now()
            delta = b - a

            array.append(delta)

            count += 1
            #print(count)

    elif count == 10:
        for results in array:
            print(results)
        exit()
