def function_1(items):
    for eachIndex, eachItem in enumerate(list_1):
        print(f'Item number {eachIndex + 1} is : {eachItem}')

    print('\n')

def function_2(item_dict):
    for key, value in item_dict.items():
        print(f'Key: {key} | Value: {value}')
    
    print('\n')

def function_3(a, b):
    output_list = list()
    output_list.append(a)
    output_list.append(b)
    return  output_list





list_1 = [1, 2, 3, 4, 'Strign', 'Python', 34.78, 99.99, [1, 2, 3, 4, 5], (1, 2, 3, 4, 5), {'A': 'a', 'B': 'b'}]
list_2 = {'Name': 'Piush', 'Age': 17, 'ProgrammingLanguage': 'Python', 'Country': 'India'}


function_1(list_1)
function_2(list_2)
print(function_3(1, 2))