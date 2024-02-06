#!/usr/bin/python3

"""
    Calculate the amount of rainwater retained between walls.

    Given a list of non-negative integers representing the heights of walls
    with unit width 1, as if viewing the cross-section of a relief map, this
    function calculates how many square units of water will be retained after
    it rains.
"""

def rain(walls):
    if not walls or len(walls) <= 2:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(1, n - 1):
        water_at_position = min(left_max[i], right_max[i]) - walls[i]
        total_water += max(0, water_at_position)

    return total_water

# Test cases
walls1 = [0, 1, 0, 2, 0, 3, 0, 4]
walls2 = [2, 0, 0, 4, 0, 0, 1, 0]

print(rain(walls1))  # Output: 6
print(rain(walls2))  # Output: 6

