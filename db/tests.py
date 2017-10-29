from django import test
from django.urls import reverse
from db.urls import urlpatterns

class UrlsTest(test.TestCase):

    def test_responses(self):
        for url in urlpatterns:
            print(url)
            response = self.client.get(reverse(url.lookup_str))
            self.assertEqual(response.status_code, 200)
