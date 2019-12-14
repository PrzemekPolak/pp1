class Arrays():
    @staticmethod 
    def print_in_col(array):
        for c in array:
           print(c)

    @staticmethod
    def zaw_tablicy_wiersz(array):
        tekst = ''
        for x in array:
            tekst = tekst + str(x) + ', '
        print(tekst[:-2])


my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.zaw_tablicy_wiersz(my_array)