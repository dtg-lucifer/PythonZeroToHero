items = []

for i in range(5):
    item = input(f'Enter the value of item no. {i + 1}: ')
    items.insert(i, item)

for eachIndex, eachItem in enumerate(items):
    print(f'The item no. {eachIndex + 1} is : {eachItem}')