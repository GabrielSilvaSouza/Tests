#In this code we'll use OOP to finish the quest instead of using Procedural Programming just for fun.
#Just for the record, the problem doesn't require OOP. It might even increase the loadwork, but once again, it's just for fun.

#Firstly, in our _init_ class, we'll define all our instance attributes that'll make up our DRE validation
#The DRE was subdivided in .year and .sequence using List Slicing to pull out the year and sequnce (Just to save some processing)

#Keeping going, we use "check_year" to verify if our DRE is in the inclusive range of 1900 and 2022(CURRENT YEAR).
#So, obviously, 2023 won't fit in our purpose. 

# check_dre_size and getYear just see if the dre is in the usual size(9) and compute the year of it using some basic operations.

# getDigit obtain the last number by summing up all digits taken in _init_ by self.sequence
#it uses, once again, List Compreehension to do so, however, to sum up we have, beforehand, convert each number to an integer by using int().
# The remainder must be equal the last digit, otherwise, it's not valid


class StudentDre:
    def __init__(self,dre):
        self.dre = dre
        self.year = int(dre[0:3])
        self.sequence = dre[3:8]
    
    def check_year(self):
        diff = 2022 - self.year
        if diff > 2022: 
            return False
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

if __name__ == '__main__':
    dre = input('Input: ')
    student = StudentDre(dre)

    if ( student.check_dre_size() and student.check_year() and student.getDigit() == True ):
        print('Output: Matrícula válida do ano de {}'.format(student.getYear()))
        print('-'*40, sep='')
    else:
        print('Output: Matrícula inválida')
        print('-'*30, sep='')

