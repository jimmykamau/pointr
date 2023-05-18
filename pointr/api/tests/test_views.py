from api.models import Points
from django.urls import reverse
from rest_framework.test import APITestCase


class CreatePointsApiTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("points-api")
        self.initial_data = self.client.post(
            self.url, {"points_list": "2,2;-1,30;20,11;4,5"}, format="json"
        )

    def test_post(self):
        self.assertEqual(self.initial_data.status_code, 201)
        self.assertEqual(self.initial_data.data["closest_points"], "2,2;4,5")

    def test_get(self):
        response = self.client.get(self.url)
        response_data = response.data[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_data["points_list"],
            "2,2;-1,30;20,11;4,5",
        )
        self.assertEqual(response_data["closest_points"], "2,2;4,5")

    def test_similar_post_not_creating_duplicates(self):
        data = {"points_list": "2,2;-1,30;20,11;4,5"}
        self.client.post(self.url, data, format="json")
        entries = Points.objects.count()
        self.assertEqual(entries, 1)
