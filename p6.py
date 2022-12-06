from aocd import data

start_of_packet = None
start_of_message = None

for i, char in enumerate(data):
    if len(set(data[i-4:i])) == 4 and start_of_packet is None:
        start_of_packet = i
    if len(set(data[i-14:i])) == 14:
        start_of_message = i

    if start_of_packet and start_of_message:
        break

print('Part 1:', start_of_packet)
print('Part 2:', start_of_message)
