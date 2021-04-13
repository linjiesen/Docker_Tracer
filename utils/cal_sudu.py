import time


def cross(A, B):
    # 例如：A = 'ABC', B = '123'
    # 则返回['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    return [a + b for a in A for b in B]


def arr_to_dict(A, B):
    # 例如：A = ['A', 'B', 'C'], B = ['1', '2', '3']
    # 则返回{'A': '1', 'B': '2', 'C': '3'}
    return dict(zip(A, B))


def str_to_arr(str_sudoku):
    # 传入：str_sudoku = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    # 返回['4', '.', '.', '.', '.', '.', '8', ... , '.', '.']
    return [c for c in str_sudoku if c in cols or c in '0.']


def show_str_sudoku(str_sudoku):
    # 解析字符串形式的数独并展示
    for i, value in enumerate(str_sudoku):
        if i % 3 == 0 and i % 9 != 0:
            print('|', end=' ')
        print(value, end=' ')
        if (i + 1) % 9 == 0:
            print()
        if i == 26 or i == 53:
            print('------+-------+------')


def show_dict_sudoku(dict_sudoku):
    # 解析字典形式的数独并展示
    width = 1 + max(len(dict_sudoku[s]) for s in squares)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(dict_sudoku[r + c].center(width) + ('|' if c in '36' else '') for c in cols))
        if r in 'CF': print(line)
    print()


cols = '123456789'
rows = 'ABCDEFGHI'
# squares表示 9*9个元素编号:['A1', 'A2', 'A3', ... , 'I8', 'I9']
squares = cross(rows, cols)
# unitlist表示 3*9个单元列表:
unitlist = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in
                                                                               ('ABC', 'DEF', 'GHI') for cs in
                                                                               ('123', '456', '789')])
# units表示 某个元素编号:与之相关的3个单元列表
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
# peers表示 某个元素编号:与之相关的20个元素编号
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)


# 一.数独预处理
def parse_sudoku(str_sudoku):
    # values代表各位置上可能的取值:{'A1': '123456789', 'A2': '123456789', ... , 'I8': '123456789', 'I9': '123456789'}
    values = dict((s, cols) for s in squares)
    # arr_sudoku为数组形式, dict_sudoku为字典形式, 均为81位
    arr_sudoku = str_to_arr(str_sudoku)
    dict_sudoku = arr_to_dict(squares, arr_sudoku)  # {'A1': '4', 'A2': '.', ... , 'I8': '.', 'I9': '.'}

    for key, value in dict_sudoku.items():
        if value in cols and not assign(values, key, value):
            return False

    return values


def assign(values, key, value):
    # 从values[key]中删除除了value以外的所有值，因为value是唯一的值
    # 如果在过程中发现矛盾，则返回False
    other_values = values[key].replace(value, '')
    if all(eliminate(values, key, num) for num in other_values):
        return values
    else:
        return False


def eliminate(values, key, num):
    # 从values[key]中删除值num，因为num是不可能的
    if num not in values[key]:
        return values
    values[key] = values[key].replace(num, '')

    # 这里采用了约束传播
    # 1.如果一个方块只有一个可能值，把这个值从方块的对等方块（的可能值）中排除。
    if len(values[key]) == 0:
        return False
    elif len(values[key]) == 1:
        only_value = values[key]
        # 从与之相关的20个元素中删除only_value
        if not all(eliminate(values, peer, only_value) for peer in peers[key]):
            return False

    # 2.如果一个单元只有一个可能位置来放某个值，就把值放那。
    for unit in units[key]:
        dplaces = [s for s in unit if num in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            only_key = dplaces[0]
            if not assign(values, only_key, num):
                return False

    return values


# 二.解数独
def solve_sudoku(str_sudoku):
    return search_sudoku(parse_sudoku(str_sudoku))


def search_sudoku(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values

    # 选择可能值数目最少的方块, 进行深度优先搜索
    n, key = min((len(values[key]), key) for key in squares if len(values[key]) > 1)
    return some_result(search_sudoku(assign(values.copy(), key, num)) for num in values[key])


def some_result(values):
    for result in values:
        if result:
            return result
    return False


if __name__ == '__main__':
    # str_sudoku为字符串形式, 为81位
    str_sudoku = ['.5.....2.4..2.6..7..8.3.1...1.....6...9...5...7.....9...5.8.3..7..9.1..4.2.....7.']
    # str_sudoku = ['4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......',
    #               '003020600900305001001806400008102900700000008006708200002609500800203009005010300',
    #               '.....6....59.....82....8....45........3........6..3.54...325..6..................']

    for sudoku in str_sudoku:
        start = time.time()
        solve_result = solve_sudoku(sudoku)
        end = time.time()
        print('初始数独为：')
        show_str_sudoku(sudoku)
        print('解为：')
        show_dict_sudoku(solve_result)
        print("求解数独运行时间为: %f s" % (end - start))
