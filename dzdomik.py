import csv  
 
class Home: 
    def __init__(self, numb_floors: int,  hight: int, lenght: int, name:str): 
        self.numb_floors = numb_floors 
        self.hight = hight  
        self.length = lenght 
        self.name = name  
 
 
def dom(): 
    print('Введите 0, чтобы создать домик или 1, чтобы посмотреть дома') 
    k = input() 
 
    if k == '0': 
        print('Введите количество этажей в вашем домике: ', end='') 
        floors = input() 
        print('Введите высоту вашего домика: ', end='') 
        height = input() 
        print('Введите длину вашего домика: ', end='') 
        length = input() 
        print('Введите имя домика: ', end='') 
        name= input() 
 
        
        if floors.isdigit() and height.isdigit() and length.isdigit(): 
            if int(floors) > 0 and int(height) > 0 and int(length) > 0: 
                domik = Home(floors, height, length, name) 
                with open ('bildings', 'a', newline='') as file: 
                    csv_out = csv.writer(file) 
                    csv_out.writerow([domik.numb_floors, domik.hight, domik.length, domik.name]) 
                print('Вы создали домик!') 
            else: 
                print( 'Эххх тыыы, математик. Высота, ширина и кол-во этажей должны быть больше 0!') 
        else: 
            print(' Ну чтож такое, число нужно вводить. Высота, ширина и кол-ва этажей должны быть числами!') 
    elif k == '1': 
            with open('bildings', 'rt') as file: 
                csv_reader = csv.reader(file) 
                for line in csv_reader: 
                    # home 
                    print(f'Название домика: {line[3]}\nКоличество этажей: {line[0]}\nВысота домика: {line[1]}\nШирина домика: {line[2]}\n') 
dom()
