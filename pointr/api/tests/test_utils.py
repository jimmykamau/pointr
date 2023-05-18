import api.utils as api_utils
from django.test import TestCase


class CalculateDistanceTestCase(TestCase):
    def test_calculate_distance(self):
        distance = api_utils.calculate_distance((2, 2), (2, 2))
        self.assertEqual(distance, 0.0)


class FindClosestPointsTestCase(TestCase):
    def test_find_closest_distance(self):
        points_list = [(2, 2), (-1, 30), (20, 11), (4, 5)]
        closest_points = api_utils.find_closest_points(points_list)
        self.assertEqual(closest_points, [(2, 2), (4, 5)])
