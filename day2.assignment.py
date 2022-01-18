name = 'Piush'

age = 17
i = 0

marks = 99.0

item_list = ['Shampoo' , 'Conditioner', 'Noodles']
item_list.append('Spices')

items_price = {}
items_price['Shampoo'] = 250
items_price['Conditioner'] = 150
items_price['Noodles'] = 350

tuple_1 = (0, 1, 2, 3, 4, 5, 6)

set_1 = {0, 1, 2, 3, 4, 5}

print('My name is ' + name + ' I am ' , age , ' years old and i got ' , marks , ' in Maths')
print('My name is %s I am %s years old and i got %s in Maths'%(name, age, marks))
print('My name is {} I am {} years old and i got {} in Maths'.format(name, age, marks))
print(f'My name is {name} I am {age} years old and i got {marks} in Maths')

for each_item in item_list:
    print(f'Item: {each_item}')

for key, value in items_price.items():
    print(f'Item: {key} - Price: {value}')

for i in tuple_1:
    print(f'Items in tuple: {tuple_1[i]}')