#In this question we'll use List Comprehension with a For Loop to take all the 5 names we want.

#After that, all those names are printed in reverse order by using a For Loop
#with a additional parameter -1. That'll run the list through the fourth index till 0, that is,
#the last input till the first.

#finally, by default, python uses a 'space' to separate the strings. So we can use the 'sep'
#to modify this to a 'newline' instead of 'space'

names =  [input() for x in range(0,5) ]
print(names)
print(*(names[i] for i in range(4,-1,-1)), sep='\n' )