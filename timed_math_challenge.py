import random
import time

Operators=["+","-","*"]
min_value=2
max_value=5
problems=10
wrong=0

def generate_problem():
    left=random.randint(min_value,max_value)
    right=random.randint(min_value,max_value)
    operators=random.choice(Operators)

    exp = str(left) + " "+operators+" "+str(right)
    answer=eval(exp)
    return exp,answer

input("press any key to start: ")
print("----------------------")
start_time=time.time()

for i in range(problems):
    exp,answer = generate_problem()
    while True:
        guess=input("problem #"+str(i+1)+": "+exp+" =")
        if guess==str(answer):
            break
        wrong +=1

end_time=time.time()
total_time=round(end_time-start_time, 
                 2)

print("----------------------")
print("nice work! you finished in ",total_time,"seconds")
print(f"you got {wrong} times wrong answer")




