class GameLogic():
    def __init__(self) -> None:
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def check_winner(self):
        for row in self.board:
            if row[0] and row[0] == row[1] == row[2]:
                return row[0]

        for col in range(3):
            if self.board[0][col] and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]

        if self.board[0][0] and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        if self.board[0][2] and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None

    def check_mark(self, place: tuple):
        x = place[0]
        y = place[1]
        return self.board[x][y] != ""

    def place_mark(self, place: tuple):
        x_or_y = place[0]
        x = place[1]
        y = place[2]

        self.board[x][y] = x_or_y
