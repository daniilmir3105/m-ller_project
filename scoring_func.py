from abc import *
from decimal import Decimal


class base_class(metaclass=ABCMeta):
    '''
    This class will be base for our scoring class
    '''

    @abstractmethod
    def rec(self, y=1, z=1):
        return 108 - ((815 - 1500 / z) / y)


class scoring_class(base_class):
    '''
    This is a class, that must score our results.
    '''

    def floatpt(self, N):
        '''
        This method will score our result in float datatype.
        '''

        x = [4, 4.25]
        for i in range(2, N + 1):
            x.append(scoring_class.rec(x[i - 1], x[i - 2]))
        return x

    def fixedpt(self, N):
        '''
        This method will score our result in decimal datatype.
        '''

        x = [Decimal(4), Decimal(17) / Decimal(4)]
        for i in range(2, N + 1):
            x.append(scoring_class.rec(x[i - 1], x[i - 2]))
        return x
