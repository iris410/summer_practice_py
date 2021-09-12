import random
class Minefield:

    def __init__(self, rows, cols, number_of_mines):
        self.total_row = rows
        self.total_col = cols

        self.game_map = []
        count = 0
        for i in range(rows):
            r = [0]*cols
            self.game_map.append(r)

        self.show_map = []
        for i in range(rows):
            r = ["-"]*cols
            self.show_map.append(r)

        while(count < number_of_mines):
            i = random.randrange(0,rows)
            j = random.randrange(0,cols)
            if (self.game_map[i][j]) == 9:
                continue
            else:
                self.game_map[i][j] = 9
                count += 1
                for r in range(-1,2):
                    if (i + r) in range(self.total_row): # in [0,total_row)
                        for c in range(-1,2):
                            if (j + c) in range(self.total_col): # in [0,total_column)
                                if ((r == 0) and (c == 0)) or self.game_map[i+r][j+c] == 9:
                                    continue
                                else:
                                    self.game_map[i+r][j+c] += 1
        #[i-1][j-1],[i-1][j],[i-1][j+1],[i][j-1],[i][j+1],[i+1][j-1],[i+1][j],[i+1][j+1]
        return

    def on_click(self, row, col):
        if (col in range(self.total_col)) and (row in range(self.total_row)):
            if self.game_map[row][col] == 9:
                return self.print_minefield(True)
            if self.game_map[row][col] == 0 and self.show_map[row][col] == '-':
                self.show_map[row][col] = 0
                for r in range(-1,2):
                    for c in range(-1,2):
                        if (r == 0) and (c == 0):
                            continue
                        else:
                            self.on_click(r+row,c+col)
            else:
                self.show_map[row][col] = self.game_map[row][col]
        pass

    def print_minefield(self, show_hidden):
        if show_hidden == True:
          #copy game_map to show_map
            for i in range(self.total_row):
                for j in range(self.total_col):
                    if self.game_map[i][j] == 9:
                        print('X', end = ' ')
                    else:
                        print(self.game_map[i][j], end = ' ')
                print('')
        else:
            for i in range(self.total_row):
                for j in range(self.total_col):
                    print(self.show_map[i][j], end = ' ')
                print('')
        pass


org = Minefield(7,5,2)
org.print_minefield(True)
org.on_click(2,2)
print('----show map------')
org.print_minefield(False)
