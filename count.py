i = 0
next_bound = 1

while True:
    i += 1
    if i == next_bound:
        print(f'Reached {i}')
        next_bound *= 10
