class initialisation:
    '''
    In this class will be method with initialisation
    '''

    def make_initialisation(self):
        '''
        Method with initialisation
        '''

        name = input("Введите, пожалуйста, свое имя: ")

        print("Приветствую, " + name +
            ", вы вошли в программу, котороая позволяет расчитывать рекуррентное соотношение Мюллера.")
        print("Рекуррентное соотношение Мюллера: x=f(y,z)=108-((815-1500/z)/y).")