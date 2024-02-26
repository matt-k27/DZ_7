print('DZ7')

originalList = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
i = 0

while i < len(originalList):
    originalList.append(originalList.pop(originalList.index(0)))
    i += 1

print(originalList)

print('Thank you for using')