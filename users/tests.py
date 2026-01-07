from django.test import TestCase
from django.urls import reverse

class CalculatorTest(TestCase):

    def test_calc_add(self):
        response = self.client.get('/calc/?num1=3&num2=7&op=%2B')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "10")