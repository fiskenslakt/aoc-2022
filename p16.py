import re
from functools import cache
# from collections import deque
# from heapq import heappop, heappush

from aocd import lines, submit

# lines = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II'''.splitlines()

REPORT_PATTERN = re.compile(r'Valve (..).+?(\d+).+valves? (.+)')
VOLCANO_ERUPTS = 30  # minutes

valve_rate = {}
graph = {}

for line in lines:
    valve, rate, child_valves = REPORT_PATTERN.search(line).groups()

    valve_rate[valve] = int(rate)
    graph[valve] = child_valves.split(', ')

# import pudb;pu.db

@cache
def dfs(minute, valve, flow, rp, open_valves):
    if minute == 30:
        return rp# , flow, open_valves
    if minute > 30:
        return 0

    pressures = []
    for child_valve in graph[valve]:
        if child_valve not in open_valves and valve_rate[child_valve] != 0:
            pressures.append(dfs(minute+2, child_valve, flow+valve_rate[child_valve], rp+flow+flow, open_valves | {child_valve}))
        else:
            pressures.append(dfs(minute+1, child_valve, flow, rp+flow, open_valves))

    return max(pressures)

submit(dfs(0, 'AA', 0, 0, frozenset()))

# import pudb;pu.db
# queue = deque([(0, 0, 0, 'AA', set(), [])])
# best_pressure = 0
# while queue:
#     # minute, flow, released_pressure, valve, open_valves, path = heappop(queue)
#     minute, flow, released_pressure, valve, open_valves, path = queue.popleft()

#     if minute == 30:
#         best_path = max(best_pressure, released_pressure)

#     for child_valve in graph[valve]:
#         if child_valve not in open_valves and valve_rate[child_valve] != 0:
#             # move to valve and open it
#             # heappush(queue, (minute+2, flow+valve_rate[child_valve], released_pressure+flow+flow, child_valve, open_valves | {child_valve}, path+[child_valve]))
#             queue.append((minute+2, flow+valve_rate[child_valve], released_pressure+flow+flow, child_valve, open_valves | {child_valve}, path+[child_valve]))
#         # just move to valve
#         queue.append((minute+1, flow, released_pressure+flow, child_valve, open_valves, path+[child_valve]))

# # print(flow, released_pressure, minute, valve, open_valves, path)
# print(best_pressure)
