class Matrix(object):
    def __init__(self, matrix_string):
        self._matrix = [
                [int(n) for n in row.split()] 
                for row in matrix_string.splitlines()
            ]

    def row(self, index):
        return [element for element in self._matrix[index - 1]]

    def column(self, index):
        return [r[index - 1] for r in self._matrix]
