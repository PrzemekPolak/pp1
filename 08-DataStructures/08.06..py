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
            
    @staticmethod
    def create_unit(x):
        pom = matrix.create(x,x)
        for q in range(x):
            pom[q][q] = 1
        return pom

m = matrix.create_unit(6)
matrix.print(m)


