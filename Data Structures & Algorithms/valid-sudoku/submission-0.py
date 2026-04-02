class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = defaultdict(set)
        col_check = defaultdict(set)
        sub_box_check = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                elif board[r][c] in row_check[r] or board[r][c] in col_check[c] or board[r][c] in sub_box_check[r//3, c//3]:
                    return False
                
                row_check[r].add(board[r][c])
                col_check[c].add(board[r][c])
                sub_box_check[r//3, c//3].add(board[r][c])
        
        return True