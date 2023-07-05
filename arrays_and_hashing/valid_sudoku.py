# It's important to clarify that only the filled cells need to be validated before
# starting the question. This is a much harder question if you need the unfilled cells
# to be validated as well.

# it's ok to use O(1) copies of an O(1) array, it's still O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Memory: O(1)
        Runtime: O(1)
        """
        # create data structures
        seen: set[str] = set()

        # check the rows
        for row in board:
            seen.clear()
            for box in row:
                if box != '.' and box in seen:
                    return False
                seen.add(box)

        # check the columns
        for i in range(0,9):
            seen.clear()
            for row in board:
                if row[i] != '.' and row[i] in seen:
                    return False
                seen.add(row[i])
                    
        # check the squares
        for box_row in range(0,3):
            for box_col in range(0,3):
                seen.clear()
                for row in range(0,3):
                    row += box_row * 3
                    for col in range(0,3):
                        col += box_col * 3
                        cell = board[row][col]
                        if cell != '.' and cell in seen:
                            return False
                        seen.add(cell)

        return True
    def isValidSudokuCleaner(self, board: List[List[str]]) -> bool:
        """
        Memory: O(1)
        Runtime: O(1)
        """
        # create data structures
        rows: dict[set[str]] = collections.defaultdict(set)
        cols: dict[set[str]] = collections.defaultdict(set)
        boxes: dict[set[str]] = collections.defaultdict(set)

        # go through each square and add the entry to the corresponding set
        # for rows, cols, and boxes
        for i in range(0, 9):
            for j in range(0,9):
                cell = board[i][j]
                if cell == '.':
                    continue
                if cell in rows[i]:
                    return False 
                rows[i].add(cell) 
                if cell in cols[j]:
                    return False
                cols[j].add(cell) 
                box = (i // 3, j // 3)
                if cell in boxes[box]: 
                    return False
                boxes[box].add(cell) 

        return True