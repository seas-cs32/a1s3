import time

i = 1
next_bound = 1

while True:
    i *= 2
    if i > next_bound:
        print(f'Passed {i}')
        next_bound *= 10
        time.sleep(0.5)
