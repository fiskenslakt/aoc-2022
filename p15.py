import re

from aocd import lines, submit

# lines = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.splitlines()

SENSOR_DATA_PATTERN = re.compile(r'.+x=(-?\d+), y=(-?\d+).+x=(-?\d+), y=(-?\d+)')
NO_BEACON_ROW = 2_000_000

cave = {}
sensors = []
beacons = []

for line in lines:
    sx, sy, bx, by = map(int, SENSOR_DATA_PATTERN.search(line).groups())
    sensor_radius = abs(sx - bx) + abs(sy - by)

    cave[(sx,sy)] = {'type': 'S', 'closest': (bx, by), 'radius': sensor_radius}
    cave[(bx,by)] = {'type': 'B', 'closest': (sx, sy)}

    sensors.append((sx, sy))
    beacons.append((bx, by))

non_beacon_positions = set()
for sensor in sensors:
    x, y = sensor
    radius = cave[sensor]['radius']

    delta = radius - abs(NO_BEACON_ROW - y)
    if delta <= 0:
        continue

    for nx in range(x-delta, x+delta+1):
        if (nx, NO_BEACON_ROW) in cave and cave[(nx, NO_BEACON_ROW)]['type'] == 'B':
            continue
        else:
            non_beacon_positions.add((nx, NO_BEACON_ROW))

print(len(non_beacon_positions))
