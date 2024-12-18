import threading 
import math

def compute_fact_log(num,file):
    try:
        result = math.factorial(num)
        with open(file,'a') as f:
            f.write(f'\n{result}')
    except Exception as e:
        with open(file,'a') as f:
            f.write(f"error in computing factorial of number {num} : {e}")

numbers = [4,5,6,7]

file = 'fact_log.txt'

with open(file,'w') as f:
    f.write("taza taza logs\n")

threads = []

for num in numbers:
    thread = threading.Thread(target=compute_fact_log,args=(num,file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()