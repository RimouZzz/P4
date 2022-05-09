import csv
import time

header = ['TestNr.', 'Age', 'Gender', 'Hearing', 'ReactionTime', 'SoundName', 'SoundMood', 'Precision']
timeString = time.strftime("%d%m%Y-%H%M%S")

testNum = int(input("Test nr:"))
age = int(input("Age: "))
gender = int(input("Gender: "))
if gender == 0:
    female = True
else:
    female = False
hearing = int(input("Hearing Rate: "))


class csvWriter():
    def writeHeader(self):
        with open(f'CSV files/SoundReaction{timeString}.csv', mode='w', encoding='UTF8', newline='') as data_collection:
            data_collection = csv.writer(data_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_collection.writerow(header)

    def writeData(self, testNo, age, Gender, Hearing, ReactionTime, SoundName, SoundMood, Precision):
        with open(f'CSV files/SoundReaction{timeString}.csv', mode='a', encoding='UTF8', newline='') as data_collection:
            data_collection = csv.writer(data_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = [testNo, age, Gender, Hearing, ReactionTime, SoundName, SoundMood, Precision]
            data_collection.writerow(row)
