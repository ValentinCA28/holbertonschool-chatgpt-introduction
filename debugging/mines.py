#!/usr/bin/python3
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_cells = width * height
        self.mine_count = mines

        # Pick unique mine positions
        self.mines = set(random.sample(range(self.total_cells), mines))

        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

        # Precompute numbers (optional but makes printing faster)
        self._precompute_numbers()

    def _precompute_numbers(self):
        """Calculate number for every non-mine cell once at start"""
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines:
                    self.field[y][x] = self._count_mines_nearby(x, y)

    def _count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def print_board(self, reveal_all=False):
        clear_screen()
        # Header
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))
        for y in range(self.height):
            print(f'{y:2} ', end='')
            for x in range(self.width):
                pos = y * self.width + x
                if reveal_all or self.revealed[y][x]:
                    if pos in self.mines:
                        print(' *', end=' ')
                    else:
                        num = self.field[y][x]
                        print(f' {num}' if num > 0 else '  ', end=' ')
                else:
                    print(' .', end=' ')
            print()
        print()

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # ignore invalid, but don't lose

        pos = y * self.width + x

        if pos in self.mines:
            return False  # lose

        if self.revealed[y][x]:
            return True

        self.revealed[y][x] = True

        # Flood fill if empty
        if self.field[y][x] == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)

        return True

    def has_won(self):
        """Win = all non-mine cells are revealed"""
        revealed_count = sum(sum(row) for row in self.revealed)
        return revealed_count == (self.total_cells - self.mine_count)

    def play(self):
        while True:
            self.print_board()

            if self.has_won():
                self.print_board(reveal_all=True)
                print("Congratulations! You've won the game!")
                break

            try:
                inp = input("Enter x y (e.g. 3 4): ").strip()
                if not inp:
                    continue
                parts = inp.split()
                if len(parts) != 2:
                    print("Please enter two numbers: x y")
                    continue
                x = int(parts[0])
                y = int(parts[1])

                if not self.reveal(x, y):
                    self.print_board(reveal_all=True)
                    print("Game Over! You hit a mine.")
                    break

            except ValueError:
                print("Invalid input. Use numbers only (example: 5 2)")
            except KeyboardInterrupt:
                print("\nGame aborted.")
                break


if __name__ == "__main__":
    # You can change difficulty here
    game = Minesweeper(width=10, height=10, mines=12)
    game.play()
