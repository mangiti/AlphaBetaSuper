'''
Minesweeper DQN Environment

'''
import numpy as np


class Minesweeper:

    def __init__(self, height=9, width=9, n_bombs=10):
        self.width = width
        self.height = height
        self.n_bombs = n_bombs

    def generate(self):
        # Genreate empty map, adjacency, and view
        h, w = self.height, self.width
        self.map = np.zeros((h, w)).astype('int8')
        self.view = np.full_like(self.map, -1).astype('int8')

        # Generate bomb locations
        self.bombs = np.random.choice(np.arange(h * w), self.n_bombs, False)
        self.bomb_loc = np.unravel_index(self.bombs, (h, w))

        # Mark bombs
        self.map[self.bomb_loc] = 1
        self.adj = self.map.copy() - 3

        for x in range(h):
            for y in range(w):
                if self.map[x, y] != 1:
                    view = self.map[max(0, x - 1):min(h, x + 2),
                                    max(0, y - 1):min(w, y + 2)]
                    self.adj[x, y] = view.sum()

    def dig(self, arr, mode='max', thresh=0.5):
        assert self.map.shape == arr.shape
        if mode == 'max':
            arr = arr / arr.sum()
            idx = np.unravel_index(arr.argmax(), arr.shape)
            self.view[idx] = self.adj[idx]
        elif mode == 'thresh':
            self.view[arr > thresh] = self.adj[arr > thresh]


def main():
    print("Minesweeper Class")
    ms = Minesweeper()
    ms.generate()
    print(ms.map)
    print(ms.view)
    print(ms.adj)

    digMask = np.random.rand(9, 9)
    ms.dig(digMask, 'thresh')
    print(ms.view)


if __name__ == "__main__":
    main()
