import re

def get_bingo(input_file_name):
    f = open(input_file_name, "r")
    bingo = list(f.read().splitlines())
    numbers_drawn = bingo.pop(0).split(',')
    return numbers_drawn, bingo


def convert_to_2d_array(bingo):
    bingo_2d_array = [[]]
    count = 0
    board_number = 0
    for x in bingo:
        if x != '':
            if count != 0 and count % 5 == 0:
                bingo_2d_array.append([])
                count = 0
                board_number += 1
                bingo_2d_array[board_number].append(x)
            else:
                bingo_2d_array[board_number].append(x)
            count += 1
            print(x)
            print(count)
            print(bingo_2d_array)


def convert_to_bingo_dict(bingo):
    count = 0
    board_number = 1
    bingo_dict = {board_number: []}
    for x in bingo:
        if x != '':
            if count != 0 and count % 5 == 0:
                count = 0
                board_number += 1
                bingo_dict[board_number] = [x]
            else:
                bingo_dict[board_number].append(x)
            count += 1
    return bingo_dict


def check_winner(numbers_drawn, bingo_dict):
    win = False
    for number in numbers_drawn:
        for board_number, board in bingo_dict.items():
            for i in range(len(board)):
                # print('row',board)
                bingo_dict[board_number][i] = re.sub(r'\b%s\b' % number, "y", bingo_dict[board_number][i])
                # print(bingo_dict[board_number])
                if bingo_dict[board_number][i].count('y') == 5:
                    print("there's a win", number)
                    print(bingo_dict[board_number])
                    print(board_number)
                    win = True
                    break
            win = check_columns(board_number, board, win)
            if win:
                get_winning_score(bingo_dict, board_number, number)
                print(board_number)
                print(bingo_dict[board_number])
                break


def check_columns(board_number, board, win):
    col_board = [elem for elem in board]
    for i in range(len(col_board)):
        col_board[i] = list(filter(lambda a: a != '', col_board[i].split(' ')))
        if col_board[i][0] == col_board[i][1] == col_board[i][2] == col_board[i][3] == col_board[i][4]:
            win = True
            print('col')
    return win



def get_winning_score(bingo_dict, board_number, number):
    winning_board = " ".join(bingo_dict[board_number])
    winning_board = winning_board.replace("y", "").split(" ")
    unmarked_sum = sum(list(map(int, list(filter(lambda a: a != '', winning_board)))))
    print(unmarked_sum*int(number))


def main():
    numbers_drawn, bingo = get_bingo("bingo.txt")
    bingo_dict = convert_to_bingo_dict(bingo)
    print("numbers", numbers_drawn)
    print(bingo_dict)
    check_winner(numbers_drawn, bingo_dict)


main()