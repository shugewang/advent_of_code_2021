def get_bingo(input_file_name):
    f = open(input_file_name, "r")
    bingo = list(f.read().splitlines())
    numbers_drawn = bingo.pop(0).split(',')
    bingo_2d_array = convert_to_bingo_dict(bingo)
    return numbers_drawn, bingo_2d_array


def convert_to_bingo_dict(bingo):
    count = 0
    board_number = 1
    bingo_dict = {board_number: []}
    for x in bingo:
        if x != '':
            x_arr = list(filter(lambda a: a != '', x.split(' ')))
            if count != 0 and count % 5 == 0:
                count = 0
                board_number += 1
                bingo_dict[board_number] = [x_arr]
            else:
                bingo_dict[board_number].append(x_arr)
            count += 1
    return bingo_dict


def check_winner(numbers_drawn, bingo):
    total_boards = list(range(1, len(bingo)+1))
    winning_score = 0
    for number in numbers_drawn:
        for board_number, board in bingo.items():
            for i in range(len(board)):
                bingo[board_number][i] = [check_if_called(x, number) for x in board[i]]
                if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] or board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i]:
                    if board_number in total_boards:
                        total_boards.remove(board_number)
                        if len(total_boards) == len(bingo) - 1:
                            winning_score = get_score(bingo, board_number, number)
                        if len(total_boards) == 0:
                            losing_score = get_score(bingo, board_number, number)
                            return winning_score, losing_score


def check_if_called(bingo_number, number):
    if bingo_number == number:
        return "y"
    else:
        return bingo_number


def get_score(bingo, board_number, number):
    unmarked_sum = 0
    for i in bingo[board_number]:
         for j in i:
             if j != 'y':
                 unmarked_sum += int(j)
    return unmarked_sum*int(number)


def main():
    numbers_drawn, bingo = get_bingo("bingo.txt")
    print(numbers_drawn)
    print(bingo)
    winning_score, losing_score = check_winner(numbers_drawn, bingo)
    print("winning score", winning_score)
    print("losing score", losing_score)


main()