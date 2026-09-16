from tkinter import *  # type: ignore
from game_logic import GameLogic

FONT = ('Courier', 48, 'normal')


class GameUI():
    def __init__(self, logic: GameLogic) -> None:
        self.game_logic = logic
        self.window = Tk()
        self.window.config(bg="white", padx=20, pady=20)
        self.window.bind('<Button-1>', self.place)
        self.turn = "x"
        self.center_coords = (0, 0)

        # Images
        self.grid_image = PhotoImage(file="images/grid-image.png")
        self.x_image = PhotoImage(file="images/x-image.png")
        self.o_image = PhotoImage(file="images/o-image.png")
        self.turn_image = self.x_image

        # Canvas
        self.canvas = Canvas(width=400, height=400, highlightthickness=0)
        self.canvas.create_image(200, 200, image=self.grid_image)
        self.canvas.grid(column=0, row=1)

        self.window.mainloop()

    def place(self, event: Event[Misc]):
        self.x_coord = event.x
        self.y_coord = event.y

        if self.check_coords():
            self.canvas.create_image(
                self.center_coords[0],
                self.center_coords[1],
                image=self.turn_image,
            )
            if self.game_logic.check_winner():
                self.canvas.delete("all")
                self.winner_image = self.turn_image.zoom(5, 5)
                self.canvas.create_image(200, 200, image=self.winner_image)
                self.canvas.create_text(
                    200, 200, text="Winner", font=FONT, fill="green")
                self.window.unbind("<Button-1>")
            self.switch_turn()

    def check_coords(self):

        cell = self.cell(self.x_coord, self.y_coord)
        if len(cell) != 0:
            self.center_coords = self.cell_center(cell[0], cell[1])

            if self.x_coord > 40 and self.y_coord > 40 and not self.game_logic.check_mark(cell):
                self.game_logic.place_mark((self.turn, cell[0], cell[1]))
                return True
            else:
                return False

        else:
            return

    def cell(self, x_coord, y_coord) -> tuple:
        if x_coord < 40 or x_coord > 360:
            return ()

        if y_coord < 40 or y_coord > 360:
            return ()

        column = int((x_coord - 40) / (320 / 3))
        row = int((y_coord - 40) / (320 / 3))

        return (row, column)

    def switch_turn(self):
        self.turn = "x" if self.turn == "o" else "o"
        if self.turn == "x":
            self.turn_image = self.x_image
        else:
            self.turn_image = self.o_image

    def cell_center(self, row, column) -> tuple:
        cell_size = 320 / 3

        x = 40 + (column * cell_size) + (cell_size / 2)
        y = 40 + (row * cell_size) + (cell_size / 2)

        return (x, y)
