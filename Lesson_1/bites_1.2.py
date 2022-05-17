# Задание №1.2

def get_bites(data):
    data_bites = eval(f'b"{data}"')
    print(data_bites)
    print(type(data_bites))
    print(len(data_bites))

get_bites('class')
get_bites('function')
get_bites('method')