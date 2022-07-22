import random
import math

result_1  = math.pow(2,4)
print("result_1 is ", result_1 )

result_2 = math.sqrt(16)
print("result_2 is ", result_2 )

result_3 = random.randint(0,100)
print("result_3", result_3 )

names = ["a", "b", "c", "d"]
print("these are the original names" , names)

random.shuffle(names)
print("names after shuffling: ", names)

result_4 = random.choice(names)
print("chosen name is " , result_4)