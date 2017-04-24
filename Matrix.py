class Matrix:

    def __init__(self, row, col):
        self.array = [[None for x in range(row)]for y in range(col)]

    def __str__(self):
        result = ""
        for col in self.array:
            result += str(col)
            result += '\n'
        return result

    def get_at(self, row, col):
        return self.array[row][col]

    def set_at(self, row, col, value):
        self.array[row][col] = value

    def __len__(self):
        return len(self.array)

    def __getitem__(self, item):
        return self.array[item]


