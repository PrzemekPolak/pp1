class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        matrix = [[0 for z in range(y)] for a in range(x)]
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

m = matrix.create(4,3)
matrix.print(m)