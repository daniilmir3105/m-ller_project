class final_result:
    '''
    This class have a method, that will return our result in a simple table.
    '''

    def returning_result(self, N, arr_1, arr_2):
        '''
        Method, that will return our result in a simple table.
        '''

        for i in range(N):
            print(str(i) + '|' + str(arr_1[i]) + '|' + str(arr_2[i]))