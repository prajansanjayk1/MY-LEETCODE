class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    box_index = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)
                else:
                    empty_cells.append((r, c))

        def get_possible_numbers(r, c):
            box_index = (r // 3) * 3 + (c // 3)
            possible = []
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                    possible.append(num)
            return possible

        # Sort empty cells based on the number of possible values (heuristic)
        empty_cells.sort(key=lambda cell: len(get_possible_numbers(cell[0], cell[1])))

        def solve(empty_cell_index):
            if empty_cell_index >= len(empty_cells):
                return True
            
            r, c = empty_cells[empty_cell_index]
            box_index = (r // 3) * 3 + (c // 3)
            
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    if solve(empty_cell_index + 1):
                        return True
                    
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)
            
            return False

        solve(0)