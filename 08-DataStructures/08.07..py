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
    
    @staticmethod
    def fill_random(matrix,m,n):
        from random import randrange
        for g in range(len(matrix)):
            for h in range(len(matrix[0])):
                losowa = randrange(m, n+1)
                matrix[g][h] = losowa
        return matrix
        

m = matrix.create(3,5)
matrix.fill_random(m,5,9)
matrix.print(m)

