from aocd import data, submit

for i, char in enumerate(data):
    # if len(set(data[i-4:i])) == 4:
    #     break
    if len(set(data[i-14:i])) == 14:
        break

submit(i)
