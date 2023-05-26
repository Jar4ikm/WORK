from random import randint

board = []
board1 = []
#создатие поля
for x in range(0, 10):
    board.append(["O"] * 10)
#создание поля игрока
for x in range(0, 10):
    board1.append(["O"] * 10)

#вывод поля игрока
def board_display1(board1):
    for row in board1:
        print(" ".join(row))
black_array = []
def black_list(obj):
    global black_array
    if isinstance(obj, Ship3):
        if obj.dir == 1:
            rm, cm = obj.row1 - 1, obj.col1 - 1
            rp, cp = obj.row1 + 1, obj.col1 + 1
            rm2, cm2 = obj.row1 - 1, obj.col2 - 1
            rp2, cp2 = obj.row1 + 1, obj.col2 + 1
            rm3, cm3 = obj.row1 - 1, obj.col3 - 1
            rp3, cp3 = obj.row1 + 1, obj.col3 + 1
            black_array.extend([(rm,cm),(rm,obj.col1),(rm,cp),(obj.row1,cm),(obj.row1,cp),(rp,cm),(rp, obj.col1),(rp,cp)])
            black_array.extend([(rm2,cm2),(rm2,obj.col2),(rm2,cp2),(obj.row1,cm2),(obj.row1,cp2),(rp2,cm2),(rp2, obj.col2),(rp2,cp2)])
            black_array.extend([(rm3,cm3),(rm3,obj.col3),(rm3,cp3),(obj.row1,cm3),(obj.row1,cp3),(rp3,cm3),(rp3, obj.col3),(rp3,cp3)])
        else:
            rm, cm = obj.row1 - 1, obj.col1 - 1
            rp, cp = obj.row1 + 1, obj.col1 + 1
            rm2, cm2 = obj.row2 - 1, obj.col1 - 1
            rp2, cp2 = obj.row2 + 1, obj.col1 + 1
            rm3, cm3 = obj.row3 - 1, obj.col1 - 1
            rp3, cp3 = obj.row3 + 1, obj.col1 + 1
            black_array.extend([(rm,cm),(rm,obj.col1),(rm,cp),(obj.row1,cm),(obj.row1,cp),(rp,cm),(rp, obj.col1),(rp,cp)])
            black_array.extend([(rm2,cm2),(rm2,obj.col1),(rm2,cp2),(obj.row2,cm2),(obj.row2,cp2),(rp2,cm2),(rp2, obj.col1),(rp2,cp2)])
            black_array.extend([(rm3,cm3),(rm3,obj.col1),(rm3,cp3),(obj.row3,cm3),(obj.row3,cp3),(rp3,cm3),(rp3, obj.col1),(rp3,cp3)])
    
    
    if isinstance(obj, Ship2):
        if obj.dir == 1:
            rm, cm = obj.row1 - 1, obj.col1 - 1
            rp, cp = obj.row1 + 1, obj.col1 + 1
            rm2, cm2 = obj.row1 - 1, obj.col2 - 1
            rp2, cp2 = obj.row1 + 1, obj.col2 + 1
            black_array.extend([(rm,cm),(rm,obj.col1),(rm,cp),(obj.row1,cm),(obj.row1,cp),(rp,cm),(rp, obj.col1),(rp,cp)])
            black_array.extend([(rm2,cm2),(rm2,obj.col2),(rm2,cp2),(obj.row1,cm2),(obj.row1,cp2),(rp2,cm2),(rp2, obj.col2),(rp2,cp2)])
            
        else:
            rm, cm = obj.row1 - 1, obj.col1 - 1
            rp, cp = obj.row1 + 1, obj.col1 + 1
            rm2, cm2 = obj.row2 - 1, obj.col1 - 1
            rp2, cp2 = obj.row2 + 1, obj.col1 + 1
            black_array.extend([(rm,cm),(rm,obj.col1),(rm,cp),(obj.row1,cm),(obj.row1,cp),(rp,cm),(rp, obj.col1),(rp,cp)])
            black_array.extend([(rm2,cm2),(rm2,obj.col1),(rm2,cp2),(obj.row2,cm2),(obj.row2,cp2),(rp2,cm2),(rp2, obj.col1),(rp2,cp2)])
    
    if isinstance(obj, Ship):
        rm, cm = obj.row - 1, obj.col - 1
        rp, cp = obj.row + 1, obj.col + 1
        black_array.extend([(rm,cm),(rm,obj.col),(rm,cp),(obj.row,cm),(obj.row,cp),(rp,cm),(rp, obj.col),(rp,cp)])









black_arrayb = []            
def black_list_bot(obj):
    global black_arrayb
    if isinstance(obj, Shipb3):
        if obj.dir == 1:
            rm, cm = obj.row1 - 1, obj.col1 - 1
            rp, cp = obj.row1 + 1, obj.col1 + 1
            rm2, cm2 = obj.row1 - 1, obj.col2 - 1
            rp2, cp2 = obj.row1 + 1, obj.col2 + 1
            rm3, cm3 = obj.row1 - 1, obj.col3 - 1
            rp3, cp3 = obj.row1 + 1, obj.col3 + 1
            black_arrayb.extend([(rm,cm),(rm,obj.col1),(rm,cp),(obj.row1,cm),(obj.row1,cp),(rp,cm),(rp, obj.col1),(rp,cp)])
            black_arrayb.extend([(rm2,cm2),(rm2,obj.col2),(rm2,cp2),(obj.row1,cm2),(obj.row1,cp2),(rp2,cm2),(rp2, obj.col2),(rp2,cp2)])
            black_arrayb.extend([(rm3,cm3),(rm3,obj.col3),(rm3,cp3),(obj.row1,cm3),(obj.row1,cp3),(rp3,cm3),(rp3, obj.col3),(rp3,cp3)])
        else:
            rm, cm = obj.row1 - 1, obj.col1 - 1
            rp, cp = obj.row1 + 1, obj.col1 + 1
            rm2, cm2 = obj.row2 - 1, obj.col1 - 1
            rp2, cp2 = obj.row2 + 1, obj.col1 + 1
            rm3, cm3 = obj.row3 - 1, obj.col1 - 1
            rp3, cp3 = obj.row3 + 1, obj.col1 + 1
            black_arrayb.extend([(rm,cm),(rm,obj.col1),(rm,cp),(obj.row1,cm),(obj.row1,cp),(rp,cm),(rp, obj.col1),(rp,cp)])
            black_arrayb.extend([(rm2,cm2),(rm2,obj.col1),(rm2,cp2),(obj.row2,cm2),(obj.row2,cp2),(rp2,cm2),(rp2, obj.col1),(rp2,cp2)])
            black_arrayb.extend([(rm3,cm3),(rm3,obj.col1),(rm3,cp3),(obj.row3,cm3),(obj.row3,cp3),(rp3,cm3),(rp3, obj.col1),(rp3,cp3)])
    
    
    if isinstance(obj, Shipb2):
        if obj.dir == 1:
            rm, cm = obj.row1 - 1, obj.col1 - 1
            rp, cp = obj.row1 + 1, obj.col1 + 1
            rm2, cm2 = obj.row1 - 1, obj.col2 - 1
            rp2, cp2 = obj.row1 + 1, obj.col2 + 1
            black_arrayb.extend([(rm,cm),(rm,obj.col1),(rm,cp),(obj.row1,cm),(obj.row1,cp),(rp,cm),(rp, obj.col1),(rp,cp)])
            black_arrayb.extend([(rm2,cm2),(rm2,obj.col2),(rm2,cp2),(obj.row1,cm2),(obj.row1,cp2),(rp2,cm2),(rp2, obj.col2),(rp2,cp2)])
            
        else:
            rm, cm = obj.row1 - 1, obj.col1 - 1
            rp, cp = obj.row1 + 1, obj.col1 + 1
            rm2, cm2 = obj.row2 - 1, obj.col1 - 1
            rp2, cp2 = obj.row2 + 1, obj.col1 + 1
            black_arrayb.extend([(rm,cm),(rm,obj.col1),(rm,cp),(obj.row1,cm),(obj.row1,cp),(rp,cm),(rp, obj.col1),(rp,cp)])
            black_arrayb.extend([(rm2,cm2),(rm2,obj.col1),(rm2,cp2),(obj.row2,cm2),(obj.row2,cp2),(rp2,cm2),(rp2, obj.col1),(rp2,cp2)])
    
    if isinstance(obj, Shipb):
        rm, cm = obj.row - 1, obj.col - 1
        rp, cp = obj.row + 1, obj.col + 1
        black_arrayb.extend([(rm,cm),(rm,obj.col),(rm,cp),(obj.row,cm),(obj.row,cp),(rp,cm),(rp, obj.col),(rp,cp)])           
            
    

#вывод поля бота
def board_display(board):
    for row in board:
        print(" ".join(row))

class Ship3():
    used_coords = []

    def __init__(self):
        while True:
            # 1 - горизонтальное | 2 - вертикальное
            dir = randint(1,2)
            self.dir = dir
            row = randint(0, 9)
            col = randint(0, 9)
            if dir == 1:
                cord2 = col + 1
                cord3 = col + 2
                if (row, col) not in Ship3.used_coords and (row, col) not in black_array and (row, cord2, cord3) not in Ship3.used_coords and (row, cord2, cord3) not in black_array and col < 8:
                    self.row1, self.col1 = row, col
                    self.row2, self.col2 = row, cord2
                    self.row3, self.col3 = row, cord3
                    Ship3.used_coords.extend([(row, col), (cord2, row),(cord3, row)])
                    break
            else:
                cord2 = row + 1
                cord3 = row + 2
                if (row, col) not in Ship3.used_coords and (row, col) not in black_array and (cord2, col,cord3) not in Ship3.used_coords and (cord2, col,cord3) not in black_array and row < 8:
                    self.row1, self.col1 = row, col
                    self.row2, self.col2 = cord2, col
                    self.row3, self.col3 = cord3, col
                    Ship3.used_coords.extend([(row, col), (cord2, col),(cord3, col)])
                    break




class Ship2():
    

    def __init__(self):
        while True:
            # 1 - горизонтальное | 2 - вертикальное
            dir = randint(1,2)
            self.dir = dir
            row = randint(0, 9)
            col = randint(0, 9)
            if dir == 1:
                cord2 = col + 1
                if (row, col) not in Ship3.used_coords and (row, col) not in black_array and (row, cord2) not in Ship3.used_coords and (row, cord2) not in black_array and col < 9:
                    self.row1, self.col1 = row, col
                    self.row2, self.col2 = row, cord2
                    Ship3.used_coords.extend([(row, col), (row, cord2)])
                    break
            else:
                cord2 = row + 1
                if (row, col) not in Ship3.used_coords and (row, col) not in black_array and (cord2, col) not in Ship3.used_coords and (cord2, col) not in black_array and row < 9:
                    self.row1, self.col1 = row, col
                    self.row2, self.col2 = cord2, col
                    Ship3.used_coords.extend([(row, col), (cord2, col)])
                    break







#короче создает несколько кораблей одиночных
class Ship():

    def __init__(self):
        while True:
            row = randint(0, 10 - 1)
            col = randint(0, 10 - 1)
            if (row, col) not in Ship3.used_coords and (row, col) not in black_array :
                self.row = row
                self.col = col
                Ship3.used_coords.append((row, col))
                break
















class Shipb3():
    used_coordsb = []

    def __init__(self):
        while True:
            # 1 - горизонтальное | 2 - вертикальное
            dir = randint(1,2)
            self.dir = dir
            row = randint(0, 9)
            col = randint(0, 9)
            if dir == 1:
                cord2 = col + 1
                cord3 = col + 2
                if (row, col) not in Shipb3.used_coordsb and (row, col) not in black_array and (row, cord2, cord3) not in Shipb3.used_coordsb and (row, cord2, cord3) not in black_arrayb and col < 8:
                    self.row1, self.col1 = row, col
                    self.row2, self.col2 = row, cord2
                    self.row3, self.col3 = row, cord3
                    Shipb3.used_coordsb.extend([(row, col), (cord2, row),(cord3, row)])
                    break
            else:
                cord2 = row + 1
                cord3 = row + 2
                if (row, col) not in Shipb3.used_coordsb and (row, col) not in black_arrayb and (cord2, col,cord3) not in Shipb3.used_coordsb and (cord2, col,cord3) not in black_arrayb and row < 8:
                    self.row1, self.col1 = row, col
                    self.row2, self.col2 = cord2, col
                    self.row3, self.col3 = cord3, col
                    Shipb3.used_coordsb.extend([(row, col), (cord2, col),(cord3, col)])
                    break




class Shipb2():
    

    def __init__(self):
        while True:
            # 1 - горизонтальное | 2 - вертикальное
            dir = randint(1,2)
            self.dir = dir
            row = randint(0, 9)
            col = randint(0, 9)
            if dir == 1:
                cord2 = col + 1
                if (row, col) not in Shipb3.used_coordsb and (row, col) not in black_arrayb and (row, cord2) not in Shipb3.used_coordsb and (row, cord2) not in black_arrayb and col < 9:
                    self.row1, self.col1 = row, col
                    self.row2, self.col2 = row, cord2
                    Shipb3.used_coordsb.extend([(row, col), (row, cord2)])
                    break
            else:
                cord2 = row + 1
                if (row, col) not in Shipb3.used_coordsb and (row, col) not in black_arrayb and (cord2, col) not in Shipb3.used_coordsb and (cord2, col) not in black_arrayb and row < 9:
                    self.row1, self.col1 = row, col
                    self.row2, self.col2 = cord2, col
                    Shipb3.used_coordsb.extend([(row, col), (cord2, col)])
                    break







#короче создает несколько кораблей одиночных
class Shipb():

    def __init__(self):
        while True:
            row = randint(0, 10 - 1)
            col = randint(0, 10 - 1)
            if (row, col) not in Shipb3.used_coordsb and (row, col) not in black_arrayb :
                self.row = row
                self.col = col
                Shipb3.used_coordsb.append((row, col))
                break

ship31 = Shipb3()
black_list_bot(ship31)
ship32 = Shipb3()
black_list_bot(ship32)


shipig31 = Ship3()
black_list(shipig31)
shipig32 = Ship3()
black_list(shipig32)


ship21 = Shipb2()
black_list_bot(ship21)
ship22 = Shipb2()
black_list_bot(ship22)
ship23 = Shipb2()
black_list_bot(ship23)

shipig21 = Ship2()
black_list(shipig21)
shipig22 = Ship2()
black_list(shipig22)
shipig23 = Ship2()
black_list(shipig23)


ship1 = Shipb()
black_list_bot(ship1)
ship2 = Shipb()
black_list_bot(ship2)
ship3 = Shipb()
black_list_bot(ship3)
ship4 = Shipb()
black_list_bot(ship4)


shipig1 = Ship()
black_list(shipig1)
shipig2 = Ship()
black_list(shipig2)
shipig3 = Ship()
black_list(shipig3)
shipig4 = Ship()
black_list(shipig4)



korablirow = []
korablicol = []
korablirowig = []
korablicolig = []
#3
korablirow.append(ship31.row1),korablicol.append(ship31.col1),korablirow.append(ship31.row2),korablicol.append(ship31.col2),korablirow.append(ship31.row3),korablicol.append(ship31.col3)

korablirow.append(ship32.row1),korablicol.append(ship32.col1),korablirow.append(ship32.row2),korablicol.append(ship32.col2),korablirow.append(ship32.row3),korablicol.append(ship32.col3)
#2
korablirow.append(ship21.row2),korablicol.append(ship21.col2),korablirow.append(ship21.row1),korablicol.append(ship21.col1)
korablirow.append(ship22.row2),korablicol.append(ship22.col2),korablirow.append(ship22.row1),korablicol.append(ship22.col1)
korablirow.append(ship23.row2),korablicol.append(ship23.col2),korablirow.append(ship23.row1),korablicol.append(ship23.col1)
#1
korablirow.append(ship1.row),korablicol.append(ship1.col)
korablirow.append(ship2.row),korablicol.append(ship2.col)
korablirow.append(ship3.row),korablicol.append(ship3.col)
korablirow.append(ship4.row),korablicol.append(ship4.col)



#3
korablirowig.append(shipig31.row1),korablicolig.append(shipig31.col1),korablirowig.append(shipig31.row2),korablicolig.append(shipig31.col2),korablirowig.append(shipig31.row3),korablicolig.append(shipig31.col3)
korablirowig.append(shipig32.row1),korablicolig.append(shipig32.col1),korablirowig.append(shipig32.row2),korablicolig.append(shipig32.col2),korablirowig.append(shipig32.row3),korablicolig.append(shipig32.col3)
#2
korablirowig.append(shipig21.row1),korablicolig.append(shipig21.col1),korablirowig.append(shipig21.row2),korablicolig.append(shipig21.col2)
korablirowig.append(shipig22.row1),korablicolig.append(shipig22.col1),korablirowig.append(shipig22.row2),korablicolig.append(shipig22.col2)
korablirowig.append(shipig23.row1),korablicolig.append(shipig23.col1),korablirowig.append(shipig23.row2),korablicolig.append(shipig23.col2)
#1
korablirowig.append(shipig1.row),korablicolig.append(shipig1.col)
korablirowig.append(shipig2.row),korablicolig.append(shipig2.col)
korablirowig.append(shipig3.row),korablicolig.append(shipig3.col)
korablirowig.append(shipig4.row),korablicolig.append(shipig4.col)

print(korablirowig)
print(korablicolig)

print(korablirow)
print(korablicol)
# print(ship1.row, ship1.col)
# print(ship2.row, ship2.col)
# print(ship3.row, ship3.col)
# print(ship1.used_coords)


#проверка кордов корабля короче
index = 0
def shipchek(row, col):
    global korablirow
    global korablicol
    global index
    index = 0
    for item in korablirow:
        if item == row:
            if korablicol[index] == col:
                return True
            else:
                index += 1
        else:
            index += 1
    return False


index1 = 0
for item in korablirowig:
    board1[item][korablicolig[index1]] = "■"
    index1 += 1





index2 = 0
for item in korablirow:
    board[item][korablicol[index2]] = "■"
    index2 += 1

board_display1(board1)
print("-------------------")
board_display(board)
   

# Начало игрового цикла
while korablicol != [] and korablirow != []:
    try:
        guess_row = int(input("Guess Row: ") ) - 1
        guess_col = int(input("Guess Col: ") ) - 1
    except:
        print("ээээ, ты не так ввел\nты проиграл из за того что ты фуфел :((")
        break
        
    if shipchek(guess_row, guess_col) == True:
        board[guess_row][guess_col] = "■"
        print("ты попал!")
        del korablirow[index]
        del korablicol[index]
    else:
        print("u missed :(")
        try:
            board[guess_row][guess_col] = "X"
        except:
            print("ээээ, ты не так ввел\nты проиграл из за того что ты фуфел :((")
            break
        
    
# стрельба бота

    
    botrow = randint(0, 9)
    botcol = randint(0, 9)
    
        
        
    if shipchek(botrow, botcol) == True:
        board1[botrow][botcol] = "▓"
        print("bot hit the ship")
        del korablirow[index]
        del korablicol[index]
    else:
        print("bot missed :)")
        board1[botrow][botcol] = "X"    
    
    board_display1(board1)
    print("-------------------")
    board_display(board)

if korablicol == [] and korablirow == []:
    print("u win")
else:
    print("u loose(")