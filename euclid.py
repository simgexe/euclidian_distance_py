import math


points = [(1, 3), (3, 4), (5, 6), (0, 0), (-3, -4)]


def euclideandistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

distances = []

# Her nokta çifti arasındaki mesafe
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideandistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafe
min_distance = min(distances)
print(min_distance)

print(distances)