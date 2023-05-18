def calculate_distance(point1, point2):
    # Use pythagorean theorem to calculate distance between two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def find_closest_points(points_list):
    closest_points = []
    min_distance = float("inf")

    for i in range(len(points_list)):
        for j in range(i + 1, len(points_list)):
            distance = calculate_distance(points_list[i], points_list[j])

            # No need to continue as distance can't be shorter than 0
            if distance == 0:
                return [points_list[i], points_list[j]]

            if distance < min_distance:
                min_distance = distance
                closest_points = [points_list[i], points_list[j]]

    return closest_points
