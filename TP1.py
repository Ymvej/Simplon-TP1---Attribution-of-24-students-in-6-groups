# init
import csv
import random
import os

cwd = os.getcwd()
writepath = cwd + '/AttributionOutput.csv'
line_count = 0
listTemp = []
listNom = []
listPrenom = []
listId = []

# parses csv in current directory and attributes a unique ID to each row and input all of this into a list
with open(cwd + '/liste_apprenants-devdataia_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}. Attributing a unique ID to each row.')
            line_count += 1
        else:
            listTemp.append(str(line_count - 1))
            listTemp.append(row[0])
            listTemp.append(row[1])
            line_count += 1

# splits the list into 3 indexed lists
listId = listTemp[0:len(listTemp):3]
listPrenom = listTemp[1:len(listTemp):3]
listNom = listTemp[2:len(listTemp):3]

print('Parsing done.', line_count, 'IDs have been attributed.')

print('Starting groups attribution...')

# randomly attributes 4 people to 6 groups, prints its output and writes it to a string in csv format
groupNumber = 1
csvOutput = ''
while groupNumber < 7:

    currentGroupId = []
    currentGroupNom = []
    currentGroupPrenom = []
    count = 0
    currentRand = 0
    while count < 4:
        currentRand = random.randrange(0, len(listId))
        currentGroupId.append(listId[currentRand])
        currentGroupPrenom.append(listPrenom[currentRand])
        currentGroupNom.append(listNom[currentRand])
        del listId[currentRand]
        del listPrenom[currentRand]
        del listNom[currentRand]
        count += 1
    csvOutput = csvOutput + 'Groupe {}, {} {}, {} {}, {} {}, {} {}\n'.format(groupNumber, currentGroupNom[0], currentGroupPrenom[0], currentGroupNom[1], currentGroupPrenom[1], currentGroupNom[2], currentGroupPrenom[2], currentGroupNom[3], currentGroupPrenom[3])
    print('Group', groupNumber, ' is ', currentGroupNom[0], currentGroupPrenom[0], ', ', currentGroupNom[1], currentGroupPrenom[1], ', ', currentGroupNom[2], currentGroupPrenom[2], ' and ', currentGroupNom[3], currentGroupPrenom[3])
    groupNumber += 1

# creates a file named AttributionOutput.csv in the current directory and writes it with the string in csv format
mode = 'a' if os.path.exists(writepath) else 'w'
with open(writepath, mode) as f:
    f.write(csvOutput)


print('CSV exported to', writepath)
print('Attribution over. You can close this terminal.')
