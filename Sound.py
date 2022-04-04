import random
from playsound import playsound #Version 1.2.2
import threading


class myThread (threading.Thread):

   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print("Starting " + self.name)
      soundgobrr(self.name, 5, self.counter)
      print("Exiting " + self.name)

def AudioDirection():
    i = 0
    Sounds = [[0, 32, 'clean.wav'], [1, 43, 'Painshort.mp3'], [2, 12, 'Malescream.mp3'], [3, 45, 'test.wav']]
    while(i < 15):

        #First number = which sound 2nd = direction of sound between two speakers
        Chosensound = random.randint(0, len([Sounds]))  # Pick random sound

        Speakers = [[0, 0], [1, 45], [2, 90], [3, 135], [4, 180], [5, 225], [6, 270], [7, 315]]#First number = which speaker 2nd = degrees
        Chosenspeaker = random.randint(0, 7)#Pick random speaker

        if (Chosenspeaker == 7):
            Speaker2 = 0
        if (Chosenspeaker != 7):
            Speaker2 = Chosenspeaker +1

        print(Chosenspeaker,Speaker2)

        print("sound coming from speaker:", Speakers[Chosenspeaker][0],"and", Speakers[Speaker2][0], "With the direction of:", Speakers[Chosenspeaker][1])#Print speaker chosen, and which direction it has.
        print("Playing sound:", Sounds[Chosensound][0], "With the direction of:", Sounds[Chosensound][1])#Print which sound, and which angle the sound has.

        Finaldirection = Speakers[Chosenspeaker][1] + Sounds[Chosensound][1]
        print("The total direction is:", Finaldirection)

        #playsound(Sounds[Chosensound][2])
        input("Press Enter to continue...")
        i += 1
        print(" ")


    return Sounds, Chosensound


AudioDirection()

def soundgobrr():
    playsound(AudioDirection.Sounds[AudioDirection.Chosensound][2])

"""
        myThread.run(soundgobrr)
        Sounds.pop(Chosensound)

        # Create new threads
        thread1 = myThread(1, "Thread-1", 1)
        thread2 = myThread(2, "Thread-2", 2)

        # Start new Threads
        thread1.start()
        thread2.start()
"""

soundgobrr()