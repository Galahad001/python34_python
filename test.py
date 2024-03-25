
'''При путешествии по планете марсоход постоянно замеряет высоту рельефа и сохраняет результаты замеров в массив.

Одна из задач марсохода — поиск «правильных гор». «Правильной» считается та гора, у которой на пути от подножия до вершины высота постоянно растёт, а на пути от вершины к подножию — постоянно уменьшается. Если у горы есть несколько вершин или в каком-то месте встречается горизонтальный участок — это «неправильная гора».

Напишите функцию valid_mountain_array, которая будет принимать на вход массив с высотами и возвращать True или False в зависимости от того, «правильная» это гора или нет.

Если в массиве менее трёх элементов, такой массив не может описывать «правильную» гору.'''


def valid_mountain_array(spis):
    if len(spis) < 3:
        return False
    for index, el in enumerate(spis):
        spis[index] = int(el)

    max_el = max(spis)
    max_index = spis.index(max_el)
    
    for i in range(len(spis)-1):
        if spis[i] == spis[i+1]:
            return False
        
    for i in range(max_index):
        if spis[i] < spis[i + 1]:
            return True
        else:
            return False

    for i in range(max_index, len(spis)-1):
        if spis[i] > spis[i + 1]:
            return True
        else:
            return False
                   


test = input().split()
print(valid_mountain_array(test))




# def valid_mountain_array():
#     elements_data = input().split()
#     for element_index, element in enumerate(elements_data):
#         elements_data[element_index] = int(element)
#     max_element = max(elements_data)
#     index_max = elements_data.index(max_element)
#     last_index = len(elements_data) - 1
#     # print(f'Last index is {last_index}')
#     # print('Индекс максимального элемента =', index_max)
#     # print('Максимальный элемент =', max_element)
#     if index_max == 0 or index_max == len(elements_data) - 1 or len(elements_data) <= 2:
#         # print('one of endpoints max or small array')
#         result = False
#     else:
#         for i in range(last_index):
#             if elements_data[i] == elements_data[i+1]:
#                 result = False
#         for i in range(index_max):
#             if elements_data[i] < elements_data[i+1]:
#                 result = True
#             else:
#                 result = False
#         for i in range(index_max, last_index):
#             if elements_data[i] > elements_data[i + 1]:
#                 result = True
#             else:
#                 result = False
#     print(result)


# valid_mountain_array()
