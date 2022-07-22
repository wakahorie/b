from random import randint , shuffle , choice
import math as b

result_1  = b.pow(2,4)
print("result_1 is ", result_1 )

result_2 = b.sqrt(16)
print("result_2 is ", result_2 )

result_3 = randint(0,100)
print("result_3", result_3 )

names = ["a", "b", "c", "d"]
print("these are the original names" , names)

shuffle(names)
print("names after shuffling: ", names)

result_4 = choice(names)
print("chosen name is " , result_4)