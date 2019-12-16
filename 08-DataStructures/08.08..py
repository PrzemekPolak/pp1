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
    
    @staticmethod     
    def transponse(matrix):
        pom = [[0 for z in range(len(matrix))] for a in range(len(matrix[0]))]
        licz = 0
        for g in matrix:
            for h in range(len(matrix[0])):
                pom[h][licz] = g[h]
            licz += 1
        return pom

m = matrix.create(3,5)
matrix.fill_random(m,1,9)
matrix.print(m)
print('')
x = matrix.transponse(m)
matrix.print(x)