import re

from aocd import lines, submit


SENSOR_DATA_PATTERN = re.compile(r'.+x=(-?\d+), y=(-?\d+).+x=(-?\d+), y=(-?\d+)')
NO_BEACON_ROW = 2_000_000
MAX_XY = 4_000_000


def in_sensor_range(sx, sy, px, py):
    radius = cave[(sx, sy)]['radius']
    dist = abs(sx - px) + abs(sy - py)
    return dist <= radius


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

print('Part 1:', len(non_beacon_positions))

for sensor in sensors:
    x, y = sensor
    radius = cave[sensor]['radius']

    for i in range(-radius-1, radius+2):
        nx = x-i
        delta = radius + 1 - i

        if nx < 0 or nx > MAX_XY:
            continue

        for sensor2 in sensors:
            if sensor2 == sensor:
                continue
            if y+delta < 0 or y+delta > MAX_XY:
                break
            sx, sy = sensor2
            if in_sensor_range(sx, sy, nx, y+delta):
                break
        else:
            distress_beacon = (nx, y+delta)
            break

        # Don't check the same point twice.
        if delta == 0:
            continue

        for sensor2 in sensors:
            if sensor2 == sensor:
                continue
            if y-delta < 0 or y-delta > MAX_XY:
                break
            sx, sy = sensor2
            if in_sensor_range(sx, sy, nx, y-delta):
                break
        else:
            distress_beacon = (nx, y-delta)
            break

tuning_freq = distress_beacon[0] * MAX_XY + distress_beacon[1]
print('Part 2:', tuning_freq)
