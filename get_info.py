class getting_information:
    '''
    This is a class, that have a method, that will become and return number of iterations
    '''

    def get_number_of_iteration(self):
        '''
        Method, that will become and return number of iterations
        '''
        try:
            N = int(input("Please, enter the number of iterations: "))
        except ValueError as err:
            print('The number of iterations can only be an integer and a positive number ')
            N = int(input("Please, enter the number of iterations: "))

        return N