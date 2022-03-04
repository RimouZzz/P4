import datetime
import keyboard

a = datetime.datetime.now()
count = 0
array = []

while True:
    if count < 5:
        if keyboard.read_key() == "p":
            b = datetime.datetime.now()
            delta = b - a

            array.append(delta)

            count += 1
            #print(count)

    elif count == 5:
        for results in array:
            print(results)
        exit()