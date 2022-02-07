class StudentDre:
    def __init__(self,dre):
        self.dre = dre
        self.year = int(dre[0:3])
        self.sequence = dre[3:8]
    
    def check_year(self):
        diff = 2022 - self.year
        if diff < 1900:
            return False
        else: 
            return True
    
    def check_dre_size(self):
        if len(self.dre) == 9:
            return True
        else:
            return False

    def getDigit(self):
        add = sum([int(self.sequence[i]) for i in range(0,len(self.sequence))])    
        remainder = (add % 10)

        if remainder == int(self.dre[8]):
            return True
        else:
            return False
    
    def getYear(self):
        res = 1900 + self.year
        return res


dre = input('Input: ')
student = StudentDre(dre)
p = student.check_dre_size()
q = student.check_year()
r = student.getDigit()

if (p and q and r == True):
    print('Output: Matrícula válida do ano de {}'.format(student.getYear()))
    print('-------------------------------------------------------')
else:
    print('Output: Matrícula inválida')

