""" output
1	2	3	4	5	6
20	21	22	23	24	7
19	32	33	34	25	8
18	31	36	35	26	9
17	30	29	28	27	10
16	15	14	13	12	11
"""

def show_spiral_matrix(n):
    """
    check if current position is empty, make it number
    check if next postion is avilable, move to it, if not, change direction.
    """
    matrix = [[0] * n for _ in range(n)]
    row, col = 0, 0
    num, direction = 1, 0 # dirction: 0 is going right, 1 is goin gdown, 2 is going left, 3 is going up.
    while num <= n ** 2:
        if matrix[row][col] == 0: # currernt postion is empty?
            matrix[row][col] = num # make current postion this turn number
            num += 1 # ready for next turn
        if direction == 0: # if going right?
            if col < n - 1 and matrix[row][col + 1] == 0: # if still in this row and next postion is empty
                col += 1 # move to next position
            else:
                direction += 1 # if not, change direction to next, going down
        elif direction == 1:#if going down?
            if row < n - 1 and matrix[row + 1][col] == 0: # if still in this col, and next postion is empty
                row += 1 # move to next position
            else:
                direction += 1 # if not, change direction to next, going down
        elif direction == 2:#if going left?
            if col > 0 and matrix[row][col - 1] == 0: # if still in this row, and next postion is empty
                col -= 1 # move to next position
            else:
                direction += 1 # if not, change direction to next, going down
        else:#if going up?
            if row > 0 and matrix[row - 1][col] == 0: # if still in this col, and next postion is empty
                row -= 1 # move to next position
            else:
                direction += 1 # if not, change direction to next, going down
        direction %= 4 # if after going up, make it going to right again
    for x in matrix:
        for y in x:
            print(y, end='\t')
        print()


show_spiral_matrix(6)
