from django.urls import reverse
from django.test import SimpleTestCase

class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")
    
    def test_homepage_contains_correct_home(self):
        self.assertContains(self.response, "homepage")
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This should not be on the page!")
                            


        
