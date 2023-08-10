def greet():
    print('-------------------')
    print('  Приветсвуем вас  ')
    print('      в игре       ')
    print('  крестики-нолики  ')
    print('-------------------')
    print('  Введите в поле   ')
    print('   номер ячейки    ')
    print(' в которую хотите  ')
    print('   сделать ход     ')


greet()

game_board = list(range(1, 10))


def board():
    print('')
    print((game_board[0]), '|', (game_board[1]), '|', (game_board[2]))
    print('----------')
    print((game_board[3]), '|', (game_board[4]), '|', (game_board[5]))
    print('----------')
    print((game_board[6]), '|', (game_board[7]), '|', (game_board[8]))
    print('')


def players_turn(count, symbol):
    number = game_board.index(count)
    game_board[number] = symbol


combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [0, 4, 8], [2, 4, 6]]


def win():
    winner = ''

    for i in combinations:
        if game_board[i[0]] == 'X' and game_board[i[1]] == 'X' and game_board[i[2]] == 'X':
            winner = 'X'
        if game_board[i[0]] == 'O' and game_board[i[1]] == 'O' and game_board[i[2]] == 'O':
            winner = 'O'

    return winner


game_over = False
player = True

while game_over == False:

    board()

    if player == True:
        symbol = 'X'
        count = int(input('Ходит Х: '))
    else:
        symbol = 'O'
        count = int(input('Ходит О: '))

    if count < 1 or count > 9:
        print(" Координаты вне диапазона! ")
        continue

    if (str(game_board[count - 1]) not in 'X' and 'O'):
        game_board[count - 1] = count

    else:
        print('Клетка занята')
        continue

    players_turn(count, symbol)
    winner = win()
    if winner != '':
        game_over = True
    else:
        game_over = False

    player = not (player)

print('Победил', winner)