import csv
import time

header = ['Sound name', 'Mood']
timeString = time.strftime("%d%m%Y-%H%M%S")

class csvWriter():

    def writeHeader(self):
        with open(f'CSV files/soundMoods{timeString}.csv', mode='w', encoding='UTF8', newline='') as data_collection:
            data_collection = csv.writer(data_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_collection.writerow(header)

    def writeData(self, soundname, mood):
        with open(f'CSV files/soundMoods{timeString}.csv', mode='a', encoding='UTF8', newline='') as data_collection:
            data_collection = csv.writer(data_collection, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = [soundname, mood]
            data_collection.writerow(row)
