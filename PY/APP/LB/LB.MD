def again():
    return work()

def exit():
    print('bye')

def work():
    while True:
        a = input('word ')
        if a != 'exit':
            return again()
        else:
            return exit()

again()
