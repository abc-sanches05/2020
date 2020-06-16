
def ask():
    
    while True:
        try:
            n= int(input('Введите число '))
        except:
            print('Произошла ошибка! Попробуйте снова!')
            continue
        else:
            m = n*n
            print(f'Спасибо! Квадрат числа {n}:{m}')
            break
        
ask()        

